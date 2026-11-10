# Walk-forward research 2026-11-10

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-14 13:30 to 2026-11-10 13:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -16.06%
- combos: 324 in 29s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 6.92 | 1.38 | 29 | 7.16 | 2.5 | 1.29 | 17 | 5.66 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 10.41 | 2.32 | 21 | 3.23 | -2.27 | 0.68 | 11 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 12.52 | 2.26 | 22 | 4.04 | 4.51 | 1.79 | 9 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 11.17 | 1.99 | 23 | 4.04 | 3.46 | 1.53 | 11 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 10.31 | 2.67 | 16 | 4.21 | 3.71 | 1.58 | 10 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 10.7 | 1.65 | 39 | 4.51 | -4.52 | 0.59 | 24 | 7.14 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 9.41 | 1.82 | 27 | 4.04 | -1.52 | 0.76 | 10 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=30d | 9.03 | 1.7 | 34 | 3.93 | -2.23 | 0.75 | 20 | 4.62 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 8.15 | 1.78 | 23 | 4.21 | 2.43 | 1.43 | 9 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 8.0 | 1.79 | 24 | 4.17 | -3.19 | 0.59 | 14 | 5.22 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=20d | 8.95 | 1.44 | 46 | 4.69 | -4.86 | 0.49 | 21 | 7.14 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
