# Walk-forward research 2026-10-03

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-06 20:00 to 2026-10-03 19:30 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +61.34%
- combos: 324 in 37s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 2.25 | 1.37 | 11 | 4.94 | 17.02 | 1.77 | 38 | 7.16 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 2.23 | 1.85 | 12 | 4.13 | 10.09 | 1.59 | 33 | 5.7 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 1.98 | 1.69 | 13 | 4.13 | 7.69 | 1.4 | 36 | 5.7 |
| pullback+breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 1.34 | 1.38 | 13 | 3.62 | 2.22 | 1.12 | 38 | 6.9 |
| pullback+breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 1.09 | 1.29 | 14 | 3.62 | 0.04 | 1.0 | 42 | 8.88 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=20 regime=30d | 1.31 | 1.19 | 12 | 4.94 | 12.07 | 1.46 | 42 | 7.85 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=20d | 1.61 | 1.2 | 17 | 6.55 | 9.98 | 1.62 | 38 | 6.02 |
| pullback+breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=30d | 1.24 | 1.48 | 12 | 5.09 | 4.92 | 1.28 | 34 | 5.7 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 1.06 | 1.17 | 15 | 4.43 | 6.04 | 1.25 | 53 | 8.83 |
| pullback+breakout stop=1.0 tgt=8.0 minatr=0.5 donch=20 regime=30d | 0.99 | 1.35 | 13 | 5.09 | 2.67 | 1.14 | 37 | 5.7 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=20d | 0.91 | 1.11 | 18 | 6.55 | 4.43 | 1.21 | 44 | 8.02 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
