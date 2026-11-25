# Walk-forward research 2026-11-25

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-29 15:30 to 2026-11-25 15:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -44.88%
- combos: 324 in 20s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 18.22 | 1.76 | 40 | 7.16 | -2.31 | 0.0 | 5 | 2.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 20.36 | 2.51 | 28 | 4.15 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 17.73 | 2.12 | 31 | 4.15 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 16.42 | 2.49 | 23 | 4.9 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 13.4 | 1.96 | 29 | 4.21 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=20d | 17.2 | 2.06 | 26 | 5.94 | -3.18 | 0.0 | 3 | 3.18 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 15.55 | 1.9 | 36 | 5.7 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=20 regime=20d | 10.96 | 1.68 | 32 | 4.21 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 12.73 | 1.9 | 28 | 4.9 | -2.41 | 0.0 | 3 | 2.41 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 15.21 | 2.24 | 21 | 5.94 | -3.18 | 0.0 | 3 | 3.18 |
| breakout stop=1.5 tgt=8.0 minatr=0.5 donch=30 regime=20d | 15.13 | 1.9 | 27 | 5.94 | -3.18 | 0.0 | 3 | 3.18 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
