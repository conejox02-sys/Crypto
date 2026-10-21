# Walk-forward research 2026-10-21

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-24 20:45 to 2026-10-21 20:15 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +14.40%
- combos: 324 in 29s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 9.53 | 2.12 | 16 | 4.97 | 10.29 | 1.58 | 31 | 6.09 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 9.35 | 2.67 | 14 | 3.43 | 0.71 | 1.07 | 20 | 5.21 |
| breakout stop=1.5 tgt=5.0 minatr=0.5 donch=30 regime=30d | 8.72 | 2.51 | 14 | 3.46 | 3.67 | 1.28 | 19 | 5.36 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 8.26 | 2.26 | 16 | 3.43 | -1.43 | 0.88 | 24 | 7.23 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 10.54 | 2.25 | 22 | 4.45 | -2.32 | 0.88 | 43 | 8.83 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 9.39 | 2.41 | 14 | 4.04 | 5.14 | 1.47 | 20 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 9.39 | 2.41 | 14 | 4.04 | 7.49 | 1.85 | 17 | 4.02 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 10.63 | 2.9 | 16 | 4.73 | 1.88 | 1.14 | 27 | 5.23 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 10.36 | 2.78 | 17 | 4.73 | -0.34 | 0.98 | 30 | 5.6 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 10.75 | 2.89 | 14 | 4.96 | -0.53 | 0.97 | 40 | 8.29 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | 10.75 | 2.89 | 14 | 4.96 | 4.76 | 1.35 | 34 | 6.52 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
