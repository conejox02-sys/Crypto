# Walk-forward research 2026-11-04

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-08 22:45 to 2026-11-04 22:15 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -7.53%
- combos: 324 in 33s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 14.59 | 1.91 | 25 | 7.16 | 5.48 | 1.53 | 20 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 16.81 | 3.6 | 15 | 3.94 | 3.68 | 1.57 | 11 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 17.06 | 2.24 | 34 | 4.0 | -7.14 | 0.47 | 29 | 7.14 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 13.59 | 2.68 | 20 | 3.23 | -2.3 | 0.68 | 12 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 15.42 | 2.96 | 16 | 3.94 | 2.64 | 1.36 | 13 | 4.82 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=30d | 14.48 | 2.32 | 30 | 3.88 | -4.24 | 0.6 | 24 | 4.62 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 12.55 | 2.27 | 21 | 4.04 | 4.47 | 1.78 | 10 | 4.02 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=30d | 12.29 | 2.73 | 16 | 4.21 | 1.63 | 1.26 | 11 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 11.2 | 2.0 | 22 | 4.04 | 3.43 | 1.52 | 12 | 4.82 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 11.11 | 2.07 | 23 | 4.14 | -3.22 | 0.59 | 15 | 5.22 |
| breakout stop=1.0 tgt=5.0 minatr=0.3 donch=30 regime=30d | 13.3 | 1.98 | 39 | 5.0 | -5.9 | 0.56 | 34 | 7.16 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
