# Walk-forward research 2026-10-25

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-28 19:45 to 2026-10-25 19:15 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +5.28%
- combos: 324 in 38s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 2.86 | 1.19 | 23 | 7.15 | 17.43 | 2.39 | 24 | 5.66 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 10.53 | 2.35 | 19 | 3.43 | -0.36 | 0.96 | 15 | 5.21 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 9.42 | 2.07 | 21 | 3.43 | -2.48 | 0.75 | 19 | 7.23 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 10.34 | 2.66 | 15 | 3.94 | 6.55 | 1.68 | 16 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 10.34 | 2.66 | 15 | 3.94 | 8.93 | 2.17 | 13 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 10.24 | 1.84 | 29 | 4.45 | -2.06 | 0.87 | 36 | 8.83 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 7.31 | 1.7 | 23 | 4.04 | 0.4 | 1.05 | 14 | 4.49 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 7.12 | 1.8 | 19 | 4.04 | 7.37 | 1.82 | 15 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 7.12 | 1.8 | 19 | 4.04 | 9.77 | 2.42 | 12 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=20d | 6.24 | 1.55 | 25 | 4.04 | -1.74 | 0.81 | 18 | 6.52 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=20 regime=30d | 7.31 | 2.06 | 16 | 4.9 | 3.26 | 1.34 | 16 | 4.82 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
