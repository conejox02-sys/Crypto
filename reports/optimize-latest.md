# Walk-forward research 2026-11-05

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-09 22:45 to 2026-11-05 22:15 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -15.02%
- combos: 324 in 28s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 8.54 | 1.52 | 26 | 7.16 | 6.4 | 1.67 | 19 | 5.66 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 10.44 | 2.33 | 20 | 3.23 | -2.3 | 0.68 | 12 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 12.55 | 2.27 | 21 | 4.04 | 4.47 | 1.78 | 10 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 12.28 | 1.82 | 36 | 4.0 | -5.86 | 0.52 | 27 | 7.14 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 11.2 | 2.0 | 22 | 4.04 | 3.43 | 1.52 | 12 | 4.82 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=30d | 10.58 | 1.93 | 31 | 3.93 | -3.6 | 0.64 | 23 | 4.62 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 10.35 | 2.69 | 15 | 4.21 | 3.68 | 1.57 | 11 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 9.44 | 1.83 | 26 | 4.04 | -1.55 | 0.76 | 11 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=20d | 10.51 | 1.55 | 43 | 4.69 | -6.2 | 0.43 | 24 | 7.14 |
| breakout stop=1.0 tgt=5.0 minatr=0.3 donch=30 regime=30d | 10.94 | 1.78 | 41 | 5.15 | -6.55 | 0.49 | 32 | 6.55 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 8.19 | 1.78 | 22 | 4.21 | 2.4 | 1.43 | 10 | 4.02 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
