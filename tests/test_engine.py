import math
import os
import random
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))
import backtest  # noqa: E402
import common  # noqa: E402
import engine  # noqa: E402
import indicators  # noqa: E402

CFG = common.load_json(common.CONFIG)
PARAMS = common.load_json(common.PARAMS)


def bar(t, o, h, l, c, v=100.0):
    return {"t": t, "o": o, "h": h, "l": l, "c": c, "v": v}


class EngineTest(unittest.TestCase):
    def setUp(self):
        self.acct = engine.Account(CFG, PARAMS)
        ok, _ = self.acct.can_enter(0, 100.0)
        self.assertTrue(ok)
        self.entry = self.acct.enter(0, 100.0, {"side": "long", "setup": "pullback", "atr": 1.0})

    def test_entry_sizing_respects_risk(self):
        pos = self.acct.pos
        risk = pos["qty"] * (pos["entry"] - pos["stop"])
        self.assertAlmostEqual(risk, CFG["starting_balance_usdt"] * PARAMS["risk_per_trade_pct"] / 100, places=6)
        self.assertGreater(self.entry["price"], 100.0)  # slippage paid

    def test_stop_wins_when_bar_hits_both(self):
        pos = self.acct.pos
        ev = self.acct.on_bar(bar(60, 100, pos["target"] + 1, pos["stop"] - 1, 100), 60)
        self.assertEqual(ev["reason"], "stop")
        self.assertLess(ev["pnl"], 0)

    def test_gap_fills_at_open(self):
        pos = self.acct.pos
        gap = pos["stop"] - 2
        ev = self.acct.on_bar(bar(60, gap, gap, gap - 1, gap), 60)
        self.assertEqual(ev["reason"], "stop_gap")
        self.assertLess(ev["price"], pos["stop"])

    def test_target_profit_after_fees(self):
        tgt = self.acct.pos["target"]
        ev = self.acct.on_bar(bar(60, 100.5, tgt + 0.1, 100.2, tgt), 60)
        self.assertEqual(ev["reason"], "target")
        self.assertGreater(ev["pnl"], 0)
        self.assertGreater(ev["fees"], 0)

    def test_breakeven_moves_next_bar(self):
        pos = self.acct.pos
        r = pos["entry"] - pos["init_stop"]
        self.assertIsNone(self.acct.on_bar(bar(60, 100.2, pos["entry"] + 1.1 * r, 100.1, 101), 60))
        self.assertGreater(self.acct.pos["stop"], self.acct.pos["entry"])

    def test_daily_loss_limit_blocks(self):
        self.acct.pos = None
        self.acct.day_pnl = -1000
        ok, why = self.acct.can_enter(10, 100)
        self.assertFalse(ok)
        self.assertEqual(why, "daily_loss_limit")

    def test_ceiling_clamps_params(self):
        p = dict(PARAMS, risk_per_trade_pct=50)
        self.assertEqual(engine.effective_params(p, CFG)["risk_per_trade_pct"],
                         CFG["ceilings"]["risk_per_trade_pct"])


class IndicatorTest(unittest.TestCase):
    def test_rsi_bounds_and_ema(self):
        xs = [100 + math.sin(i / 3) * 5 for i in range(100)]
        r = [v for v in indicators.rsi(xs, 14) if v is not None]
        self.assertTrue(all(0 <= v <= 100 for v in r))
        self.assertAlmostEqual(indicators.ema([1.0] * 30, 10)[-1], 1.0)


class BacktestSmoke(unittest.TestCase):
    def test_synthetic_run_is_consistent(self):
        random.seed(7)
        px, rows = 120.0, []
        for i in range(3000):
            o = px
            px *= math.exp(random.gauss(0.00005, 0.004))
            h, l = max(o, px) * (1 + abs(random.gauss(0, 0.001))), min(o, px) * (1 - abs(random.gauss(0, 0.001)))
            rows.append(bar(i * 900, o, h, l, px, random.uniform(50, 300)))
        ev, acct, curve = backtest.run(rows, PARAMS, CFG, common.load_signals())
        exits = [e for e in ev if e["type"] == "exit"]
        self.assertEqual(len(exits), len([e for e in ev if e["type"] == "entry"]))
        self.assertAlmostEqual(CFG["starting_balance_usdt"] + sum(e["pnl"] for e in exits), acct.cash, places=2)
        self.assertIsNone(acct.pos)


if __name__ == "__main__":
    unittest.main()
