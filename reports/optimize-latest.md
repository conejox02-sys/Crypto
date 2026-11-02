# Walk-forward research 2026-11-02

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-06 13:30 to 2026-11-02 13:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -7.34%
- combos: 324 in 23s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 10.58 | 1.64 | 26 | 7.16 | 5.45 | 1.52 | 21 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 17.8 | 4.25 | 14 | 3.94 | 2.82 | 1.39 | 12 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 14.54 | 3.05 | 19 | 3.23 | -3.11 | 0.6 | 13 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 16.39 | 3.38 | 15 | 3.94 | 1.79 | 1.22 | 14 | 4.82 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 regime=30d | 12.04 | 2.28 | 22 | 3.33 | -4.03 | 0.54 | 16 | 5.22 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 13.5 | 2.51 | 20 | 4.04 | 3.6 | 1.55 | 11 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 14.04 | 2.0 | 34 | 4.45 | -5.03 | 0.63 | 30 | 7.14 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=30d | 13.23 | 3.15 | 15 | 4.21 | 0.78 | 1.11 | 12 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 12.14 | 2.18 | 21 | 4.04 | 2.56 | 1.35 | 13 | 4.82 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=20 regime=30d | 11.88 | 2.58 | 16 | 4.21 | -0.2 | 0.98 | 14 | 4.82 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 15.65 | 3.07 | 14 | 5.94 | 3.08 | 1.42 | 10 | 5.36 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
