# Walk-forward research 2026-10-19

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-22 21:30 to 2026-10-19 21:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +19.87%
- combos: 324 in 36s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 6.79 | 2.09 | 12 | 4.97 | 13.11 | 1.64 | 35 | 7.16 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=20 regime=30d | 6.79 | 2.09 | 12 | 4.97 | 8.33 | 1.34 | 39 | 7.85 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 6.79 | 2.09 | 12 | 4.97 | 13.11 | 1.64 | 35 | 7.16 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 5.8 | 1.91 | 17 | 4.45 | 2.04 | 1.09 | 48 | 8.83 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 5.55 | 2.54 | 12 | 4.73 | 4.14 | 1.23 | 34 | 5.7 |
| breakout stop=1.5 tgt=5.0 minatr=0.4 donch=20 regime=30d | 4.69 | 1.63 | 17 | 4.97 | 11.86 | 1.44 | 45 | 6.89 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=20 regime=30d | 3.93 | 1.75 | 12 | 4.4 | -1.55 | 0.92 | 45 | 8.29 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=30 regime=30d | 3.93 | 1.75 | 12 | 4.4 | 3.65 | 1.23 | 39 | 6.52 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 2.94 | 1.56 | 12 | 3.43 | 3.66 | 1.26 | 28 | 7.23 |
| pullback+breakout stop=1.5 tgt=10.0 minatr=0.5 donch=20 regime=30d | 4.5 | 1.98 | 12 | 5.68 | 0.84 | 1.04 | 28 | 8.55 |
| breakout stop=2.0 tgt=8.0 minatr=0.4 donch=20 regime=30d | 4.3 | 1.6 | 12 | 5.58 | 2.89 | 1.11 | 39 | 9.71 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
