"""Plain-Python indicators. Each returns a list aligned with the input; None
until the indicator has enough history."""


def ema(values, n):
    out = [None] * len(values)
    if len(values) < n:
        return out
    k = 2.0 / (n + 1)
    e = sum(values[:n]) / n
    out[n - 1] = e
    for i in range(n, len(values)):
        e = values[i] * k + e * (1 - k)
        out[i] = e
    return out


def sma(values, n):
    out = [None] * len(values)
    s = 0.0
    for i, v in enumerate(values):
        s += v
        if i >= n:
            s -= values[i - n]
        if i >= n - 1:
            out[i] = s / n
    return out


def rsi(closes, n=14):
    """Wilder RSI."""
    out = [None] * len(closes)
    if len(closes) <= n:
        return out
    gain = loss = 0.0
    for i in range(1, n + 1):
        d = closes[i] - closes[i - 1]
        gain += max(d, 0.0)
        loss += max(-d, 0.0)
    gain /= n
    loss /= n
    out[n] = 100.0 if loss == 0 else 100.0 - 100.0 / (1 + gain / loss)
    for i in range(n + 1, len(closes)):
        d = closes[i] - closes[i - 1]
        gain = (gain * (n - 1) + max(d, 0.0)) / n
        loss = (loss * (n - 1) + max(-d, 0.0)) / n
        out[i] = 100.0 if loss == 0 else 100.0 - 100.0 / (1 + gain / loss)
    return out


def atr(candles, n=14):
    """Wilder ATR."""
    out = [None] * len(candles)
    if len(candles) <= n:
        return out
    trs = [candles[0]["h"] - candles[0]["l"]]
    for i in range(1, len(candles)):
        c, pc = candles[i], candles[i - 1]["c"]
        trs.append(max(c["h"] - c["l"], abs(c["h"] - pc), abs(c["l"] - pc)))
    a = sum(trs[1:n + 1]) / n
    out[n] = a
    for i in range(n + 1, len(candles)):
        a = (a * (n - 1) + trs[i]) / n
        out[i] = a
    return out


def highest(values, n):
    """Highest of the n values BEFORE i (excludes the current bar)."""
    out = [None] * len(values)
    for i in range(n, len(values)):
        out[i] = max(values[i - n:i])
    return out
