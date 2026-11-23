# Walk-forward research 2026-11-23

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-27 16:00 to 2026-11-23 15:30 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -34.85%
- combos: 324 in 29s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 25.07 | 2.06 | 41 | 7.16 | -3.44 | 0.0 | 7 | 4.81 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 25.2 | 3.61 | 24 | 3.94 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 23.47 | 3.19 | 25 | 3.94 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 22.46 | 2.86 | 27 | 3.94 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 20.77 | 2.59 | 28 | 3.94 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 24.66 | 3.41 | 22 | 5.94 | -5.36 | 0.0 | 5 | 5.36 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 16.33 | 2.45 | 26 | 4.21 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=30d | 17.96 | 2.76 | 25 | 4.9 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=20d | 21.36 | 2.72 | 23 | 5.94 | -5.36 | 0.0 | 5 | 5.36 |
| breakout stop=1.5 tgt=8.0 minatr=0.5 donch=30 regime=30d | 20.93 | 2.69 | 24 | 5.94 | -5.36 | 0.0 | 5 | 5.36 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 25.07 | 2.06 | 41 | 7.16 | -3.44 | 0.0 | 7 | 4.81 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
