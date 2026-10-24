# Walk-forward research 2026-10-24

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-27 09:30 to 2026-10-24 09:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +1.51%
- combos: 324 in 22s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 4.97 | 1.35 | 22 | 6.3 | 16.4 | 2.24 | 25 | 5.66 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 10.53 | 2.35 | 19 | 3.43 | -0.36 | 0.96 | 15 | 5.21 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 11.62 | 2.87 | 15 | 3.94 | 6.55 | 1.68 | 16 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 11.62 | 2.87 | 15 | 3.94 | 8.93 | 2.17 | 13 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 9.42 | 2.07 | 21 | 3.43 | -2.48 | 0.75 | 19 | 7.23 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 10.98 | 1.96 | 28 | 4.45 | -2.71 | 0.84 | 37 | 8.83 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 8.37 | 1.94 | 19 | 4.04 | 7.37 | 1.82 | 15 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 8.37 | 1.94 | 19 | 4.04 | 9.77 | 2.42 | 12 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 7.31 | 1.7 | 23 | 4.04 | 0.4 | 1.05 | 14 | 4.49 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 8.97 | 2.04 | 20 | 4.96 | 2.26 | 1.14 | 34 | 8.29 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | 8.97 | 2.04 | 20 | 4.96 | 7.7 | 1.68 | 28 | 6.52 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
