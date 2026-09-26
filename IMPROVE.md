# Improvement procedure (daily retro)

Run by Claude Code once a day, after the 05:11 UTC research job. Follow it
exactly once, then stop.

## Hard rules

- Never edit `core/`, `config/`, `.github/`, or this file. If a protected rule
  looks wrong, argue it in the retro under "Proposals for the operator".
- You may edit `strategy/params.json` and `strategy/signals.py`, and write
  `journal/retros/` and `strategy/changelog.md`.
- Every strategy edit must cite evidence: settled demo trades, or the research
  report's out-of-sample result. No speculative rewrites.
- Small samples: under ~20 closed demo trades, the demo ledger can veto a
  change but cannot justify one alone. Lean on out-of-sample research, and
  change at most ONE parameter group per day so its effect can be measured.

## Steps

1. `git pull`, then `python3 core/validate.py` and
   `python3 -m unittest discover -s tests`.
2. Read `journal/STATUS.md`, `journal/ledger.jsonl`, `journal/signals.jsonl`,
   and the tail of `journal/cycles.log`. Check health: did ticks run every
   ~15 min, which data source answered, were signals skipped as stale?
3. Read `reports/optimize-latest.md` and `reports/backtest-latest.md`.
4. Write `journal/retros/RETRO-<YYYY-MM-DD>.md`:
   - each closed trade: was it a bad signal, a bad fill, or normal variance?
   - per-setup verdict (pullback / breakout) on PF, avg R, and fees as a
     share of gross P&L
   - skipped signals: did the skip reason cost anything?
   - decision: change or keep, with the evidence
5. If the evidence supports it, edit `strategy/params.json` (bump `version`)
   and add a line to `strategy/changelog.md`.
6. `python3 core/validate.py`, then commit
   `git commit -am "retro: <one-line lesson>"` and push.
