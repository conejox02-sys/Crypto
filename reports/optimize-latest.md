# Walk-forward research 2026-10-02

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-04-05 11:15 to 2026-10-02 10:45 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: +68.24%
- combos: 324 in 29s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 5.34 | 1.85 | 12 | 4.94 | 17.02 | 1.77 | 38 | 7.16 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=20 regime=30d | 5.39 | 2.22 | 12 | 4.93 | 7.7 | 1.35 | 46 | 8.29 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 5.34 | 1.85 | 12 | 4.94 | 17.02 | 1.77 | 38 | 7.16 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=20 regime=30d | 4.37 | 1.61 | 13 | 4.94 | 12.07 | 1.46 | 42 | 7.85 |
| breakout stop=1.5 tgt=10.0 minatr=0.4 donch=20 regime=30d | 3.92 | 1.67 | 12 | 5.19 | 3.3 | 1.13 | 42 | 10.3 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=30 regime=30d | 3.17 | 1.69 | 12 | 4.37 | 7.5 | 1.44 | 42 | 6.52 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 regime=30d | 2.86 | 1.45 | 17 | 4.43 | 6.04 | 1.25 | 53 | 8.83 |
| breakout stop=2.0 tgt=8.0 minatr=0.4 donch=30 regime=30d | 3.57 | 1.5 | 12 | 5.56 | 10.63 | 1.45 | 38 | 7.82 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=20 regime=30d | 2.47 | 1.47 | 13 | 4.37 | 2.1 | 1.1 | 48 | 8.29 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 2.23 | 1.85 | 12 | 4.13 | 10.09 | 1.59 | 33 | 5.7 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 1.98 | 1.69 | 13 | 4.13 | 7.69 | 1.4 | 36 | 5.7 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
