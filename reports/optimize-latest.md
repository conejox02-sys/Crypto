# Walk-forward research 2026-09-27

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-03-31 20:15 to 2026-09-27 19:45 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +68.69%
- combos: 324 in 39s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 4.45 | 1.63 | 13 | 4.94 | 19.78 | 2.02 | 33 | 7.16 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | 5.45 | 2.25 | 12 | 4.93 | 16.25 | 2.15 | 34 | 6.52 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 4.72 | 1.94 | 13 | 4.93 | 10.38 | 1.54 | 40 | 8.29 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 4.45 | 1.63 | 13 | 4.94 | 19.78 | 2.02 | 33 | 7.16 |
| breakout stop=1.5 tgt=10.0 minatr=0.4 donch=30 regime=30d | 4.0 | 1.7 | 12 | 5.19 | 11.73 | 1.65 | 32 | 7.32 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=20 regime=30d | 3.5 | 1.44 | 14 | 4.94 | 14.71 | 1.62 | 37 | 7.16 |
| breakout stop=1.5 tgt=10.0 minatr=0.4 donch=20 regime=30d | 3.05 | 1.46 | 13 | 5.19 | 5.74 | 1.25 | 37 | 10.3 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=30 regime=30d | 2.52 | 1.48 | 13 | 4.37 | 10.17 | 1.7 | 36 | 6.52 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 2.2 | 1.83 | 13 | 4.13 | 12.82 | 1.89 | 30 | 5.7 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 2.21 | 1.32 | 18 | 4.43 | 8.67 | 1.4 | 47 | 6.56 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 1.95 | 1.67 | 14 | 4.13 | 10.35 | 1.63 | 33 | 5.7 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
