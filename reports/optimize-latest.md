# Walk-forward research 2026-11-27

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-31 01:00 to 2026-11-27 00:30 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -41.35%
- combos: 324 in 31s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 15.46 | 1.69 | 39 | 7.16 | -2.31 | 0.0 | 5 | 2.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 21.44 | 2.68 | 27 | 3.94 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 18.78 | 2.25 | 30 | 3.94 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 15.58 | 2.34 | 23 | 3.94 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 14.41 | 2.1 | 28 | 4.21 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 13.06 | 1.94 | 26 | 3.94 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=20d | 18.64 | 2.23 | 25 | 5.94 | -3.18 | 0.0 | 3 | 3.18 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=20 regime=20d | 11.95 | 1.78 | 31 | 4.21 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 11.27 | 1.75 | 33 | 4.01 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.5 tgt=8.0 minatr=0.5 donch=30 regime=20d | 16.54 | 2.05 | 26 | 5.94 | -3.18 | 0.0 | 3 | 3.18 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=30d | 10.16 | 1.83 | 24 | 3.94 | -2.41 | 0.0 | 3 | 2.41 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
