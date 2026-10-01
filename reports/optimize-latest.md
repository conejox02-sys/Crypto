# Walk-forward research 2026-10-01

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-04 11:45 to 2026-10-01 11:15 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +61.18%
- combos: 324 in 37s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 5.34 | 1.85 | 12 | 4.94 | 18.22 | 1.87 | 36 | 7.16 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 5.39 | 2.22 | 12 | 4.93 | 9.22 | 1.45 | 43 | 8.29 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 5.34 | 1.85 | 12 | 4.94 | 18.22 | 1.87 | 36 | 7.16 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=20 regime=30d | 4.37 | 1.61 | 13 | 4.94 | 13.22 | 1.52 | 40 | 7.16 |
| breakout stop=1.5 tgt=10.0 minatr=0.4 donch=20 regime=30d | 3.92 | 1.67 | 12 | 5.19 | 4.36 | 1.18 | 40 | 10.3 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=30 regime=30d | 3.17 | 1.69 | 12 | 4.37 | 9.01 | 1.58 | 39 | 6.52 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 2.86 | 1.45 | 17 | 4.43 | 7.53 | 1.33 | 50 | 7.54 |
| breakout stop=2.0 tgt=8.0 minatr=0.4 donch=30 regime=30d | 3.57 | 1.5 | 12 | 5.56 | 12.04 | 1.54 | 36 | 7.82 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=20 regime=30d | 2.47 | 1.47 | 13 | 4.37 | 3.54 | 1.17 | 45 | 8.29 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 2.23 | 1.85 | 12 | 4.13 | 11.75 | 1.76 | 31 | 5.7 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 1.98 | 1.69 | 13 | 4.13 | 9.31 | 1.53 | 34 | 5.7 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
