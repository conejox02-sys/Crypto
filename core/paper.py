"""Demo account tick: one pass of the live paper trader on KuCoin market data.

    python3 core/paper.py tick      # run once (GitHub Actions calls this every 15 min)
    python3 core/paper.py status    # print the account summary
    python3 core/paper.py reset     # wipe the demo account (asks no questions)

Each tick catches up on every strategy candle that closed since the last tick
(GitHub's scheduler drops many runs, so gaps of hours are normal):
1. The open position is managed through each CLOSED 1-minute candle; the stop
   and target behave like resting exchange orders.
2. Each missed strategy candle is evaluated in order, exactly as a bot running
   continuously would have: a signal on candle i fills at the open of the first
   1-minute candle after it closed (fill="replay"). Nothing after that moment
   is used for the decision.
3. A signal on the latest candle, found within one candle of its close, fills at
   the live best ask (fill="live").
Slippage and fees apply to both. Catch-up is capped at MAX_CATCHUP_H hours.
Every signal, fill and skip is journaled, with the data source that answered.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
import common  # noqa: E402
import engine  # noqa: E402
import market  # noqa: E402
import stats  # noqa: E402

SIGNALS = os.path.join(common.JOURNAL, "signals.jsonl")
STATUS = os.path.join(common.JOURNAL, "STATUS.md")


def iso(ts):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts))


MAX_CATCHUP_H = 48


def tick(now=None):
    now = int(now or time.time())
    cfg = common.load_json(common.CONFIG)
    params = common.load_json(common.PARAMS)
    state = common.load_json(common.STATE, {})
    signals = common.load_signals()
    sym, tf = cfg["symbol"], cfg["timeframe"]
    step = market.TF_SEC[tf]
    acct = engine.Account(cfg, params, state.get("account"))
    events, sig_rows, notes = [], [], []

    # Strategy candles: warm-up history plus everything missed since the last tick.
    horizon = now - MAX_CATCHUP_H * 3600
    last_eval = max(state.get("last_signal_bar", now), horizon)
    lookback = (signals.warmup(acct.p) + 20) * step
    rows, src = market.candles(sym, tf, min(last_eval, now) - lookback, now)
    closed = market.closed_only(rows, tf, now)
    if not closed:
        raise RuntimeError("no closed candles returned")
    if "last_signal_bar" not in state:  # first tick ever: only the latest candle
        last_eval = closed[-1]["t"] - 1
    pending = [i for i, c in enumerate(closed) if c["t"] > last_eval]
    x = signals.prepare(closed, acct.p)
    mark = closed[-1]["c"]

    # 1-minute candles covering the open position and the missed window.
    starts = [closed[i]["t"] + step for i in pending]
    if acct.pos:
        starts.append(state.get("managed_until", acct.pos["entry_ts"]))
    m1, src1 = ([], None)
    if starts and min(starts) < now:
        m1, src1 = market.candles(sym, "1m", min(starts), now)
        m1 = market.closed_only(m1, "1m", now)
    j = 0

    def manage_until(ts):
        nonlocal j
        while j < len(m1) and m1[j]["t"] + 60 <= ts:
            b = m1[j]
            j += 1
            if acct.pos and b["t"] >= state.get("managed_until", 0):
                state["managed_until"] = b["t"] + 60
                ev = acct.on_bar(b, 60)
                if ev:
                    ev.update({"mode": "paper", "source": src1})
                    events.append(ev)
                    notes.append(f"exit {ev['reason']} pnl {ev['pnl']:+.2f}")

    for i in pending:
        bar = closed[i]
        close_ts = bar["t"] + step
        ev = None
        manage_until(close_ts)
        state["last_signal_bar"] = bar["t"]
        if acct.pos:
            continue
        sig = signals.signal(x, i, acct.p)
        if not sig:
            continue
        row = {"ts": now, "bar": bar["t"], "setup": sig["setup"], "close": bar["c"],
               "atr": round(sig["atr"], 4), "source": src}
        live = i == len(closed) - 1 and now - close_ts <= step
        if live:
            ok, why = acct.can_enter(now, mark)
            if ok:
                tk, tsrc = market.ticker(sym)
                ev = acct.enter(now, tk["ask"], sig)
                if ev:
                    ev.update({"fill": "live", "source": tsrc, "bid": tk["bid"], "ask": tk["ask"]})
                    state["managed_until"] = (now // 60 + 1) * 60
                    mark = tk["last"]
        else:
            nxt = next((b for b in m1[j:] if b["t"] >= close_ts), None)
            if nxt is None:
                ok, why = False, "no_1m_data_after_signal"
            else:
                ok, why = acct.can_enter(nxt["t"], nxt["o"])
                if ok:
                    ev = acct.enter(nxt["t"], nxt["o"], sig)
                    if ev:
                        ev.update({"fill": "replay", "source": src1})
                        state["managed_until"] = nxt["t"]
        if ok and ev:
            ev.update({"mode": "paper", "signal_bar": bar["t"]})
            events.append(ev)
            notes.append(f"entry {sig['setup']} ({ev['fill']}) @ {ev['price']}")
            row["action"] = "entered_" + ev["fill"]
        elif ok:
            row["action"] = "skipped:size_below_min"
        else:
            row["action"] = "skipped:" + why
            notes.append(f"signal {sig['setup']} skipped ({why})")
        sig_rows.append(row)
    manage_until(now + 60)
    if m1:
        mark = m1[-1]["c"]

    common.append_jsonl(common.LEDGER, events)
    common.append_jsonl(SIGNALS, sig_rows)
    state["account"] = acct.state()
    state["last_tick"] = iso(now)
    state["last_price"] = mark
    common.save_json(common.STATE, state)
    eq = acct.equity(mark)
    pos = f"LONG {acct.pos['qty']:.4f} @ {acct.pos['entry']:.3f} stop {acct.pos['stop']:.3f} " \
          f"tgt {acct.pos['target']:.3f}" if acct.pos else "flat"
    line = f"{iso(now)} tick src={src} px={mark:.3f} equity={eq:.2f} {pos}" + \
           (" | " + "; ".join(notes) if notes else "")
    with open(common.CYCLES, "a") as f:
        f.write(line + "\n")
    write_status(cfg, state, eq, mark)
    print(line)


def write_status(cfg, state, eq, mark):
    exits = [e for e in common.read_jsonl(common.LEDGER) if e["type"] == "exit"]
    s = stats.summarize(exits, cfg["starting_balance_usdt"])
    start = cfg["starting_balance_usdt"]
    acct = state["account"]
    lines = [
        "# Demo account status (auto-generated by core/paper.py)", "",
        f"- last tick: {state['last_tick']}",
        f"- {cfg['symbol']} last: {mark:.3f}",
        f"- equity: {eq:.2f} USDT (start {start:.2f}, {((eq / start) - 1) * 100:+.2f}%)",
        f"- open position: {acct['pos']['setup'] + ' long @ ' + format(acct['pos']['entry'], '.3f') if acct['pos'] else 'none'}",
        "", stats.render(s, "Closed trades"),
    ]
    with open(STATUS, "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "tick"
    if cmd == "tick":
        tick()
    elif cmd == "status":
        print(open(STATUS).read() if os.path.exists(STATUS) else "no ticks yet")
    elif cmd == "reset":
        for p in (common.STATE, common.LEDGER, SIGNALS, STATUS):
            if os.path.exists(p):
                os.remove(p)
        print("demo account reset")
    else:
        sys.exit(f"unknown command {cmd}")


if __name__ == "__main__":
    main()
