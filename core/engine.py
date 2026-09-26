"""Trading engine shared by the backtester and the paper (demo) account.

Honest-fill rules (the same in backtest and paper):
- Market entries pay the taker fee plus `slippage_bps` over the reference
  price (next bar's open in backtests, the live best ask in paper ticks).
- The stop is a resting stop-market order: a bar that opens through it fills
  at the open (gap), otherwise at the stop; both minus slippage, plus fee.
- The target is a resting limit sell: fills at the target, taker fee charged
  anyway (conservative).
- When one bar touches both stop and target, the STOP is assumed first.
- Trailing / breakeven stop moves use a bar's high only from the next bar on.
- Risk caps from config/protected.json clamp strategy/params.json.
"""
import datetime as dt

from market import TF_SEC


def effective_params(params, cfg):
    p = dict(params)
    ceil = cfg["ceilings"]
    for k in ("risk_per_trade_pct", "position_pct", "daily_loss_pct", "trades_per_day"):
        p[k] = min(p[k], ceil[k])
    return p


def day_of(ts):
    return dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime("%Y-%m-%d")


class Account:
    def __init__(self, cfg, params, state=None):
        self.cfg = cfg
        self.p = effective_params(params, cfg)
        self.fee = cfg["taker_fee"]
        self.slip = cfg["slippage_bps"] / 10000.0
        s = state or {}
        self.cash = s.get("cash", cfg["starting_balance_usdt"])
        self.pos = s.get("pos")
        self.day = s.get("day")
        self.day_start_equity = s.get("day_start_equity", self.cash)
        self.day_pnl = s.get("day_pnl", 0.0)
        self.trades_today = s.get("trades_today", 0)
        self.cooldown_until = s.get("cooldown_until", 0)
        self.trade_seq = s.get("trade_seq", 0)

    def state(self):
        return {"cash": self.cash, "pos": self.pos, "day": self.day,
                "day_start_equity": self.day_start_equity, "day_pnl": self.day_pnl,
                "trades_today": self.trades_today, "cooldown_until": self.cooldown_until,
                "trade_seq": self.trade_seq}

    def equity(self, mark):
        return self.cash + (self.pos["qty"] * mark if self.pos else 0.0)

    def _roll_day(self, ts, mark):
        d = day_of(ts)
        if d != self.day:
            self.day = d
            self.day_start_equity = self.equity(mark)
            self.day_pnl = 0.0
            self.trades_today = 0

    def can_enter(self, ts, mark):
        """Returns (ok, reason)."""
        self._roll_day(ts, mark)
        if self.pos:
            return False, "in_position"
        if ts < self.cooldown_until:
            return False, "cooldown"
        if self.trades_today >= self.p["trades_per_day"]:
            return False, "max_trades_today"
        if self.day_pnl <= -self.p["daily_loss_pct"] / 100.0 * self.day_start_equity:
            return False, "daily_loss_limit"
        return True, ""

    def enter(self, ts, ref_price, sig):
        """Market buy at ref_price (+slippage). Returns the entry event or None."""
        fill = ref_price * (1 + self.slip)
        a = sig["atr"]
        stop = fill - self.p["atr_stop"] * a
        target = fill + self.p["atr_target"] * a
        risk_per_unit = fill - stop
        if risk_per_unit <= 0:
            return None
        eq = self.cash
        qty_risk = (self.p["risk_per_trade_pct"] / 100.0 * eq) / risk_per_unit
        qty_cap = (self.p["position_pct"] / 100.0 * eq) / (fill * (1 + self.fee))
        qty = min(qty_risk, qty_cap)
        if qty * fill < 5:  # below a sensible KuCoin minimum order value
            return None
        cost = qty * fill
        fee = cost * self.fee
        self.cash -= cost + fee
        self.trade_seq += 1
        self.trades_today += 1
        self.pos = {"id": self.trade_seq, "setup": sig["setup"], "entry_ts": ts,
                    "entry": fill, "qty": qty, "stop": stop, "init_stop": stop,
                    "target": target, "atr": a, "entry_fee": fee, "high": fill,
                    "equity_at_entry": eq}
        return {"type": "entry", "id": self.trade_seq, "ts": ts, "setup": sig["setup"],
                "price": round(fill, 4), "qty": round(qty, 6), "stop": round(stop, 4),
                "target": round(target, 4), "atr": round(a, 4), "fee": round(fee, 4),
                "cash_after": round(self.cash, 4)}

    def _exit(self, ts, price, reason):
        pos = self.pos
        proceeds = pos["qty"] * price
        fee = proceeds * self.fee
        self.cash += proceeds - fee
        pnl = proceeds - fee - (pos["qty"] * pos["entry"] + pos["entry_fee"])
        r_unit = pos["qty"] * (pos["entry"] - pos["init_stop"])
        self.day_pnl += pnl
        if pnl < 0:
            bar = TF_SEC[self.cfg["timeframe"]]
            self.cooldown_until = ts + self.p["cooldown_bars_after_loss"] * bar
        self.pos = None
        return {"type": "exit", "id": pos["id"], "ts": ts, "setup": pos["setup"],
                "reason": reason, "entry": round(pos["entry"], 4), "price": round(price, 4),
                "qty": round(pos["qty"], 6), "pnl": round(pnl, 4),
                "r": round(pnl / r_unit, 3) if r_unit > 0 else 0.0,
                "fees": round(fee + pos["entry_fee"], 4),
                "held_min": round((ts - pos["entry_ts"]) / 60, 1),
                "cash_after": round(self.cash, 4)}

    def on_bar(self, bar, bar_sec):
        """Manage the open position through one CLOSED bar (any timeframe).
        Returns an exit event or None."""
        pos = self.pos
        if not pos:
            return None
        self._roll_day(bar["t"], bar["o"])
        close_ts = bar["t"] + bar_sec
        if bar["o"] <= pos["stop"]:
            return self._exit(close_ts, bar["o"] * (1 - self.slip), "stop_gap")
        if bar["l"] <= pos["stop"]:
            reason = "stop" if pos["stop"] < pos["entry"] else "trail_stop"
            return self._exit(close_ts, pos["stop"] * (1 - self.slip), reason)
        if bar["h"] >= pos["target"]:
            return self._exit(close_ts, pos["target"], "target")
        if close_ts - pos["entry_ts"] >= self.p["max_hold_minutes"] * 60:
            return self._exit(close_ts, bar["c"] * (1 - self.slip), "time")
        # Stop management applies from the next bar on.
        pos["high"] = max(pos["high"], bar["h"])
        r = pos["entry"] - pos["init_stop"]
        if self.p["breakeven_at_r"] > 0 and pos["high"] >= pos["entry"] + self.p["breakeven_at_r"] * r:
            be = pos["entry"] * (1 + 2 * self.fee)  # covers both fees
            pos["stop"] = max(pos["stop"], be)
        if self.p["trail_atr"] > 0 and pos["high"] > pos["entry"] + r:
            pos["stop"] = max(pos["stop"], pos["high"] - self.p["trail_atr"] * pos["atr"])
        return None
