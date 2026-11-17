# Walk-forward research 2026-11-17

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-21 14:30 to 2026-11-17 14:00 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -32.43%
- combos: 324 in 20s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 18.54 | 1.87 | 35 | 7.16 | -0.94 | 0.85 | 13 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 14.48 | 2.54 | 22 | 3.94 | 0.62 | 1.14 | 8 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 13.89 | 2.38 | 21 | 3.94 | 0.62 | 1.14 | 8 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 13.11 | 2.22 | 23 | 3.94 | -0.39 | 0.93 | 10 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 12.53 | 2.1 | 22 | 3.94 | -0.39 | 0.93 | 10 | 4.82 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 11.32 | 2.03 | 27 | 4.01 | -1.94 | 0.56 | 8 | 4.02 |
| breakout stop=1.5 tgt=8.0 minatr=0.4 donch=30 regime=30d | 18.54 | 1.87 | 35 | 7.16 | -0.94 | 0.85 | 13 | 5.66 |
| breakout stop=1.5 tgt=8.0 minatr=0.5 donch=30 regime=30d | 15.16 | 2.3 | 20 | 5.94 | -0.52 | 0.91 | 8 | 5.36 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=20d | 9.89 | 1.62 | 41 | 3.88 | -2.96 | 0.45 | 14 | 4.62 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 14.9 | 2.36 | 19 | 5.94 | 0.51 | 1.09 | 8 | 5.36 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=30d | 10.64 | 1.61 | 42 | 4.4 | -2.96 | 0.45 | 14 | 4.62 |

## Verdict

RECOMMEND: `{"setups": {"pullback": false, "breakout": true}, "atr_stop": 1.0, "atr_target": 10.0, "min_atr_pct": 0.5, "donchian_len": 30, "regime_ema": 1920, "regime_slope_bars": 288}` - best on train and beats current params out of sample. Apply via IMPROVE.md only if the live demo ledger does not contradict it.
