# Walk-forward research 2026-10-07

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-10 11:45 to 2026-10-07 11:15 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +55.97%
- combos: 324 in 37s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 2.28 | 1.38 | 10 | 4.94 | 17.02 | 1.77 | 38 | 7.16 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 1.79 | 1.32 | 13 | 4.43 | 6.04 | 1.25 | 53 | 8.83 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=20d | 1.61 | 1.2 | 17 | 6.55 | 9.98 | 1.62 | 38 | 6.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=20d | 0.91 | 1.11 | 18 | 6.55 | 4.43 | 1.21 | 44 | 8.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.3 donch=30 regime=20d | 0.25 | 1.03 | 24 | 6.55 | 9.43 | 1.47 | 50 | 7.63 |
| breakout stop=1.5 tgt=5.0 minatr=0.4 donch=20 regime=30d | 0.06 | 1.01 | 13 | 4.94 | 15.96 | 1.55 | 50 | 6.89 |
| breakout stop=1.0 tgt=10.0 minatr=0.3 donch=30 regime=30d | -0.81 | 0.88 | 16 | 7.77 | 12.4 | 1.59 | 53 | 8.38 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | -0.85 | 0.85 | 15 | 6.91 | 3.51 | 1.14 | 59 | 8.73 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=20d | -1.09 | 0.91 | 17 | 8.42 | 14.62 | 1.7 | 36 | 7.16 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | -1.09 | 0.82 | 16 | 6.91 | -1.71 | 0.94 | 65 | 11.21 |
| breakout stop=1.0 tgt=10.0 minatr=0.3 donch=20 regime=20d | -1.15 | 0.89 | 29 | 6.84 | 2.65 | 1.1 | 59 | 10.1 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
