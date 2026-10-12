# Walk-forward research 2026-10-12

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-15 13:15 to 2026-10-12 12:45 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +44.73%
- combos: 324 in 38s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 3.23 | 1.63 | 9 | 4.94 | 17.02 | 1.77 | 38 | 7.16 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 1.82 | 1.33 | 12 | 4.43 | 6.04 | 1.25 | 53 | 8.83 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=20d | 2.25 | 1.31 | 16 | 6.55 | 9.98 | 1.62 | 38 | 6.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=20d | 1.55 | 1.19 | 17 | 6.55 | 4.43 | 1.21 | 44 | 8.02 |
| breakout stop=1.5 tgt=5.0 minatr=0.4 donch=20 regime=30d | 0.99 | 1.16 | 12 | 4.94 | 15.96 | 1.55 | 50 | 6.89 |
| breakout stop=1.0 tgt=10.0 minatr=0.3 donch=30 regime=20d | 0.31 | 1.03 | 22 | 6.55 | 9.43 | 1.47 | 50 | 7.63 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=20d | -0.25 | 0.98 | 16 | 8.42 | 14.62 | 1.7 | 36 | 7.16 |
| breakout stop=1.5 tgt=8.0 minatr=0.3 donch=30 regime=30d | -0.51 | 0.94 | 16 | 8.39 | 12.42 | 1.42 | 53 | 7.29 |
| breakout stop=1.5 tgt=10.0 minatr=0.4 donch=30 regime=20d | -0.69 | 0.93 | 15 | 8.42 | 6.08 | 1.31 | 35 | 7.16 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=30 regime=20d | -0.59 | 0.93 | 17 | 6.55 | 5.05 | 1.31 | 40 | 6.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.3 donch=30 regime=30d | -0.78 | 0.88 | 15 | 7.77 | 12.4 | 1.59 | 53 | 8.38 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
