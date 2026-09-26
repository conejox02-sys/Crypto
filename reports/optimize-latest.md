# Walk-forward research 2026-09-26

- data: file:data/sol-15m.json, 5759 x 15m bars, 2026-07-28 21:45 to 2026-09-26 21:15 UTC
- train: first 3839 bars; test (out of sample): last 1920 bars
- buy & hold over test: +14.57%
- combos: 288 in 6s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | -18.36 | 0.48 | 95 | 18.71 | -10.08 | 0.55 | 43 | 11.11 |
| breakout stop=1.0 tgt=3.5 rsi=35 trail=2.0 minatr=0.2 | -4.94 | 0.8 | 69 | 11.04 | -7.02 | 0.45 | 32 | 7.02 |
| breakout stop=1.0 tgt=3.5 rsi=42 trail=2.0 minatr=0.2 | -4.94 | 0.8 | 69 | 11.04 | -7.02 | 0.45 | 32 | 7.02 |
| breakout stop=1.0 tgt=3.5 rsi=50 trail=2.0 minatr=0.2 | -4.94 | 0.8 | 69 | 11.04 | -7.02 | 0.45 | 32 | 7.02 |
| breakout stop=1.0 tgt=3.5 rsi=35 trail=2.0 minatr=0.1 | -5.09 | 0.8 | 72 | 11.17 | -7.17 | 0.44 | 33 | 7.16 |
| breakout stop=1.0 tgt=3.5 rsi=42 trail=2.0 minatr=0.1 | -5.09 | 0.8 | 72 | 11.17 | -7.17 | 0.44 | 33 | 7.16 |
| breakout stop=1.0 tgt=3.5 rsi=50 trail=2.0 minatr=0.1 | -5.09 | 0.8 | 72 | 11.17 | -7.17 | 0.44 | 33 | 7.16 |
| breakout stop=1.0 tgt=3.5 rsi=35 trail=0.0 minatr=0.2 | -5.8 | 0.76 | 69 | 11.04 | -7.28 | 0.43 | 32 | 7.28 |
| breakout stop=1.0 tgt=3.5 rsi=42 trail=0.0 minatr=0.2 | -5.8 | 0.76 | 69 | 11.04 | -7.28 | 0.43 | 32 | 7.28 |
| breakout stop=1.0 tgt=3.5 rsi=50 trail=0.0 minatr=0.2 | -5.8 | 0.76 | 69 | 11.04 | -7.28 | 0.43 | 32 | 7.28 |
| breakout stop=1.0 tgt=3.5 rsi=35 trail=0.0 minatr=0.1 | -5.94 | 0.76 | 72 | 11.17 | -7.42 | 0.43 | 33 | 7.42 |

## Verdict

KEEP current params: no train-best config beat them out of sample with >= 6 trades and PF > 1.1.
