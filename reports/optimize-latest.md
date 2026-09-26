# Walk-forward research 2026-09-26

- data: file:data/sol-15m.json, 8639 x 15m bars, 2026-06-28 21:45 to 2026-09-26 21:15 UTC
- train: first 5759 bars; test (out of sample): last 2880 bars
- buy & hold over test: +12.28%
- combos: 324 in 12s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 11.92 | 1.79 | 26 | 7.16 | 10.45 | 2.17 | 17 | 3.05 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 vol=1.5 | 16.03 | 3.3 | 17 | 4.66 | 3.06 | 1.46 | 12 | 3.8 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 vol=1.5 | 16.03 | 3.3 | 17 | 4.66 | 5.36 | 2.15 | 9 | 2.63 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 vol=1.5 | 12.83 | 2.49 | 22 | 4.15 | -0.72 | 0.87 | 10 | 2.63 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=20 vol=1.5 | 11.7 | 2.23 | 24 | 4.15 | -2.83 | 0.62 | 14 | 3.8 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 vol=1.2 | 16.38 | 2.86 | 20 | 6.0 | 5.35 | 2.09 | 9 | 4.18 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=20 vol=1.2 | 16.03 | 2.75 | 21 | 6.29 | 0.6 | 1.06 | 13 | 5.65 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=20 vol=1.5 | 14.27 | 2.06 | 34 | 5.77 | -4.49 | 0.66 | 27 | 4.83 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=20 vol=1.5 | 14.45 | 2.68 | 17 | 5.94 | 2.9 | 1.41 | 10 | 4.51 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 vol=1.5 | 14.45 | 2.68 | 17 | 5.94 | 6.47 | 2.66 | 7 | 4.18 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=20 vol=2.0 | 10.27 | 2.67 | 14 | 4.65 | 3.85 | 1.64 | 9 | 3.68 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
