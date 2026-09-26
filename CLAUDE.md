# SOL/USDT day trader

Self-improving paper (demo) trader for SOL-USDT on KuCoin market data. See
README.md for the design and IMPROVE.md for the daily retro procedure.

- `core/` and `config/protected.json` are operator-owned: the engine, the
  honest-fill model, and the hard caps. The retro loop never edits them.
- `strategy/` is what self-improves. Edits need evidence and a
  `strategy/changelog.md` entry.
- `journal/` is written by `core/paper.py`; never hand-edit ledger rows.
- Tests: `python3 -m unittest discover -s tests`; checks: `python3 core/validate.py`.
- Standard library only; no pip dependencies.
