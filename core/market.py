"""Public market data. KuCoin first, Crypto.com as a data-only fallback.

Stdlib only so it runs anywhere (GitHub Actions, a laptop, a VPS).
Candles are dicts {t, o, h, l, c, v} where t is the candle OPEN time in unix
seconds, oldest first. Every call reports which source answered, and the
ledger records it, so a fallback is never silent.
"""
import json
import time
import urllib.parse
import urllib.request

KUCOIN = "https://api.kucoin.com"
CRYPTOCOM = "https://api.crypto.com/exchange/v1"

TF_SEC = {"1m": 60, "5m": 300, "15m": 900, "30m": 1800, "1h": 3600, "4h": 14400}
_KUCOIN_TF = {"1m": "1min", "5m": "5min", "15m": "15min", "30m": "30min",
              "1h": "1hour", "4h": "4hour"}
_CDC_TF = {"1m": "1m", "5m": "5m", "15m": "15m", "30m": "30m", "1h": "1h", "4h": "4h"}


def _get(url, params=None, timeout=20):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "sol-daytrader/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def _cdc_symbol(symbol):
    return symbol.replace("-", "_")


def kucoin_candles(symbol, tf, start, end):
    out = {}
    cursor = int(end)
    while cursor > start:
        d = _get(KUCOIN + "/api/v1/market/candles",
                 {"type": _KUCOIN_TF[tf], "symbol": symbol,
                  "startAt": int(start), "endAt": cursor})
        if d.get("code") != "200000":
            raise RuntimeError(f"kucoin candles: {d.get('code')} {d.get('msg')}")
        rows = d.get("data") or []
        if not rows:
            break
        # KuCoin row: [time, open, close, high, low, volume, turnover], newest first
        for r in rows:
            t = int(r[0])
            out[t] = {"t": t, "o": float(r[1]), "c": float(r[2]), "h": float(r[3]),
                      "l": float(r[4]), "v": float(r[5])}
        oldest = min(int(r[0]) for r in rows)
        if oldest <= start or oldest - 1 >= cursor:
            break
        cursor = oldest - 1
        time.sleep(0.25)
    return [out[t] for t in sorted(out) if start <= t <= end]


def cryptocom_candles(symbol, tf, start, end):
    out = {}
    cursor = int(end)
    step = TF_SEC[tf]
    while cursor > start:
        d = _get(CRYPTOCOM + "/public/get-candlestick",
                 {"instrument_name": _cdc_symbol(symbol), "timeframe": _CDC_TF[tf],
                  "count": 300, "start_ts": int(start) * 1000,
                  "end_ts": (cursor + step) * 1000})
        rows = (d.get("result") or {}).get("data") or []
        if not rows:
            break
        for r in rows:
            t = int(r["t"]) // 1000
            out[t] = {"t": t, "o": float(r["o"]), "h": float(r["h"]), "l": float(r["l"]),
                      "c": float(r["c"]), "v": float(r["v"])}
        oldest = min(int(r["t"]) // 1000 for r in rows)
        if oldest <= start or oldest - 1 >= cursor:
            break
        cursor = oldest - 1
        time.sleep(0.25)
    return [out[t] for t in sorted(out) if start <= t <= end]


def candles(symbol, tf, start, end, prefer="kucoin"):
    """Returns (candles, source). Raises only if every source fails."""
    order = [("kucoin", kucoin_candles), ("cryptocom", cryptocom_candles)]
    if prefer == "cryptocom":
        order.reverse()
    errors = []
    for name, fn in order:
        try:
            rows = fn(symbol, tf, start, end)
            if rows:
                return rows, name
            errors.append(f"{name}: empty")
        except Exception as e:  # network, HTTP 4xx/5xx, bad payload
            errors.append(f"{name}: {e}")
    raise RuntimeError("no candle source answered: " + "; ".join(errors))


def ticker(symbol, prefer="kucoin"):
    """Returns ({bid, ask, last, ts}, source)."""
    errors = []
    sources = ["kucoin", "cryptocom"] if prefer == "kucoin" else ["cryptocom", "kucoin"]
    for name in sources:
        try:
            if name == "kucoin":
                d = _get(KUCOIN + "/api/v1/market/orderbook/level1", {"symbol": symbol})
                if d.get("code") != "200000" or not d.get("data"):
                    raise RuntimeError(f"{d.get('code')} {d.get('msg')}")
                x = d["data"]
                return {"bid": float(x["bestBid"]), "ask": float(x["bestAsk"]),
                        "last": float(x["price"]), "ts": int(x["time"]) // 1000}, name
            d = _get(CRYPTOCOM + "/public/get-tickers",
                     {"instrument_name": _cdc_symbol(symbol)})
            x = d["result"]["data"][0]
            return {"bid": float(x["b"]), "ask": float(x["k"]), "last": float(x["a"]),
                    "ts": int(x["t"]) // 1000}, name
        except Exception as e:
            errors.append(f"{name}: {e}")
    raise RuntimeError("no ticker source answered: " + "; ".join(errors))


def closed_only(rows, tf, now):
    step = TF_SEC[tf]
    return [c for c in rows if c["t"] + step <= now]
