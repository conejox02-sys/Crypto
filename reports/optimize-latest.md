# Walk-forward research 2026-11-06

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-10 22:15 to 2026-11-06 21:45 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -13.00%
- combos: 324 in 38s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 6.22 | 1.34 | 27 | 7.16 | 7.44 | 1.86 | 18 | 5.66 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 10.44 | 2.33 | 20 | 3.23 | -2.3 | 0.68 | 12 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 12.55 | 2.27 | 21 | 4.04 | 4.47 | 1.78 | 10 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 11.46 | 1.73 | 37 | 4.0 | -5.18 | 0.56 | 26 | 7.14 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 11.2 | 2.0 | 22 | 4.04 | 3.43 | 1.52 | 12 | 4.82 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=30d | 9.78 | 1.8 | 32 | 3.88 | -2.9 | 0.69 | 22 | 4.62 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 10.35 | 2.69 | 15 | 4.21 | 3.68 | 1.57 | 11 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 9.44 | 1.83 | 26 | 4.04 | -1.55 | 0.76 | 11 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=20d | 9.71 | 1.49 | 44 | 4.69 | -5.51 | 0.46 | 23 | 7.14 |
| breakout stop=1.0 tgt=5.0 minatr=0.3 donch=30 regime=30d | 10.14 | 1.69 | 42 | 5.0 | -5.87 | 0.52 | 31 | 6.29 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 8.19 | 1.78 | 22 | 4.21 | 2.4 | 1.43 | 10 | 4.02 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
