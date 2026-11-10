# Walk-forward research 2026-11-10

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-14 22:30 to 2026-11-10 22:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -18.23%
- combos: 324 in 36s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 11.34 | 1.62 | 29 | 7.16 | 3.73 | 1.49 | 16 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 11.35 | 2.02 | 23 | 4.04 | 5.6 | 2.19 | 8 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 10.02 | 1.81 | 24 | 4.04 | 4.54 | 1.82 | 10 | 4.82 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 9.27 | 2.02 | 22 | 4.01 | -1.25 | 0.79 | 10 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 9.17 | 2.25 | 17 | 4.21 | 4.8 | 1.88 | 9 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 8.28 | 1.66 | 28 | 4.04 | -0.49 | 0.91 | 9 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=30d | 7.9 | 1.56 | 35 | 3.93 | -1.21 | 0.85 | 19 | 4.62 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 9.55 | 1.54 | 40 | 5.5 | -3.52 | 0.65 | 23 | 7.14 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 7.03 | 1.6 | 24 | 4.21 | 3.5 | 1.76 | 8 | 4.02 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 9.29 | 1.74 | 27 | 5.7 | 3.94 | 1.63 | 11 | 4.81 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 6.78 | 1.71 | 20 | 4.21 | 3.75 | 1.6 | 11 | 4.82 |

## Verdict

RECOMMEND: `{"setups": {"pullback": false, "breakout": true}, "atr_stop": 1.0, "atr_target": 10.0, "min_atr_pct": 0.5, "donchian_len": 30, "regime_ema": 1920, "regime_slope_bars": 288}` - best on train and beats current params out of sample. Apply via IMPROVE.md only if the live demo ledger does not contradict it.
