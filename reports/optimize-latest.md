# Walk-forward research 2026-09-26

- data: file:data/sol-15m.json, 8639 x 15m bars, 2026-06-28 21:45 to 2026-09-26 21:15 UTC
- train: first 5759 bars; test (out of sample): last 2880 bars
- buy & hold over test: +12.28%
- combos: 224 in 14s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | -21.15 | 0.57 | 138 | 28.19 | -17.66 | 0.44 | 64 | 18.16 |
| pullback stop=2.0 tgt=3.5 rsi=42 trail=2.0 minatr=0.2 | -1.82 | 0.86 | 32 | 6.26 | -4.51 | 0.4 | 15 | 7.28 |
| pullback stop=2.0 tgt=3.5 rsi=42 trail=0.0 minatr=0.2 | -1.87 | 0.85 | 32 | 6.31 | -4.51 | 0.4 | 15 | 7.28 |
| breakout stop=1.0 tgt=3.5 rsi=35 trail=2.0 minatr=0.2 | -8.62 | 0.74 | 96 | 21.74 | -9.81 | 0.47 | 48 | 9.81 |
| pullback+breakout stop=1.0 tgt=3.5 rsi=35 trail=2.0 minatr=0.2 | -9.14 | 0.73 | 97 | 22.19 | -11.43 | 0.43 | 51 | 11.44 |
| breakout stop=1.0 tgt=3.5 rsi=35 trail=2.0 minatr=0.1 | -9.15 | 0.73 | 101 | 22.2 | -9.95 | 0.47 | 49 | 9.95 |
| pullback+breakout stop=1.0 tgt=3.5 rsi=35 trail=2.0 minatr=0.1 | -9.67 | 0.72 | 102 | 22.64 | -11.57 | 0.43 | 52 | 11.57 |
| pullback stop=2.0 tgt=3.5 rsi=42 trail=2.0 minatr=0.1 | -3.37 | 0.77 | 39 | 7.75 | -4.51 | 0.4 | 15 | 7.28 |
| breakout stop=1.0 tgt=3.5 rsi=35 trail=0.0 minatr=0.2 | -9.48 | 0.72 | 96 | 21.77 | -10.06 | 0.46 | 48 | 10.06 |
| pullback stop=2.0 tgt=3.5 rsi=42 trail=0.0 minatr=0.1 | -3.42 | 0.77 | 39 | 7.79 | -4.51 | 0.4 | 15 | 7.28 |
| breakout stop=1.5 tgt=3.5 rsi=35 trail=2.0 minatr=0.2 | -8.32 | 0.75 | 87 | 18.74 | -6.46 | 0.73 | 47 | 10.15 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
