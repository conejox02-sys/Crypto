# Walk-forward research 2026-11-07

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-11 21:00 to 2026-11-07 20:30 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -13.31%
- combos: 324 in 35s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 5.3 | 1.27 | 28 | 7.16 | 8.39 | 2.06 | 17 | 5.66 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 10.44 | 2.33 | 20 | 3.23 | -2.3 | 0.68 | 12 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 12.55 | 2.27 | 21 | 4.04 | 4.47 | 1.78 | 10 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 11.2 | 2.0 | 22 | 4.04 | 3.43 | 1.52 | 12 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 10.35 | 2.69 | 15 | 4.21 | 3.68 | 1.57 | 11 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 10.73 | 1.65 | 38 | 4.48 | -4.55 | 0.59 | 25 | 7.14 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 9.44 | 1.83 | 26 | 4.04 | -1.55 | 0.76 | 11 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=30d | 9.06 | 1.7 | 33 | 3.88 | -2.26 | 0.75 | 21 | 4.62 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 8.19 | 1.78 | 22 | 4.21 | 2.4 | 1.43 | 10 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 8.03 | 1.79 | 23 | 4.14 | -3.22 | 0.59 | 15 | 5.22 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=20d | 8.98 | 1.44 | 45 | 4.69 | -4.89 | 0.49 | 22 | 7.14 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
