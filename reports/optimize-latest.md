# Walk-forward research 2026-11-24

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-28 16:00 to 2026-11-24 15:30 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -42.72%
- combos: 324 in 35s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 23.65 | 1.94 | 42 | 7.16 | -2.31 | 0.0 | 5 | 2.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 23.17 | 2.98 | 25 | 3.94 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 20.47 | 2.46 | 28 | 3.94 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 20.36 | 2.51 | 28 | 4.15 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 17.73 | 2.12 | 31 | 4.15 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 21.89 | 2.68 | 23 | 5.94 | -3.18 | 0.0 | 3 | 3.18 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 23.65 | 1.94 | 42 | 7.16 | -2.31 | 0.0 | 5 | 2.82 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=30d | 16.04 | 2.33 | 26 | 4.9 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 13.4 | 1.96 | 29 | 4.21 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.5 tgt=8.0 minatr=0.5 donch=30 regime=30d | 18.24 | 2.21 | 25 | 5.94 | -3.18 | 0.0 | 3 | 3.18 |
| breakout stop=1.5 tgt=5.0 minatr=0.5 donch=30 regime=30d | 16.42 | 2.02 | 30 | 5.46 | -3.18 | 0.0 | 3 | 3.18 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
