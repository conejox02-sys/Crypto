# SOL/USDT day trader: a self-improving KuCoin demo account

A SOL-USDT day-trading bot that trades a **paper (demo) account on live KuCoin
market data** and improves its own strategy from evidence. The loop
architecture is adapted from [bennyjo/phil](https://github.com/bennyjo/phil)
(Apache-2.0), a self-improving Polymarket agent. Phil itself trades prediction
markets and bans crypto up/down bets, so it cannot trade SOL/USDT as-is. This
repo keeps its design (a protected engine, a strategy the agent may edit,
honest fills, a journal, retros, evidence-cited edits) and swaps the market for
KuCoin spot.

## How it runs

| Piece | What it does | When |
|---|---|---|
| `core/paper.py tick` | Demo account: manages the open position on 1m candles, checks the entry signal on the latest closed 15m candle, fills at the live KuCoin ask | GitHub Actions, every 15 min, catches up on missed runs (`.github/workflows/paper.yml`) |
| `core/optimize.py` | Walk-forward research on 60 days of 15m candles: ranks ~300 param combos on the first 2/3, checks them out of sample on the last 1/3 | 05:11 and 17:11 UTC (`research.yml`) |
| `IMPROVE.md` | The retro procedure: read the ledger + research, change params only with cited evidence | Daily, by Claude Code |

Everything the bot does lands in `journal/`: `ledger.jsonl` (fills),
`signals.jsonl` (every signal, entered or skipped and why), `cycles.log`
(one line per tick), `STATUS.md` (current equity and stats).

## Strategy (v1, `strategy/`)

15m candles, long only (spot).

- **Pullback**: price above EMA200, EMA21 > EMA55, RSI(14) crosses back up
  through 42. Buys dips inside an uptrend.
- **Breakout**: price above EMA200, close above the prior 20-bar high on
  volume > 1.5x average.
- Stop 1.5 ATR, target 2.5 ATR, breakeven at +1R, 2 ATR trailing stop after
  +1R, 8h max hold, 1% equity risked per trade.
- Skips candles whose ATR is under 0.15% of price, where fees eat the edge.
- Daily guards: -3% day loss stops trading until 00:00 UTC; max 6 trades/day;
  2-bar cooldown after a loss.

## Honest-fill rules (`core/engine.py`)

- 0.1% KuCoin taker fee on both sides, plus 3 bps slippage on market fills.
- Stops behave as resting stop orders: a gap through the stop fills at the
  open, not the stop.
- If one candle touches both the stop and the target, the stop is assumed to
  have filled first.
- The backtest enters at the next bar's open. The demo account enters at the
  live ask when it sees the signal within one candle.
- GitHub's scheduler drops many runs, so each tick catches up on every candle
  it missed (up to 48h) exactly as a continuously running bot would have:
  entry at the open of the first minute after the signal candle, exits checked
  minute by minute. These fills are tagged `"fill": "replay"`; nothing after
  the decision moment is used to make it.

## Guardrails

`config/protected.json` belongs to the operator: mode (`paper`), fee model,
and hard ceilings on risk per trade (2%), day loss (5%) and trades per day
(12). The strategy may tune `strategy/params.json` only inside those limits.
`core/validate.py`, run in CI, fails the build if the mode leaves `paper` or
params exceed a ceiling.

## About the "KuCoin demo account"

KuCoin retired its public API sandbox, and its in-app demo trading has no API.
The demo account here is therefore a paper account driven by KuCoin's live
public order book and candles. It needs no API keys and cannot touch funds.
If KuCoin can't be reached, market data falls back to Crypto.com, and every
row records which source answered.

## Run locally

```bash
python3 core/paper.py tick              # one demo tick
python3 core/paper.py status            # account summary
python3 core/backtest.py --days 30      # backtest current params
python3 core/optimize.py --days 60      # walk-forward research
python3 -m unittest discover -s tests   # tests
```

Python 3.10+, standard library only.

## Disclaimer

Research and education only. This is not financial advice. Backtest and paper
results overstate what live trading achieves.
