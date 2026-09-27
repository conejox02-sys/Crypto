"""Backtest the original nasdaq2 and the protected version side by side.

    # NQ/MNQ exported from NinjaTrader (1 minute, ET clock, Globex session 18:00):
    python3 strategies/nasdaq2/run_backtest.py --nt NQ_1min.txt --session-start 18

    # SOL-USDT 1m from KuCoin (data/ in this repo), KuCoin futures fees:
    python3 strategies/nasdaq2/run_backtest.py --json data/sol-1m-365d.json.gz --costs kucoin_futures

Amounts are % of capital, where capital = MaxEntries x one entry's notional
(no leverage). Multiply by your leverage to see it in account terms.
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "core"))
import fade  # noqa: E402

COSTS = {
    "nq": {"fee_taker": 0.00002, "fee_maker": 0.00002, "slippage": 0.00001},
    "kucoin_futures": {"fee_taker": 0.0006, "fee_maker": 0.0002, "slippage": 0.0001},
    "kucoin_spot": {"fee_taker": 0.001, "fee_maker": 0.001, "slippage": 0.0001, "allow_short": False},
}
ORIGINAL = {}
PROTECTED = {"vol_scale": True, "tp_mode": "per_lot", "tp_pct": 0.3, "cycle_stop_pct": 0.2,
             "trend_days": 40, "lifetime_stop": None}
# Crypto adaptation (KuCoin futures fees): no averaging, entry further out, wider stop.
CRYPTO = {"vol_scale": True, "tp_mode": "per_lot", "max_entries": 1, "entry_pct": 1.0, "tp_pct": 0.3,
          "cycle_stop_pct": 0.5, "trend_days": 40, "lifetime_stop": None}


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--nt", help="NinjaTrader 1-minute export (.txt)")
    src.add_argument("--json", help="candles JSON (.json or .json.gz) from this repo")
    ap.add_argument("--session-start", type=float, default=None,
                    help="hour the session starts on the data's clock (default: 18 for --nt, 0 for --json)")
    ap.add_argument("--costs", choices=sorted(COSTS), default="nq")
    a = ap.parse_args()
    if a.nt:
        bars = fade.load_ninjatrader(a.nt)
        start = 18.0 if a.session_start is None else a.session_start
    else:
        import common
        bars = common.load_json(a.json)
        start = 0.0 if a.session_start is None else a.session_start
    print(f"{len(bars)} bars, session start {start:g}h, costs {a.costs}")
    for name, p in (("ORIGINAL (as written, incl. the CumProfit stop)", ORIGINAL),
                    ("ORIGINAL without the CumProfit bug", {"lifetime_stop": None}),
                    ("PROTECTED (nasdaq2_blindada defaults)", PROTECTED),
                    ("CRYPTO (single entry, no averaging)", CRYPTO)):
        p = dict(p, session_start_h=start, **COSTS[a.costs])
        cycles, lots = fade.run(bars, p)
        print(f"\n== {name}\n" + json.dumps(fade.report(cycles, lots, p, 0), indent=2))


if __name__ == "__main__":
    main()
