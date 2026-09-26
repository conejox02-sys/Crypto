"""Entry signals for SOL-USDT day trading. Strategy-owned: the improvement loop
may edit this file, with evidence (IMPROVE.md).

A signal is evaluated on a CLOSED candle i and acted on afterwards (next bar's
open in backtests, the live ask in paper ticks). Long only on spot.

Setups:
- pullback: uptrend (close > EMA200, EMA21 > EMA55) and RSI crossing back up
  through `rsi_pullback` after a dip — buy the dip inside a trend.
- breakout: uptrend on EMA200, close breaks the prior Donchian high on volume
  > `volume_mult` x its 20-bar average — ride momentum expansion.
Both require ATR >= `min_atr_pct` % of price so fees don't eat the edge.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))
import indicators as ind  # noqa: E402


def prepare(candles, p):
    closes = [c["c"] for c in candles]
    highs = [c["h"] for c in candles]
    vols = [c["v"] for c in candles]
    return {
        "close": closes,
        "ema_fast": ind.ema(closes, p["ema_fast"]),
        "ema_slow": ind.ema(closes, p["ema_slow"]),
        "ema_trend": ind.ema(closes, p["ema_trend"]),
        "rsi": ind.rsi(closes, p["rsi_len"]),
        "atr": ind.atr(candles, p["atr_len"]),
        "don_high": ind.highest(highs, p["donchian_len"]),
        "vol_avg": ind.sma(vols, 20),
        "vol": vols,
    }


def warmup(p):
    return max(p["ema_trend"], p["ema_slow"], p["donchian_len"], p["atr_len"], 20) + 2


def signal(x, i, p):
    """Returns None or {"side", "setup", "atr"} for the close of candle i."""
    if i < 1:
        return None
    need = ("ema_fast", "ema_slow", "ema_trend", "rsi", "atr", "don_high", "vol_avg")
    if any(x[k][i] is None for k in need) or x["rsi"][i - 1] is None:
        return None
    close, a = x["close"][i], x["atr"][i]
    if a / close * 100 < p["min_atr_pct"]:
        return None
    uptrend = close > x["ema_trend"][i]
    setups = p.get("setups", {})

    if setups.get("pullback") and uptrend and x["ema_fast"][i] > x["ema_slow"][i]:
        lvl = p["rsi_pullback"]
        if x["rsi"][i - 1] < lvl <= x["rsi"][i]:
            return {"side": "long", "setup": "pullback", "atr": a}

    if setups.get("breakout") and uptrend:
        if close > x["don_high"][i] and x["vol"][i] > p["volume_mult"] * x["vol_avg"][i]:
            return {"side": "long", "setup": "breakout", "atr": a}
    return None
