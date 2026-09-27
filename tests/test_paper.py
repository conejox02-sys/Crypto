"""Demo-account ticks on synthetic data: catch-up after missed runs must make
the same decisions as a bot that never missed a tick."""
import math
import os
import random
import sys
import tempfile
import contextlib
import io
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))
import common  # noqa: E402
import market  # noqa: E402
import paper  # noqa: E402

T0 = 1_700_000_000 - 1_700_000_000 % 900


def synthetic_1m(n, seed=3):
    random.seed(seed)
    px, out = 120.0, []
    for i in range(n):
        o = px
        drift = 0.00012 if (i // 2500) % 3 else -0.00003
        px *= math.exp(random.gauss(drift, 0.0016))
        vol = random.uniform(5, 40) * (6 if random.random() < 0.02 else 1)
        out.append({"t": T0 + i * 60, "o": o, "h": max(o, px) * 1.0004,
                    "l": min(o, px) * 0.9996, "c": px, "v": vol})
    return out


def aggregate(m1, step):
    out = {}
    for b in m1:
        k = b["t"] - b["t"] % step
        if k not in out:
            out[k] = dict(b, t=k)
        else:
            a = out[k]
            a["h"], a["l"], a["c"] = max(a["h"], b["h"]), min(a["l"], b["l"]), b["c"]
            a["v"] += b["v"]
    return [out[k] for k in sorted(out)]


class PaperReplayTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m1 = synthetic_1m(9 * 1440)
        cls.series = {"1m": cls.m1, "15m": aggregate(cls.m1, 900)}

    def run_ticks(self, tick_times):
        d = tempfile.mkdtemp()
        patches = {(common, "STATE"): "state.json", (common, "LEDGER"): "ledger.jsonl",
                   (common, "CYCLES"): "cycles.log", (paper, "SIGNALS"): "signals.jsonl",
                   (paper, "STATUS"): "STATUS.md"}
        saved = {k: getattr(*k) for k in patches}
        saved_market = (market.candles, market.ticker)
        now = [0]

        def candles(sym, tf, start, end, prefer="kucoin"):
            return [b for b in self.series[tf] if start <= b["t"] <= min(end, now[0])], "synthetic"

        def ticker(sym, prefer="kucoin"):
            b = [x for x in self.m1 if x["t"] + 60 <= now[0]][-1]
            return {"bid": b["c"] * 0.9999, "ask": b["c"] * 1.0001, "last": b["c"], "ts": now[0]}, "synthetic"

        try:
            for (mod, name), fn in patches.items():
                setattr(mod, name, os.path.join(d, fn))
            market.candles, market.ticker = candles, ticker
            for t in tick_times:
                now[0] = t
                with contextlib.redirect_stdout(io.StringIO()):
                    paper.tick(t)
            return common.read_jsonl(common.LEDGER)
        finally:
            for (mod, name), v in saved.items():
                setattr(mod, name, v)
            market.candles, market.ticker = saved_market

    def test_gappy_ticks_match_dense_ticks(self):
        start = T0 + 3 * 1440 * 60 + 900
        dense = [start + k * 900 + 120 for k in range(6 * 96)]
        gappy = dense[::24]  # one tick every 6 hours
        led_dense = self.run_ticks(dense)
        led_gappy = self.run_ticks(gappy)
        e_dense = [r for r in led_dense if r["type"] == "entry"]
        e_gappy = [r for r in led_gappy if r["type"] == "entry"]
        self.assertGreater(len(e_dense), 0, "synthetic data produced no signals")
        self.assertTrue(all(r["fill"] == "replay" for r in e_gappy[:-1]))
        self.assertEqual([r["signal_bar"] for r in e_dense][:3], [r["signal_bar"] for r in e_gappy][:3])
        exits = [r for r in led_gappy if r["type"] == "exit"]
        self.assertTrue(all(x["ts"] > e["ts"] for e, x in zip(e_gappy, exits)))


if __name__ == "__main__":
    unittest.main()
