# Walk-forward research 2026-10-20

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-23 10:00 to 2026-10-20 09:30 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +13.37%
- combos: 324 in 37s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 5.83 | 1.81 | 14 | 4.97 | 14.15 | 1.72 | 33 | 7.16 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 5.78 | 2.7 | 12 | 4.73 | 6.5 | 1.41 | 30 | 5.7 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 5.84 | 2.35 | 12 | 4.96 | 4.08 | 1.2 | 42 | 8.29 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | 5.84 | 2.35 | 12 | 4.96 | 9.61 | 1.62 | 36 | 6.52 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=20 regime=30d | 5.83 | 1.81 | 14 | 4.97 | 9.32 | 1.39 | 37 | 7.85 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 5.83 | 1.81 | 14 | 4.97 | 14.15 | 1.72 | 33 | 7.16 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 5.52 | 2.52 | 13 | 4.73 | 4.17 | 1.23 | 33 | 5.7 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 5.07 | 1.71 | 19 | 4.45 | 2.76 | 1.13 | 46 | 8.83 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 4.55 | 1.85 | 12 | 4.04 | 10.01 | 1.79 | 22 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 4.55 | 1.85 | 12 | 4.04 | 12.47 | 2.19 | 19 | 4.02 |
| breakout stop=1.5 tgt=10.0 minatr=0.4 donch=20 regime=30d | 5.32 | 2.1 | 12 | 5.22 | 0.04 | 1.0 | 38 | 10.3 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
