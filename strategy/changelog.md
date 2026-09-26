# Strategy changelog

Every edit to strategy/params.json or strategy/signals.py gets one entry: date, change, evidence.

- 2026-09-26 v1: initial params (pullback + breakout, 1.5 ATR stop, 2.5 ATR target, 1% risk). Evidence: none yet - baseline to be measured by the demo ledger and daily research.
- 2026-09-26 v2: breakout only (pullback off), min_atr_pct 0.15 -> 0.4, donchian 20 -> 30, target 2.5 -> 8 ATR, trail off, max hold 8h -> 24h. Evidence (journal/retros/RETRO-2026-09-26.md): on 90d of KuCoin 15m, v1 lost 35% (PF 0.53, fees $332 on 202 trades; with zero fees it was roughly break-even, so costs killed it). 5 of 432 grid configs were positive in all 3 folds and all shared breakout + high-vol filter + large target + 24h hold; the 96-config neighbourhood around it is a plateau (90/96 net positive). v2: +23.6%, PF 1.94, DD 7.2%, 43 trades, positive in every fold. Caveat: the whole sample is a +72% bull run and v2 was selected on it; the demo ledger is the out-of-sample test.
