# Walk-forward research 2026-11-24

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-28 03:30 to 2026-11-24 03:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -39.61%
- combos: 324 in 31s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 23.69 | 1.94 | 41 | 7.16 | -2.34 | 0.0 | 6 | 4.81 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 24.2 | 3.27 | 24 | 3.94 | -3.22 | 0.0 | 4 | 3.22 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 22.45 | 2.92 | 26 | 3.94 | -3.22 | 0.0 | 4 | 3.22 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 21.48 | 2.65 | 27 | 3.94 | -3.22 | 0.0 | 4 | 3.22 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 19.77 | 2.41 | 29 | 3.94 | -3.22 | 0.0 | 4 | 3.22 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 23.28 | 3.0 | 22 | 5.94 | -4.28 | 0.0 | 4 | 4.28 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 15.37 | 2.26 | 27 | 4.21 | -3.22 | 0.0 | 4 | 3.22 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=30d | 17.02 | 2.53 | 25 | 4.9 | -3.22 | 0.0 | 4 | 3.22 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=20d | 19.99 | 2.45 | 24 | 5.94 | -4.28 | 0.0 | 4 | 4.28 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 23.69 | 1.94 | 41 | 7.16 | -2.34 | 0.0 | 6 | 4.81 |
| breakout stop=1.5 tgt=8.0 minatr=0.5 donch=30 regime=30d | 19.59 | 2.42 | 24 | 5.94 | -4.28 | 0.0 | 4 | 4.28 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
