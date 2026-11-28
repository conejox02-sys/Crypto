# Walk-forward research 2026-11-28

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-06-01 00:30 to 2026-11-28 00:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -39.58%
- combos: 324 in 36s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 15.03 | 1.65 | 39 | 7.16 | -1.11 | 0.0 | 4 | 1.85 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 20.29 | 2.46 | 28 | 3.94 | -1.48 | 0.0 | 2 | 1.48 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 17.66 | 2.09 | 31 | 3.94 | -1.48 | 0.0 | 2 | 1.48 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 14.5 | 2.14 | 24 | 3.94 | -1.48 | 0.0 | 2 | 1.48 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 13.34 | 1.94 | 29 | 4.21 | -1.48 | 0.0 | 2 | 1.48 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 11.99 | 1.8 | 27 | 3.94 | -1.48 | 0.0 | 2 | 1.48 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=20d | 17.2 | 2.04 | 26 | 5.94 | -1.99 | 0.0 | 2 | 1.99 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=20 regime=20d | 10.9 | 1.66 | 32 | 4.21 | -1.48 | 0.0 | 2 | 1.48 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 10.22 | 1.63 | 34 | 4.01 | -1.48 | 0.0 | 2 | 1.48 |
| breakout stop=1.5 tgt=8.0 minatr=0.5 donch=30 regime=20d | 15.13 | 1.88 | 27 | 5.94 | -1.99 | 0.0 | 2 | 1.99 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 13.81 | 2.01 | 22 | 5.94 | -1.99 | 0.0 | 2 | 1.99 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
