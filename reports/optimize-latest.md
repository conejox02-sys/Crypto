# Walk-forward research 2026-09-27

- data: file:data/sol-15m-365d.json, 35039 x 15m bars, 2025-09-27 09:45 to 2026-09-27 09:15 UTC
- train: first 23359 bars; test (out of sample): last 11680 bars
- buy & hold over test: +50.63%
- combos: 324 in 45s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | -9.93 | 0.21 | 26 | 12.16 | 23.65 | 1.94 | 42 | 7.16 |
| pullback+breakout stop=2.0 tgt=8.0 minatr=0.4 donch=20 regime=30d | -4.0 | 0.8 | 38 | 10.57 | 1.46 | 1.04 | 61 | 9.41 |
| pullback+breakout stop=1.0 tgt=8.0 minatr=0.4 donch=20 regime=30d | -5.23 | 0.7 | 47 | 12.64 | -5.34 | 0.83 | 73 | 13.31 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | -3.83 | 0.73 | 30 | 8.79 | 11.24 | 1.56 | 43 | 5.7 |
| breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=20d | -3.6 | 0.68 | 37 | 8.15 | 11.08 | 1.55 | 45 | 6.02 |
| pullback+breakout stop=1.0 tgt=10.0 minatr=0.4 donch=30 regime=30d | -5.56 | 0.59 | 42 | 12.07 | 6.46 | 1.23 | 64 | 8.73 |
| breakout stop=1.0 tgt=8.0 minatr=0.4 donch=20 regime=20d | -4.74 | 0.65 | 41 | 10.19 | -1.26 | 0.95 | 54 | 8.02 |
| breakout stop=1.5 tgt=10.0 minatr=0.3 donch=30 regime=20d | -4.77 | 0.76 | 47 | 10.2 | 2.92 | 1.1 | 56 | 9.24 |
| pullback+breakout stop=2.0 tgt=10.0 minatr=0.3 donch=30 regime=30d | -6.1 | 0.71 | 47 | 12.64 | -2.38 | 0.93 | 74 | 14.43 |
| pullback+breakout stop=2.0 tgt=5.0 minatr=0.4 donch=30 regime=30d | -3.75 | 0.84 | 44 | 7.77 | -3.12 | 0.92 | 65 | 11.01 |
| breakout stop=1.0 tgt=10.0 minatr=0.3 donch=30 regime=20d | -4.81 | 0.7 | 54 | 9.57 | 9.71 | 1.39 | 59 | 7.63 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
