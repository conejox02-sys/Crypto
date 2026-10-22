# Walk-forward research 2026-10-22

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-25 20:45 to 2026-10-22 20:15 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +8.70%
- combos: 324 in 30s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 7.13 | 1.65 | 18 | 4.97 | 12.76 | 1.8 | 29 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 12.37 | 3.94 | 12 | 3.94 | 4.63 | 1.41 | 19 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 12.37 | 3.94 | 12 | 3.94 | 6.97 | 1.75 | 16 | 4.02 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=20 regime=30d | 10.55 | 2.74 | 12 | 3.71 | 3.17 | 1.24 | 17 | 7.55 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 10.55 | 2.74 | 12 | 3.71 | 6.75 | 1.69 | 14 | 5.36 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 9.06 | 2.54 | 16 | 3.43 | 0.98 | 1.1 | 18 | 5.21 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 7.97 | 2.16 | 18 | 3.43 | -1.17 | 0.9 | 22 | 7.23 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 10.24 | 2.17 | 24 | 4.45 | -2.06 | 0.89 | 41 | 8.83 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 9.1 | 2.31 | 16 | 4.04 | 5.43 | 1.51 | 18 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 9.1 | 2.31 | 16 | 4.04 | 7.78 | 1.91 | 15 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 10.45 | 2.75 | 16 | 4.96 | -0.27 | 0.99 | 38 | 8.29 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
