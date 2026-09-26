"""Performance statistics over exit events."""
from collections import defaultdict


def max_drawdown_pct(curve):
    peak, dd = None, 0.0
    for _, eq in curve:
        peak = eq if peak is None else max(peak, eq)
        if peak > 0:
            dd = max(dd, (peak - eq) / peak * 100)
    return dd


def _block(exits):
    n = len(exits)
    wins = [e for e in exits if e["pnl"] > 0]
    gross_win = sum(e["pnl"] for e in wins)
    gross_loss = -sum(e["pnl"] for e in exits if e["pnl"] <= 0)
    return {
        "trades": n,
        "win_rate_pct": round(len(wins) / n * 100, 1) if n else 0.0,
        "net_pnl": round(sum(e["pnl"] for e in exits), 2),
        "fees": round(sum(e.get("fees", 0) for e in exits), 2),
        "avg_r": round(sum(e["r"] for e in exits) / n, 3) if n else 0.0,
        "profit_factor": round(gross_win / gross_loss, 2) if gross_loss > 0 else (
            float("inf") if gross_win > 0 else 0.0),
    }


def summarize(exits, start_balance, curve=None):
    s = _block(exits)
    s["return_pct"] = round(s["net_pnl"] / start_balance * 100, 2)
    s["max_drawdown_pct"] = round(max_drawdown_pct(curve), 2) if curve else None
    by = defaultdict(list)
    for e in exits:
        by["setup:" + e["setup"]].append(e)
        by["exit:" + e["reason"]].append(e)
    s["breakdown"] = {k: _block(v) for k, v in sorted(by.items())}
    return s


def render(s, title):
    lines = [f"## {title}", ""]
    for k in ("source", "bars", "trades", "win_rate_pct", "net_pnl", "return_pct",
              "buy_and_hold_pct", "profit_factor", "avg_r", "fees", "max_drawdown_pct"):
        if k in s and s[k] is not None:
            lines.append(f"- {k}: {s[k]}")
    if s.get("breakdown"):
        lines += ["", "| slice | trades | win% | net | avg R | PF |", "|---|---|---|---|---|---|"]
        for k, b in s["breakdown"].items():
            lines.append(f"| {k} | {b['trades']} | {b['win_rate_pct']} | {b['net_pnl']} | "
                         f"{b['avg_r']} | {b['profit_factor']} |")
    return "\n".join(lines)
