"""Backtest strategy/params.json on historical candles.

    python3 core/backtest.py --days 30              # fetch from KuCoin
    python3 core/backtest.py --file data/x.json     # candles saved earlier

Signals fire on a closed bar; entries fill at the NEXT bar's open (+slippage).
"""
import argparse
import gzip
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
import common  # noqa: E402
import engine  # noqa: E402
import market  # noqa: E402
import stats  # noqa: E402


def run(candles, params, cfg, signals, start_index=None):
    """Returns (events, final_account, equity_curve)."""
    bar_sec = market.TF_SEC[cfg["timeframe"]]
    x = signals.prepare(candles, params)
    acct = engine.Account(cfg, params)
    events, curve = [], []
    pending = None
    first = max(signals.warmup(params), start_index or 0)
    for i in range(first, len(candles)):
        bar = candles[i]
        if pending is not None:
            ok, _ = acct.can_enter(bar["t"], bar["o"])
            if ok:
                ev = acct.enter(bar["t"], bar["o"], pending)
                if ev:
                    events.append(ev)
            pending = None
        ev = acct.on_bar(bar, bar_sec)
        if ev:
            events.append(ev)
        if acct.pos is None:
            sig = signals.signal(x, i, acct.p)
            if sig:
                pending = sig
        curve.append((bar["t"] + bar_sec, acct.equity(bar["c"])))
    if acct.pos is not None and candles:
        last = candles[-1]
        events.append(acct._exit(last["t"] + bar_sec, last["c"] * (1 - acct.slip), "end_of_data"))
        curve.append((last["t"] + bar_sec, acct.cash))
    return events, acct, curve


def fetch(cfg, days, tf=None):
    tf = tf or cfg["timeframe"]
    end = int(time.time())
    start = end - days * 86400
    rows, src = market.candles(cfg["symbol"], tf, start, end)
    return market.closed_only(rows, tf, end), src


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--file")
    ap.add_argument("--save", help="save fetched candles to this JSON file")
    ap.add_argument("--params", default=common.PARAMS)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--tf", help="candle timeframe to fetch (default: config timeframe)")
    ap.add_argument("--fetch-only", action="store_true", help="save candles, skip the backtest")
    a = ap.parse_args()
    cfg = common.load_json(common.CONFIG)
    params = common.load_json(a.params)
    if a.file:
        candles, src = common.load_json(a.file), "file:" + a.file
    else:
        candles, src = fetch(cfg, a.days, a.tf)
        if a.save:
            os.makedirs(os.path.dirname(os.path.abspath(a.save)), exist_ok=True)
            opener = gzip.open if a.save.endswith(".gz") else open
            with opener(a.save, "wt") as f:  # compact: one candle per line
                f.write("[\n" + ",\n".join(json.dumps(c, separators=(",", ":")) for c in candles) + "\n]\n")
        if a.fetch_only:
            print(f"saved {len(candles)} x {a.tf or cfg['timeframe']} candles from {src} to {a.save}")
            return
    events, acct, curve = run(candles, params, cfg, common.load_signals())
    s = stats.summarize([e for e in events if e["type"] == "exit"],
                        cfg["starting_balance_usdt"], curve)
    s.update({"source": src, "bars": len(candles),
              "buy_and_hold_pct": round((candles[-1]["c"] / candles[0]["c"] - 1) * 100, 2)
              if candles else None})
    if a.json:
        print(json.dumps(s, indent=2))
    else:
        print(stats.render(s, "Backtest " + cfg["symbol"] + " " + cfg["timeframe"]))


if __name__ == "__main__":
    main()
