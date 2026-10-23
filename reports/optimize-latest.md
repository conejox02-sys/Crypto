# Walk-forward research 2026-10-23

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-26 20:30 to 2026-10-23 20:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +8.03%
- combos: 324 in 29s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 3.81 | 1.27 | 21 | 6.3 | 16.36 | 2.23 | 26 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 10.37 | 2.67 | 14 | 3.94 | 6.52 | 1.67 | 17 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 10.37 | 2.67 | 14 | 3.94 | 8.9 | 2.16 | 14 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 7.12 | 1.91 | 18 | 3.43 | 2.81 | 1.34 | 16 | 5.21 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 7.16 | 1.8 | 18 | 4.04 | 7.33 | 1.82 | 16 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 7.16 | 1.8 | 18 | 4.04 | 9.73 | 2.41 | 13 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 6.05 | 1.69 | 20 | 3.43 | 0.62 | 1.06 | 20 | 7.23 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 7.55 | 1.66 | 27 | 4.45 | 0.39 | 1.02 | 38 | 8.83 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 7.76 | 1.89 | 19 | 4.96 | 2.23 | 1.14 | 35 | 8.29 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | 7.76 | 1.89 | 19 | 4.96 | 7.66 | 1.68 | 29 | 6.52 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=20 regime=30d | 7.34 | 2.07 | 15 | 4.9 | 3.23 | 1.34 | 17 | 4.82 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
