# Walk-forward research 2026-11-13

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-17 22:45 to 2026-11-13 22:15 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -23.75%
- combos: 324 in 19s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 17.08 | 1.89 | 30 | 7.16 | 3.76 | 1.5 | 15 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 15.57 | 3.02 | 17 | 3.94 | 4.8 | 1.88 | 9 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 14.19 | 2.56 | 18 | 3.94 | 3.75 | 1.6 | 11 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 12.57 | 2.24 | 22 | 3.94 | 5.6 | 2.19 | 8 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 12.38 | 2.33 | 22 | 4.01 | -1.25 | 0.79 | 10 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 11.23 | 1.98 | 23 | 3.94 | 4.54 | 1.82 | 10 | 4.82 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=30d | 10.93 | 1.75 | 36 | 3.88 | -1.18 | 0.85 | 18 | 4.62 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=30d | 11.09 | 2.34 | 18 | 4.21 | 2.72 | 1.51 | 9 | 4.02 |
| breakout stop=1.5 tgt=8.0 minatr=0.5 donch=30 regime=30d | 14.56 | 2.5 | 17 | 5.94 | 0.95 | 1.13 | 9 | 5.36 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 14.3 | 2.61 | 16 | 5.94 | 4.3 | 1.7 | 8 | 5.36 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 17.08 | 1.89 | 30 | 7.16 | 3.76 | 1.5 | 15 | 5.66 |

## Verdict

RECOMMEND: `{"setups": {"pullback": false, "breakout": true}, "atr_stop": 1.0, "atr_target": 10.0, "min_atr_pct": 0.5, "donchian_len": 30, "regime_ema": 2880, "regime_slope_bars": 288}` - best on train and beats current params out of sample. Apply via IMPROVE.md only if the live demo ledger does not contradict it.
