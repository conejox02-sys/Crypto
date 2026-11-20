# Walk-forward research 2026-11-20

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-24 14:00 to 2026-11-20 13:30 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -40.09%
- combos: 324 in 22s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 25.88 | 2.21 | 38 | 7.16 | -5.16 | 0.0 | 9 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 22.5 | 3.33 | 23 | 3.94 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 22.11 | 3.28 | 24 | 3.94 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 21.74 | 2.98 | 24 | 3.94 | -4.82 | 0.0 | 7 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 21.35 | 2.93 | 25 | 3.94 | -4.82 | 0.0 | 7 | 4.82 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 16.23 | 2.58 | 25 | 4.21 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=20 regime=20d | 16.04 | 2.39 | 26 | 4.21 | -4.82 | 0.0 | 7 | 4.82 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 21.97 | 3.15 | 21 | 5.94 | -5.36 | 0.0 | 5 | 5.36 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 25.88 | 2.21 | 38 | 7.16 | -5.16 | 0.0 | 9 | 5.66 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 14.38 | 2.17 | 30 | 4.01 | -4.02 | 0.0 | 5 | 4.02 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=20 regime=30d | 21.26 | 2.85 | 22 | 5.94 | -7.29 | 0.0 | 7 | 7.55 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
