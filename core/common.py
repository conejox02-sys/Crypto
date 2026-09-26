"""Shared paths and loaders."""
import importlib.util
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG = os.path.join(ROOT, "config", "protected.json")
PARAMS = os.path.join(ROOT, "strategy", "params.json")
JOURNAL = os.path.join(ROOT, "journal")
LEDGER = os.path.join(JOURNAL, "ledger.jsonl")
STATE = os.path.join(JOURNAL, "state.json")
CYCLES = os.path.join(JOURNAL, "cycles.log")
REPORTS = os.path.join(ROOT, "reports")
CACHE = os.path.join(ROOT, "data")


def load_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path) as f:
        return json.load(f)


def save_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp, path)


def append_jsonl(path, rows):
    if not rows:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        for r in rows:
            f.write(json.dumps(r, sort_keys=True) + "\n")


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def load_signals():
    """Imports strategy/signals.py (strategy-owned, so loaded by path)."""
    path = os.path.join(ROOT, "strategy", "signals.py")
    spec = importlib.util.spec_from_file_location("signals", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
