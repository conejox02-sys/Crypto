"""The nasdaq2 port must reproduce the NinjaScript mechanics exactly."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "strategies", "nasdaq2"))
import fade  # noqa: E402

DAY = 1_790_000_000 - 1_790_000_000 % 86400
ZERO = {"fee_taker": 0.0, "fee_maker": 0.0, "slippage": 0.0, "lifetime_stop": None}


def bars(path, day=DAY):
    """path: list of (o, h, l, c) for consecutive 1-minute bars."""
    return [{"t": day + i * 60, "o": o, "h": h, "l": lo, "c": c, "v": 1} for i, (o, h, lo, c) in enumerate(path)]


class FadePortTest(unittest.TestCase):
    def test_long_fade_hits_target(self):
        b = bars([(100, 100, 100, 100),      # first bar of session: open recorded, skipped
                  (100, 100, 99.4, 99.4),    # close -0.6% -> EnterLong at next open
                  (99.4, 99.6, 99.4, 99.5),  # fill 99.4, target 99.4994 touched
                  (99.5, 99.5, 99.5, 99.5)])
        cycles, lots = fade.run(b, ZERO)
        self.assertEqual(len(lots), 1)
        self.assertEqual(lots[0]["reason"], "target")
        self.assertAlmostEqual(lots[0]["pnl"], 0.001, places=6)
        self.assertEqual(cycles[0]["side"], 1)

    def test_short_fade_and_only_one_cycle_per_session(self):
        b = bars([(100, 100, 100, 100), (100, 100.6, 100, 100.6), (100.6, 100.6, 100.4, 100.5),
                  (100.5, 100.8, 100.5, 100.8), (100.8, 100.8, 100.8, 100.8)])
        cycles, lots = fade.run(b, ZERO)
        self.assertEqual([c["side"] for c in cycles], [-1])  # no second entry after the target
        self.assertEqual(lots[0]["reason"], "target")

    def test_averaging_per_lot_targets_and_session_close(self):
        b = bars([(100, 100, 100, 100), (100, 100, 99.4, 99.4),      # entry 1 signal
                  (99.4, 99.4, 99.2, 99.2),                          # fill 99.4; close 99.2 = -0.2% -> add
                  (99.2, 99.25, 99.0, 99.0),                         # fill 99.2; close -0.2% more -> add
                  (99.0, 99.12, 99.0, 99.1),                         # fill 99.0, its target 99.099 hits
                  (99.1, 99.1, 99.1, 99.1)])                         # session close: 2 lots at a loss
        cycles, lots = fade.run(b, ZERO)
        self.assertEqual([lot["reason"] for lot in lots], ["target", "session_close", "session_close"])
        self.assertEqual(cycles[0]["entries"], 3)
        self.assertLess(cycles[0]["pnl"], 0)

    def test_cycle_stop_caps_the_loss(self):
        path = [(100, 100, 100, 100), (100, 100, 99.4, 99.4)]
        px = 99.4
        for _ in range(40):
            path.append((px, px, px - 0.2, px - 0.2))
            px -= 0.2
        cycles, _ = fade.run(bars(path), dict(ZERO, cycle_stop_pct=1.0))
        self.assertEqual(cycles[0]["reason"], "cycle_stop")
        self.assertAlmostEqual(cycles[0]["pnl"], -0.01, places=4)

    def test_lifetime_stop_bug_exits_every_new_position(self):
        # day 1 loses more than the -0.2% realized threshold, day 2 gets kicked out right after entry
        d1 = [(100, 100, 100, 100), (100, 100, 99.4, 99.4), (99.4, 99.4, 98.0, 98.0), (98, 98, 98, 98)]
        d2 = [(100, 100, 100, 100), (100, 100, 99.4, 99.4), (99.4, 99.45, 99.3, 99.35),
              (99.35, 99.35, 99.35, 99.35), (99.35, 99.35, 99.35, 99.35)]
        b = bars(d1) + bars(d2, DAY + 86400)
        cycles, _ = fade.run(b, dict(ZERO, lifetime_stop=0.002))
        self.assertEqual(cycles[1]["reason"], "lifetime_stop")


    def test_limit_entry_needs_trade_through_and_pays_maker(self):
        p = dict(ZERO, entry_mode="limit", fee_maker=0.0002)
        touch = bars([(100, 100, 100, 100), (100, 100, 99.5, 99.6), (99.6, 99.7, 99.6, 99.7)])
        self.assertEqual(fade.run(touch, p)[1], [])  # touched 99.5, never traded through
        through = bars([(100, 100, 100, 100), (100, 100, 99.4, 99.45), (99.45, 99.7, 99.45, 99.7)])
        cycles, lots = fade.run(through, p)
        self.assertAlmostEqual(lots[0]["entry"], 99.5)
        self.assertEqual(lots[0]["reason"], "target")  # on the NEXT bar, not the fill bar
        self.assertAlmostEqual(lots[0]["pnl"], 0.001 - 0.0002 - 0.0002, places=6)

    def test_ninjatrader_export_loader(self):
        import tempfile
        path = os.path.join(tempfile.mkdtemp(), "NQ.txt")
        with open(path, "w") as f:
            f.write("20260102 180100;21000.25;21001;20999.5;21000.75;120\n"
                    "20260102 180200;21000.75;21002;21000.5;21001.5;80\n")
        b = fade.load_ninjatrader(path)
        self.assertEqual(len(b), 2)
        self.assertEqual(b[1]["t"] - b[0]["t"], 60)
        self.assertEqual(b[0]["c"], 21000.75)
        fade.SESSION["start_h"] = 18
        self.assertEqual(fade.day_key(b[0]["t"]), "2026-01-02")  # 18:00 opens the 01-02 18h session
        fade.SESSION["start_h"] = 0


if __name__ == "__main__":
    unittest.main()
