"""Python port of the NinjaTrader `nasdaq2` strategy, plus optional protections.

The original (strategies/nasdaq2/nasdaq2_original.cs) is a session-open fade
with averaging:
- session open = open of the first bar of the session (here: 00:00 UTC day,
  crypto has no session); the first bar itself is skipped
- price closes >= 0.5% below the open -> buy 3; >= 0.5% above -> sell short 3
- only one initial entry per session (entryCount is not reset when flat)
- every further 200 ticks (NQ: 50 pts, ~0.2%) against the last entry -> add 3
  more, up to 5 entries (15 contracts)
- each entry has its OWN profit target at +0.1% from its fill
  (SetProfitTarget without fromEntrySignal)
- no per-trade stop. The "StopLossTotal" check reads CumProfit of ALL trades
  since the strategy started (realized only, never reset daily despite the
  comment), so it ignores the open loss that matters
- everything open is closed 30 s before the session ends

Fill model (same as NinjaTrader's historical defaults, conservative where it
is ambiguous): orders are decided on bar close and fill at the next bar's
open plus slippage; profit targets are limit orders that fill when the bar
trades at the target; when one bar reaches both a protective stop and a target,
the stop is assumed first. All amounts are in units of the per-entry notional
(1.0 = the value of one entry); `capital` = max_entries x that.
"""
import datetime as dt
from collections import defaultdict

ORIGINAL = {
    "entry_pct": 0.5,        # distance from the session open that triggers the first entry
    "step_pct": 0.2,         # adverse move between averaging entries (200 NQ ticks ~ 0.2%)
    "tp_pct": 0.1,           # profit target, % from fill
    "max_entries": 5,
    "allow_short": True,
    "tp_mode": "per_lot",    # "per_lot" (original) | "average" (whole position at avg + tp)
    "lifetime_stop": 0.002,  # original: -3000 USD of REALIZED lifetime P&L ~ 0.2% of one entry (3 NQ)
    # protections (off in the original)
    "vol_scale": False,      # scale entry/step/tp by the trailing average daily range
    "cycle_stop_pct": None,  # hard stop on the whole cycle (realized + open), % of one entry
                             # (scaled by volatility too when vol_scale is on)
    "trend_days": 0,         # only fade in the direction of the N-day EMA of daily closes
    "entry_window_h": 24,    # first entry only in the first N hours of the session
    "session_start_h": 0.0,  # 0 = midnight (crypto); NQ Globex from an ET export: 18
    # costs, per side, as fractions of notional
    "fee_taker": 0.00002,    # NQ-like: ~$4.5 RT on ~$500k notional
    "fee_maker": 0.00002,
    "slippage": 0.00001,     # ~1 NQ tick
}


SESSION = {"start_h": 0.0}  # session starts this many hours after 00:00 of the data's clock


def day_key(t):
    shifted = t - SESSION["start_h"] * 3600
    return dt.datetime.fromtimestamp(shifted, dt.timezone.utc).strftime("%Y-%m-%d")


def daily_table(bars):
    days = {}
    for b in bars:
        k = day_key(b["t"])
        d = days.get(k)
        if d is None:
            days[k] = {"o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"]}
        else:
            d["h"], d["l"], d["c"] = max(d["h"], b["h"]), min(d["l"], b["l"]), b["c"]
    keys = sorted(days)
    adr, ema = {}, {}
    ranges, e = [], None
    for k in keys:
        d = days[k]
        adr[k] = sum(ranges[-14:]) / len(ranges[-14:]) if ranges else None  # prior days only
        ema[k] = e
        ranges.append((d["h"] - d["l"]) / d["o"] * 100)
        e = d["c"] if e is None else e + (d["c"] - e) * 2 / (21 + 1)
    return days, adr, ema


def run(bars, p):
    """Returns (cycles, lots). A cycle = one session's position, first entry to flat."""
    p = dict(ORIGINAL, **p)
    SESSION["start_h"] = p["session_start_h"]
    days, adr, ema = daily_table(bars)
    if p["trend_days"]:
        ema = _ema_n(days, p["trend_days"])
    lots, cycles = [], []
    pos = []            # open lots: {side, px, tp, t}
    pending = []        # entries decided on the last close: (side, signal_close)
    pending_exit = None
    realized_life = 0.0
    state = {}
    cur_day = None

    def close_lot(lot, px, t, reason, maker=False):
        fee = p["fee_maker"] if maker else p["fee_taker"]
        gross = (px - lot["px"]) / lot["px"] if lot["side"] > 0 else (lot["px"] - px) / lot["px"]
        pnl = gross - fee - lot["fee_in"]
        lots.append({"t": t, "side": lot["side"], "entry": lot["px"], "exit": px, "pnl": pnl,
                     "reason": reason, "n": lot["n"]})
        state["cycle_pnl"] += pnl
        return pnl

    def finish_cycle(t):
        if state.get("cycle_open"):
            cycles.append({"day": state["day"], "pnl": state["cycle_pnl"], "entries": state["entries"],
                           "side": state["side"], "reason": state.get("end_reason", "")})
            state["cycle_open"] = False

    for i, b in enumerate(bars):
        k = day_key(b["t"])
        new_session = k != cur_day
        # 1. fills at the open
        if pending_exit and pos:
            px = b["o"] * (1 - p["slippage"] * pos[0]["side"])
            for lot in pos:
                realized_life += close_lot(lot, px, b["t"], pending_exit)
            pos = []
            state["end_reason"] = pending_exit
            finish_cycle(b["t"])
        pending_exit = None
        for side, _sig in pending:
            px = b["o"] * (1 + p["slippage"] * side)
            tp_mult = state["tp"] / 100
            pos.append({"side": side, "px": px, "fee_in": p["fee_taker"], "n": state["entries"],
                        "tp": px * (1 + tp_mult * side), "t": b["t"]})
        pending = []
        # 2. intrabar: cycle stop, then targets
        if pos:
            side = pos[0]["side"]
            if state.get("stop") is not None:
                # price where realized + open P&L of the cycle = -stop (per-entry units)
                q = [1 / lot["px"] for lot in pos]  # units per 1.0 notional
                fees = sum(lot["fee_in"] + p["fee_taker"] for lot in pos)
                target_loss = -state["stop"] / 100 - state["cycle_pnl"] + fees
                # side*(sum(q)*P - len) = target_loss  ->  P
                stop_px = (len(pos) + side * target_loss) / sum(q)
                hit = (b["l"] <= stop_px) if side > 0 else (b["h"] >= stop_px)
                if hit:
                    gap = (b["o"] <= stop_px) if side > 0 else (b["o"] >= stop_px)
                    px = b["o"] if gap else stop_px
                    px *= (1 - p["slippage"] * side)
                    for lot in pos:
                        realized_life += close_lot(lot, px, b["t"], "cycle_stop")
                    pos = []
                    state["end_reason"] = "cycle_stop"
                    finish_cycle(b["t"])
            if pos and p["tp_mode"] == "per_lot":
                keep = []
                for lot in pos:
                    hit = b["h"] >= lot["tp"] if side > 0 else b["l"] <= lot["tp"]
                    if hit:
                        realized_life += close_lot(lot, lot["tp"], b["t"], "target", maker=True)
                    else:
                        keep.append(lot)
                pos = keep
            elif pos:  # one target for the whole position at average price + tp
                avg = len(pos) / sum(1 / lot["px"] for lot in pos)
                tp = avg * (1 + state["tp"] / 100 * side)
                if (b["h"] >= tp) if side > 0 else (b["l"] <= tp):
                    for lot in pos:
                        realized_life += close_lot(lot, tp, b["t"], "target", maker=True)
                    pos = []
            if not pos and state.get("cycle_open"):
                state["end_reason"] = state.get("end_reason") or "target"
                finish_cycle(b["t"])

        # 3. bar close logic (OnBarUpdate)
        last_of_day = i + 1 == len(bars) or day_key(bars[i + 1]["t"]) != k
        if new_session:
            cur_day = k
            a = adr.get(k)
            scale = (a / 1.3) if (p["vol_scale"] and a) else 1.0  # 1.3% ~ NQ average daily range
            state.update({"day": k, "open": b["o"], "entries": 0, "last": 0.0,
                          "cycle_open": False, "cycle_pnl": 0.0, "end_reason": "",
                          "entry": p["entry_pct"] * scale, "step": p["step_pct"] * scale,
                          "tp": p["tp_pct"] * scale, "start": b["t"],
                          "stop": p["cycle_stop_pct"] * scale if p["cycle_stop_pct"] else None,
                          "trend": ema.get(k) if p["trend_days"] else None, "side": 0})
            if p["vol_scale"] and not a:
                state["entries"] = p["max_entries"]  # no ADR yet: skip the day
            continue
        if last_of_day:
            if pos:
                px = b["c"] * (1 - p["slippage"] * pos[0]["side"])
                for lot in pos:
                    realized_life += close_lot(lot, px, b["t"], "session_close")
                pos = []
                state["end_reason"] = "session_close"
                finish_cycle(b["t"])
            continue
        if p["lifetime_stop"] is not None and realized_life <= -p["lifetime_stop"] and pos:
            pending_exit = "lifetime_stop"
            continue
        c = b["c"]
        chg = (c - state["open"]) / state["open"] * 100
        if not pos and state["entries"] == 0 and b["t"] - state["start"] < p["entry_window_h"] * 3600:
            side = 1 if chg <= -state["entry"] else (-1 if chg >= state["entry"] and p["allow_short"] else 0)
            tr = state["trend"]
            if side and tr is not None and ((side > 0 and c < tr) or (side < 0 and c > tr)):
                side = 0
            if side:
                pending.append((side, c))
                state.update({"last": c, "cycle_open": True, "side": side, "entries": 1})
        elif pos and state["entries"] < p["max_entries"]:
            side = pos[0]["side"]
            step = state["last"] * state["step"] / 100
            if (side > 0 and c <= state["last"] - step) or (side < 0 and c >= state["last"] + step):
                pending.append((side, c))
                state["last"] = c
                state["entries"] += 1
    return cycles, lots


def _ema_n(days, n):
    out, e = {}, None
    for k in sorted(days):
        out[k] = e
        c = days[k]["c"]
        e = c if e is None else e + (c - e) * 2 / (n + 1)
    return out


def report(cycles, lots, p, n_days):
    p = dict(ORIGINAL, **p)
    capital = p["max_entries"]  # per-entry notional units
    pnl = [c["pnl"] for c in cycles]
    wins = [x for x in pnl if x > 0]
    losses = [x for x in pnl if x <= 0]
    eq, peak, dd = 0.0, 0.0, 0.0
    for x in pnl:
        eq += x
        peak = max(peak, eq)
        dd = max(dd, peak - eq)
    lot_w = sum(1 for lot in lots if lot["pnl"] > 0)
    by_reason = defaultdict(lambda: [0, 0.0])
    for c in cycles:
        by_reason[c["reason"]][0] += 1
        by_reason[c["reason"]][1] += c["pnl"]
    gw, gl = sum(wins), -sum(losses)
    return {
        "days": n_days, "cycles": len(cycles),
        "lot_win_rate_pct": round(lot_w / len(lots) * 100, 1) if lots else 0,
        "cycle_win_rate_pct": round(len(wins) / len(pnl) * 100, 1) if pnl else 0,
        "return_on_capital_pct": round(sum(pnl) / capital * 100, 2),
        "max_drawdown_pct": round(dd / capital * 100, 2),
        "profit_factor": round(gw / gl, 2) if gl else float("inf"),
        "avg_win_pct": round(sum(wins) / len(wins) * 100, 3) if wins else 0,
        "avg_loss_pct": round(sum(losses) / len(losses) * 100, 3) if losses else 0,
        "worst_cycle_pct": round(min(pnl) * 100, 2) if pnl else 0,
        "best_cycle_pct": round(max(pnl) * 100, 2) if pnl else 0,
        "full_ladder_cycles": sum(1 for c in cycles if c["entries"] >= p["max_entries"]),
        "exits": {k: (v[0], round(v[1] * 100, 2)) for k, v in sorted(by_reason.items())},
    }


def load_ninjatrader(path):
    """NinjaTrader export (Tools > Historical Data > Export, 1 Minute):
    `yyyyMMdd HHmmss;open;high;low;close;volume`, time = bar END in the PC's
    time zone. Times are kept on that clock (treated as UTC for arithmetic)."""
    out = []
    with open(path) as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) < 6:
                continue
            end = dt.datetime.strptime(parts[0], "%Y%m%d %H%M%S").replace(tzinfo=dt.timezone.utc)
            o, h, lo, c, v = (float(x) for x in parts[1:6])
            out.append({"t": int(end.timestamp()) - 60, "o": o, "h": h, "l": lo, "c": c, "v": v})
    out.sort(key=lambda b: b["t"])
    return out
