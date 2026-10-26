# Walk-forward research 2026-10-26

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-29 21:45 to 2026-10-26 21:15 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -7.11%
- combos: 324 in 36s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 11.96 | 1.79 | 25 | 7.16 | 7.9 | 1.69 | 22 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 16.9 | 3.71 | 16 | 3.94 | 0.57 | 1.06 | 15 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 16.9 | 3.71 | 16 | 3.94 | 2.82 | 1.39 | 12 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 13.67 | 2.74 | 21 | 3.43 | -3.11 | 0.6 | 13 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 12.54 | 2.42 | 23 | 3.43 | -5.18 | 0.47 | 17 | 5.22 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 15.86 | 2.3 | 32 | 4.45 | -6.81 | 0.56 | 33 | 7.14 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 13.5 | 2.51 | 20 | 4.04 | 1.34 | 1.16 | 14 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 13.5 | 2.51 | 20 | 4.04 | 3.6 | 1.55 | 11 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=30d | 11.95 | 2.11 | 29 | 4.4 | -2.74 | 0.76 | 27 | 4.62 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 10.36 | 1.99 | 25 | 4.04 | -2.38 | 0.67 | 12 | 4.02 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=20 regime=30d | 12.37 | 2.8 | 17 | 4.9 | -1.39 | 0.85 | 15 | 4.82 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
