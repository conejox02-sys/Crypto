# Walk-forward research 2026-11-22

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-26 13:30 to 2026-11-22 13:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -39.84%
- combos: 324 in 29s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 26.28 | 2.17 | 40 | 7.16 | -4.36 | 0.0 | 8 | 4.87 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 25.2 | 3.61 | 24 | 3.94 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 24.83 | 3.56 | 24 | 3.94 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 22.46 | 2.86 | 27 | 3.94 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 22.1 | 2.83 | 27 | 3.94 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 17.61 | 2.72 | 25 | 4.21 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 24.66 | 3.41 | 22 | 5.94 | -5.36 | 0.0 | 5 | 5.36 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=20d | 22.78 | 3.0 | 23 | 5.94 | -5.36 | 0.0 | 5 | 5.36 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 26.28 | 2.17 | 40 | 7.16 | -4.36 | 0.0 | 8 | 4.87 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=30d | 17.96 | 2.76 | 25 | 4.9 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 14.38 | 2.17 | 30 | 4.01 | -4.02 | 0.0 | 5 | 4.02 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
