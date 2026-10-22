# Walk-forward research 2026-10-22

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-25 10:15 to 2026-10-22 09:45 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +11.26%
- combos: 324 in 38s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 8.19 | 1.83 | 17 | 4.97 | 11.65 | 1.69 | 30 | 5.66 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 9.09 | 2.55 | 15 | 3.43 | 0.95 | 1.1 | 19 | 5.21 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 8.0 | 2.17 | 17 | 3.43 | -1.2 | 0.9 | 23 | 7.23 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 10.27 | 2.18 | 23 | 4.45 | -2.09 | 0.89 | 42 | 8.83 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 9.13 | 2.32 | 15 | 4.04 | 5.39 | 1.51 | 19 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 9.13 | 2.32 | 15 | 4.04 | 7.75 | 1.9 | 16 | 4.02 |
| breakout stop=1.5 tgt=5.0 minatr=0.5 donch=30 regime=30d | 7.4 | 2.04 | 15 | 3.46 | 4.96 | 1.42 | 18 | 5.36 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 10.48 | 2.76 | 15 | 4.96 | -0.3 | 0.98 | 39 | 8.29 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | 10.48 | 2.76 | 15 | 4.96 | 5.01 | 1.37 | 33 | 6.52 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=20 regime=30d | 9.32 | 2.91 | 12 | 4.9 | 1.37 | 1.12 | 20 | 4.82 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=30d | 9.32 | 2.91 | 12 | 4.9 | 3.6 | 1.39 | 17 | 4.02 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
