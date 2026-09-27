"""Run the CRYPTO preset (single-entry day-trading fade) on several coins at
once and report per coin and for the combined portfolio.

    python3 strategies/nasdaq2/multi_coin.py data/*-1m-365d.json.gz

Every position opens and closes within the same UTC day. The portfolio puts
the same notional on each coin; capital = coins x one position.
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "core"))
import common  # noqa: E402
import fade  # noqa: E402
from run_backtest import COSTS, CRYPTO  # noqa: E402

VARIANTS = {"entry 0.9": {"entry_pct": 0.9}, "entry 1.0 (preset)": {}, "entry 1.1": {"entry_pct": 1.1}}


def main(paths, costs="kucoin_futures"):
    lines = ["# Day-trading fade on several coins (KuCoin futures fees)", ""]
    for vname, over in VARIANTS.items():
        p = dict(CRYPTO, **COSTS[costs], **over)
        per_day = collections.defaultdict(float)
        trades_day = collections.Counter()
        rows, n_days = [], set()
        for path in paths:
            name = os.path.basename(path).split("-1m-")[0].upper()
            bars = common.load_json(path)
            cycles, lots = fade.run(bars, p)
            r = fade.report(cycles, lots, p, 0)
            half = bars[len(bars) * 2 // 3]["t"]
            late = fade.day_key(half)
            first = sum(c["pnl"] for c in cycles if c["day"] < late) * 100
            second = sum(c["pnl"] for c in cycles if c["day"] >= late) * 100
            bh = (bars[-1]["c"] / bars[0]["o"] - 1) * 100
            rows.append(f"| {name} | {r['cycles']} | {r['cycle_win_rate_pct']} | {r['return_on_capital_pct']:+.2f}% | "
                        f"{first:+.2f}% / {second:+.2f}% | {r['max_drawdown_pct']:.2f}% | {r['profit_factor']} | {bh:+.1f}% |")
            for c in cycles:
                per_day[c["day"]] += c["pnl"]
                trades_day[c["day"]] += 1
            n_days |= {fade.day_key(b["t"]) for b in bars[::1440]}
        n = len(paths)
        eq = peak = dd = 0.0
        for d in sorted(per_day):
            eq += per_day[d] / n
            peak = max(peak, eq)
            dd = max(dd, peak - eq)
        days_total = max(len(n_days), 1)
        lines += [f"## {vname}", "",
                  "| coin | trades | win % | year | first 8 mo / last 4 mo | max DD | PF | buy & hold |",
                  "|---|---|---|---|---|---|---|---|", *rows, "",
                  f"**Portfolio ({n} coins, equal size):** {eq * 100:+.2f}% on capital, max drawdown {dd * 100:.2f}%, "
                  f"{sum(trades_day.values())} trades = {sum(trades_day.values()) / days_total:.2f} per day, "
                  f"days with at least one trade: {len(trades_day)}/{days_total} "
                  f"({len(trades_day) / days_total * 100:.0f}%).", ""]
    text = "\n".join(lines)
    os.makedirs(os.path.join(common.ROOT, "reports"), exist_ok=True)
    with open(os.path.join(common.ROOT, "reports", "multi-coin-fade.md"), "w") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main(sys.argv[1:])
