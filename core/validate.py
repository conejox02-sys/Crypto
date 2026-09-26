"""Integrity tripwires (CI): configs parse, mode stays paper, params respect
the protected ceilings, ledger rows are well-formed."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import common  # noqa: E402

errors = []
cfg = common.load_json(common.CONFIG)
params = common.load_json(common.PARAMS)
if cfg.get("mode") != "paper":
    errors.append("config mode must stay 'paper' (demo) - live trading is an operator decision")
for k, ceil in cfg["ceilings"].items():
    if params.get(k, 0) > ceil:
        errors.append(f"params.{k}={params[k]} exceeds protected ceiling {ceil}")
for k in ("atr_stop", "atr_target", "max_hold_minutes"):
    if not params.get(k) or params[k] <= 0:
        errors.append(f"params.{k} must be > 0")
for i, row in enumerate(common.read_jsonl(common.LEDGER)):
    if row.get("type") not in ("entry", "exit") or "id" not in row:
        errors.append(f"ledger line {i + 1} malformed")
    if row.get("type") == "entry" and row.get("mode") != "paper":
        errors.append(f"ledger line {i + 1}: non-paper entry")
common.load_signals()
if errors:
    print("\n".join("FAIL: " + e for e in errors))
    sys.exit(1)
print("validate: ok")
