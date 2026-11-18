# Walk-forward research 2026-11-18

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-22 14:00 to 2026-11-18 13:30 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -33.48%
- combos: 324 in 36s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 23.48 | 2.15 | 35 | 7.16 | -2.17 | 0.65 | 12 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 19.42 | 3.08 | 21 | 3.94 | 0.65 | 1.15 | 7 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 19.03 | 3.03 | 22 | 3.94 | 0.65 | 1.15 | 7 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 17.99 | 2.68 | 22 | 3.94 | -0.36 | 0.93 | 9 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 17.61 | 2.64 | 23 | 3.94 | -0.36 | 0.93 | 9 | 4.82 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 23.48 | 2.15 | 35 | 7.16 | -2.17 | 0.65 | 12 | 5.66 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 18.9 | 2.91 | 19 | 5.94 | -0.74 | 0.87 | 7 | 5.36 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 13.3 | 2.34 | 23 | 4.21 | -0.37 | 0.92 | 7 | 4.02 |
| breakout stop=1.5 tgt=5.0 minatr=0.5 donch=30 regime=30d | 16.53 | 2.26 | 26 | 5.46 | -3.27 | 0.43 | 7 | 5.36 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 11.91 | 2.0 | 28 | 4.01 | -1.91 | 0.56 | 7 | 4.02 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=20 regime=30d | 17.52 | 2.57 | 20 | 5.94 | -2.95 | 0.63 | 9 | 7.55 |

## Verdict

RECOMMEND: `{"setups": {"pullback": false, "breakout": true}, "atr_stop": 1.0, "atr_target": 10.0, "min_atr_pct": 0.5, "donchian_len": 30, "regime_ema": 2880, "regime_slope_bars": 288}` - best on train and beats current params out of sample. Apply via IMPROVE.md only if the live demo ledger does not contradict it.
