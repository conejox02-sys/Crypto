# Walk-forward research 2026-10-05

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-08 12:15 to 2026-10-05 11:45 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +64.87%
- combos: 324 in 29s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 2.25 | 1.37 | 11 | 4.94 | 17.02 | 1.77 | 38 | 7.16 |
| pullback+breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 1.15 | 1.31 | 12 | 3.62 | 0.04 | 1.0 | 42 | 8.88 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=20 regime=30d | 1.31 | 1.19 | 12 | 4.94 | 12.07 | 1.46 | 42 | 7.85 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=20d | 1.61 | 1.2 | 17 | 6.55 | 9.98 | 1.62 | 38 | 6.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 1.06 | 1.17 | 15 | 4.43 | 6.04 | 1.25 | 53 | 8.83 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=20d | 0.91 | 1.11 | 18 | 6.55 | 4.43 | 1.21 | 44 | 8.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.3 donch=30 regime=20d | 0.25 | 1.03 | 24 | 6.55 | 9.43 | 1.47 | 50 | 7.63 |
| breakout stop=1.0 tgt=10.0 minatr=0.3 donch=30 regime=30d | -0.84 | 0.87 | 17 | 7.77 | 12.4 | 1.59 | 53 | 8.38 |
| breakout stop=2.0 tgt=8.0 minatr=0.4 donch=20 regime=30d | -0.61 | 0.92 | 12 | 5.56 | 5.49 | 1.19 | 42 | 9.71 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=20 regime=30d | -0.54 | 0.89 | 12 | 4.37 | 2.1 | 1.1 | 48 | 8.29 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | -0.88 | 0.85 | 16 | 6.91 | 3.51 | 1.14 | 59 | 8.73 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
