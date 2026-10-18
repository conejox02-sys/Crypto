# Walk-forward research 2026-10-18

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-21 19:30 to 2026-10-18 19:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +24.36%
- combos: 324 in 37s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 3.2 | 1.62 | 10 | 4.97 | 17.05 | 1.77 | 37 | 7.16 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 1.79 | 1.32 | 13 | 4.45 | 6.07 | 1.25 | 52 | 8.83 |
| breakout stop=1.5 tgt=8.0 minatr=0.3 donch=30 regime=30d | 1.95 | 1.22 | 18 | 8.39 | 9.7 | 1.34 | 51 | 7.29 |
| breakout stop=1.0 tgt=10.0 minatr=0.3 donch=30 regime=30d | 1.56 | 1.21 | 17 | 7.77 | 9.8 | 1.49 | 51 | 8.38 |
| breakout stop=1.5 tgt=5.0 minatr=0.4 donch=20 regime=30d | 0.96 | 1.15 | 13 | 4.97 | 15.99 | 1.55 | 49 | 6.89 |
| breakout stop=1.5 tgt=10.0 minatr=0.3 donch=30 regime=30d | 1.39 | 1.18 | 17 | 8.64 | 4.18 | 1.17 | 48 | 10.19 |
| pullback+breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 0.37 | 1.08 | 12 | 4.22 | 0.84 | 1.04 | 41 | 8.88 |
| breakout stop=2.0 tgt=8.0 minatr=0.3 donch=30 regime=30d | 0.43 | 1.04 | 17 | 9.03 | 6.19 | 1.22 | 48 | 9.29 |
| breakout stop=1.5 tgt=8.0 minatr=0.3 donch=20 regime=30d | 0.38 | 1.04 | 24 | 10.09 | 6.73 | 1.2 | 56 | 8.88 |
| breakout stop=1.0 tgt=10.0 minatr=0.3 donch=20 regime=30d | 0.29 | 1.03 | 24 | 8.92 | 3.56 | 1.14 | 59 | 10.61 |
| breakout stop=1.5 tgt=10.0 minatr=0.3 donch=20 regime=30d | -0.18 | 0.98 | 23 | 10.34 | 0.76 | 1.03 | 54 | 13.7 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
