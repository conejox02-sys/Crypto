# Walk-forward research 2026-09-29

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-02 11:30 to 2026-09-29 11:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +62.09%
- combos: 324 in 32s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 4.45 | 1.63 | 13 | 4.94 | 18.32 | 1.88 | 34 | 7.16 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | 5.45 | 2.25 | 12 | 4.93 | 15.16 | 2.0 | 35 | 6.52 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 4.72 | 1.94 | 13 | 4.93 | 9.34 | 1.46 | 41 | 8.29 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 4.45 | 1.63 | 13 | 4.94 | 18.32 | 1.88 | 34 | 7.16 |
| breakout stop=1.5 tgt=10.0 minatr=0.4 donch=30 regime=30d | 4.0 | 1.7 | 12 | 5.19 | 10.38 | 1.54 | 33 | 7.32 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=20 regime=30d | 3.5 | 1.44 | 14 | 4.94 | 13.32 | 1.53 | 38 | 7.16 |
| breakout stop=1.5 tgt=10.0 minatr=0.4 donch=20 regime=30d | 3.05 | 1.46 | 13 | 5.19 | 4.46 | 1.18 | 38 | 10.3 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=30 regime=30d | 2.52 | 1.48 | 13 | 4.37 | 9.13 | 1.59 | 37 | 6.52 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 2.2 | 1.83 | 13 | 4.13 | 11.75 | 1.76 | 31 | 5.7 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 2.21 | 1.32 | 18 | 4.43 | 7.65 | 1.34 | 48 | 7.44 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 1.95 | 1.67 | 14 | 4.13 | 9.31 | 1.53 | 34 | 5.7 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
