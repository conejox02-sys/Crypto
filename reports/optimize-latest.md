# Walk-forward research 2026-11-17

- data: file:data/sol-15m.json, 17279 x 15m bars, 2026-05-21 01:00 to 2026-11-17 00:30 UTC
- train: first 11519 bars; test (out of sample): last 5760 bars
- buy & hold over test: -29.47%
- combos: 324 in 21s

| config | train ret% | train PF | train n | train DD% | TEST ret% | TEST PF | TEST n | TEST DD% |
|---|---|---|---|---|---|---|---|---|
| **current params** | 15.38 | 1.76 | 32 | 7.16 | 4.73 | 1.71 | 14 | 5.66 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=30d | 14.73 | 2.75 | 18 | 3.94 | 4.8 | 1.88 | 9 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=30 regime=20d | 13.45 | 2.43 | 21 | 3.94 | 5.6 | 2.19 | 8 | 4.02 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=30d | 13.36 | 2.36 | 19 | 3.94 | 3.75 | 1.6 | 11 | 4.82 |
| breakout stop=1.0 tgt=10.0 minatr=0.5 donch=20 regime=20d | 12.1 | 2.12 | 22 | 3.94 | 4.54 | 1.82 | 10 | 4.82 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=30d | 11.56 | 2.16 | 23 | 4.01 | -1.25 | 0.79 | 10 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.5 donch=30 regime=20d | 10.32 | 1.94 | 26 | 4.01 | -0.49 | 0.91 | 9 | 4.02 |
| breakout stop=1.0 tgt=5.0 minatr=0.4 donch=30 regime=20d | 8.9 | 1.55 | 40 | 3.88 | -1.53 | 0.76 | 15 | 4.62 |
| breakout stop=1.5 tgt=8.0 minatr=0.5 donch=30 regime=30d | 13.43 | 2.27 | 18 | 5.94 | 0.95 | 1.13 | 9 | 5.36 |
| breakout stop=1.5 tgt=10.0 minatr=0.5 donch=30 regime=30d | 13.18 | 2.34 | 17 | 5.94 | 4.3 | 1.7 | 8 | 5.36 |
| breakout stop=1.0 tgt=8.0 minatr=0.5 donch=30 regime=20d | 9.06 | 1.91 | 22 | 4.21 | 3.5 | 1.76 | 8 | 4.02 |

## Verdict

RECOMMEND: `{"setups": {"pullback": false, "breakout": true}, "atr_stop": 1.0, "atr_target": 10.0, "min_atr_pct": 0.5, "donchian_len": 30, "regime_ema": 2880, "regime_slope_bars": 288}` - best on train and beats current params out of sample. Apply via IMPROVE.md only if the live demo ledger does not contradict it.
