# Walk-forward research 2026-09-30

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-03 11:15 to 2026-09-30 10:45 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +64.52%
- combos: 324 in 37s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 4.45 | 1.63 | 13 | 4.94 | 18.25 | 1.87 | 35 | 7.16 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | 5.45 | 2.25 | 12 | 4.93 | 15.07 | 1.99 | 36 | 6.52 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 4.72 | 1.94 | 13 | 4.93 | 9.26 | 1.45 | 42 | 8.29 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 4.45 | 1.63 | 13 | 4.94 | 18.25 | 1.87 | 35 | 7.16 |
| breakout stop=1.5 tgt=10.0 minatr=0.4 donch=30 regime=30d | 4.0 | 1.7 | 12 | 5.19 | 10.31 | 1.53 | 34 | 7.32 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=20 regime=30d | 3.5 | 1.44 | 14 | 4.94 | 13.25 | 1.52 | 39 | 7.16 |
| breakout stop=1.5 tgt=10.0 minatr=0.4 donch=20 regime=30d | 3.05 | 1.46 | 13 | 5.19 | 4.39 | 1.18 | 39 | 10.3 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=30 regime=30d | 2.52 | 1.48 | 13 | 4.37 | 9.04 | 1.58 | 38 | 6.52 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 2.2 | 1.83 | 13 | 4.13 | 11.75 | 1.76 | 31 | 5.7 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 2.21 | 1.32 | 18 | 4.43 | 7.56 | 1.34 | 49 | 7.51 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 1.95 | 1.67 | 14 | 4.13 | 9.31 | 1.53 | 34 | 5.7 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
