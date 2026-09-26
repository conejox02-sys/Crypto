"""Walk-forward parameter research. Proposes; never applies.

    python3 core/optimize.py --days 60

Splits the history into TRAIN (first 2/3) and TEST (last 1/3). Every grid
combination is ranked on TRAIN only; TEST is the out-of-sample check nobody
optimised on. A candidate is RECOMMENDED only if it also beats the current
params out of sample. The report lands in reports/; applying it is a strategy
edit (IMPROVE.md), made with the evidence cited.
"""
import argparse
import itertools
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
import backtest  # noqa: E402
import common  # noqa: E402
import stats  # noqa: E402

GRID = {
    "setups": [{"pullback": True, "breakout": False},
               {"pullback": False, "breakout": True},
               {"pullback": True, "breakout": True}],
    "atr_stop": [1.0, 1.5, 2.0],
    "atr_target": [1.5, 2.5, 3.5],
    "rsi_pullback": [35, 42, 50],
    "trail_atr": [0.0, 2.0],
    "min_atr_pct": [0.1, 0.2],
}
MIN_TRAIN_TRADES = 15
MIN_TEST_TRADES = 6


def score(s):
    """Return per unit of drawdown, zero-floored on too few trades."""
    if s["trades"] < MIN_TRAIN_TRADES:
        return -1e9
    return s["return_pct"] / max(s["max_drawdown_pct"] or 0, 1.0)


def evaluate(candles, split, params, cfg, signals):
    start = cfg["starting_balance_usdt"]
    ev, _, curve = backtest.run(candles[:split], params, cfg, signals)
    tr = stats.summarize([e for e in ev if e["type"] == "exit"], start, curve)
    ev, _, curve = backtest.run(candles, params, cfg, signals, start_index=split)
    te = stats.summarize([e for e in ev if e["type"] == "exit"], start, curve)
    for s in (tr, te):
        s.pop("breakdown", None)
    return tr, te


def label(p):
    setups = "+".join(k for k, v in p["setups"].items() if v) or "none"
    return (f"{setups} stop={p['atr_stop']} tgt={p['atr_target']} rsi={p['rsi_pullback']} "
            f"trail={p['trail_atr']} minatr={p['min_atr_pct']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--file")
    ap.add_argument("--top", type=int, default=10)
    a = ap.parse_args()
    cfg = common.load_json(common.CONFIG)
    current = common.load_json(common.PARAMS)
    signals = common.load_signals()
    if a.file:
        candles, src = common.load_json(a.file), "file:" + a.file
    else:
        candles, src = backtest.fetch(cfg, a.days)
    split = len(candles) * 2 // 3
    t0 = time.time()

    cur_tr, cur_te = evaluate(candles, split, current, cfg, signals)
    results = []
    keys = list(GRID)
    for combo in itertools.product(*(GRID[k] for k in keys)):
        p = dict(current)
        p.update(dict(zip(keys, combo)))
        if p["atr_target"] <= p["atr_stop"] * 0.75:
            continue
        if not p["setups"]["pullback"] and p["rsi_pullback"] != GRID["rsi_pullback"][0]:
            continue  # rsi only matters to the pullback setup
        tr, te = evaluate(candles, split, p, cfg, signals)
        results.append({"params": {k: p[k] for k in keys}, "train": tr, "test": te,
                        "score": score(tr)})
    results.sort(key=lambda r: r["score"], reverse=True)
    top = results[:a.top]

    best = top[0] if top else None
    rec = None
    if best and best["test"]["trades"] >= MIN_TEST_TRADES \
            and best["test"]["return_pct"] > cur_te["return_pct"] \
            and (best["test"]["profit_factor"] or 0) > 1.1:
        rec = best

    day = time.strftime("%Y-%m-%d", time.gmtime())
    first, last = candles[0]["t"], candles[-1]["t"]
    fmt = lambda t: time.strftime("%Y-%m-%d %H:%M", time.gmtime(t))  # noqa: E731
    lines = [
        f"# Walk-forward research {day}", "",
        f"- data: {src}, {len(candles)} x {cfg['timeframe']} bars, {fmt(first)} to {fmt(last)} UTC",
        f"- train: first {split} bars; test (out of sample): last {len(candles) - split} bars",
        f"- buy & hold over test: {(candles[-1]['c'] / candles[split]['c'] - 1) * 100:+.2f}%",
        f"- combos: {len(results)} in {time.time() - t0:.0f}s", "",
        "| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |",
        "|---|---|---|---|---|---|---|---|---|",
        f"| **current params** | {cur_tr['return_pct']} | {cur_tr['profit_factor']} | {cur_tr['trades']} | "
        f"{cur_tr['max_drawdown_pct']} | {cur_te['return_pct']} | {cur_te['profit_factor']} | "
        f"{cur_te['trades']} | {cur_te['max_drawdown_pct']} |",
    ]
    for r in top:
        p = dict(current)
        p.update(r["params"])
        tr, te = r["train"], r["test"]
        lines.append(f"| {label(p)} | {tr['return_pct']} | {tr['profit_factor']} | {tr['trades']} | "
                     f"{tr['max_drawdown_pct']} | {te['return_pct']} | {te['profit_factor']} | "
                     f"{te['trades']} | {te['max_drawdown_pct']} |")
    lines += ["", "## Verdict", ""]
    if rec:
        lines.append(f"RECOMMEND: `{json.dumps(rec['params'])}` - best on train and beats current "
                     "params out of sample. Apply via IMPROVE.md only if the live demo ledger "
                     "does not contradict it.")
    else:
        lines.append("KEEP current params: no train-best config beat them out of sample "
                     f"with >= {MIN_TEST_TRADES} trades and PF > 1.1.")
    text = "\n".join(lines) + "\n"
    os.makedirs(common.REPORTS, exist_ok=True)
    with open(os.path.join(common.REPORTS, "optimize-latest.md"), "w") as f:
        f.write(text)
    common.save_json(os.path.join(common.REPORTS, f"optimize-{day}.json"),
                     {"source": src, "bars": len(candles), "split": split,
                      "current": {"train": cur_tr, "test": cur_te},
                      "top": top, "recommended": rec["params"] if rec else None})
    print(text)


if __name__ == "__main__":
    main()
