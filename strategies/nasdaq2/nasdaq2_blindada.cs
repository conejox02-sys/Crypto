// nasdaq2_blindada: la misma lógica de nasdaq2 (fade desde la apertura de sesión
// con promediado), con las protecciones que el backtest mostró necesarias.
// Ver strategies/nasdaq2/ANALISIS.md para el porqué de cada cambio.
//
// Cambios respecto al original:
//  1. Stop real del ciclo completo (realizado de la sesión + abierto), puesto como
//     orden stop en el mercado, no solo comprobado al cierre de vela. El original
//     no tenía stop: su "StopLossTotal" leía el CumProfit de TODA la historia
//     (solo realizado), así que ignoraba la pérdida abierta y, una vez tocado,
//     cerraba cada operación nueva justo después de abrirla.
//  2. Niveles escalados por volatilidad: entrada, promediado, objetivo y stop se
//     multiplican por (rango diario medio de 14 días / 1.3%). En un día normal de
//     NQ son los mismos del original; en días muy volátiles se alejan.
//  3. Filtro de tendencia: solo compra caídas si el cierre diario está sobre su
//     EMA de 40 días, y solo vende subidas si está por debajo.
//  4. Objetivo 0.3% en vez de 0.1%.
//  5. Límite diario en dinero (MaxDailyLossCurrency) como tope absoluto.
//
// IMPORTANTE: los valores por defecto salen de un backtest en SOL-USDT (1 año, velas
// de 1 min) con costes tipo NQ. Verifícalos en el Strategy Analyzer con datos de
// NQ/MNQ antes de operar, empezando por MNQ en simulación.

#region Using declarations
using System;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using NinjaTrader.Cbi;
using NinjaTrader.Data;
using NinjaTrader.NinjaScript;
using NinjaTrader.NinjaScript.Indicators;
using NinjaTrader.NinjaScript.Strategies;
#endregion

namespace NinjaTrader.NinjaScript.Strategies
{
    public class nasdaq2Blindada : Strategy
    {
        private double openPrice;
        private double lastEntryPrice;
        private int entryCount;
        private double realizedAtSessionStart;
        private double scale = 1.0;
        private bool skipSession;

        protected override void OnStateChange()
        {
            if (State == State.SetDefaults)
            {
                Name = "nasdaq2Blindada";
                Description = "nasdaq2 con stop de ciclo, niveles por volatilidad y filtro de tendencia";
                Calculate = Calculate.OnBarClose;
                EntriesPerDirection = 5;
                EntryHandling = EntryHandling.AllEntries;
                IsExitOnSessionCloseStrategy = true;
                ExitOnSessionCloseSeconds = 30;
                IncludeCommission = true;
                StopTargetHandling = StopTargetHandling.PerEntryExecution;
                BarsRequiredToTrade = 1;

                ContractsPerEntry = 3;
                MaxEntries = 5;
                EntryPct = 0.5;
                StepPct = 0.2;
                TargetPct = 0.3;
                CycleStopPct = 0.2;
                MaxDailyLossCurrency = 3000;
                UseVolScaling = true;
                ReferenceAdrPct = 1.3;
                AdrDays = 14;
                UseTrendFilter = true;
                TrendDays = 40;
            }
            else if (State == State.Configure)
            {
                EntriesPerDirection = MaxEntries;
                AddDataSeries(BarsPeriodType.Day, 1);
            }
        }

        protected override void OnBarUpdate()
        {
            if (BarsInProgress != 0 || CurrentBar < 1)
                return;

            double cumProfit = SystemPerformance.AllTrades.TradesPerformance.Currency.CumProfit;

            if (Bars.IsFirstBarOfSession)
            {
                openPrice = Open[0];
                lastEntryPrice = 0;
                entryCount = 0;
                realizedAtSessionStart = cumProfit;
                skipSession = false;
                scale = 1.0;
                if (UseVolScaling)
                {
                    // Series 1 index 0 is the last COMPLETED daily bar: no look-ahead.
                    if (CurrentBars[1] < AdrDays)
                        skipSession = true;
                    else
                    {
                        double sum = 0;
                        for (int k = 0; k < AdrDays; k++)
                            sum += (Highs[1][k] - Lows[1][k]) / Opens[1][k] * 100.0;
                        scale = (sum / AdrDays) / ReferenceAdrPct;
                    }
                }
                if (UseTrendFilter && CurrentBars[1] < TrendDays)
                    skipSession = true;
                return;
            }

            if (openPrice == 0 || skipSession)
                return;

            double pointValue = Instrument.MasterInstrument.PointValue;
            double sessionRealized = cumProfit - realizedAtSessionStart;

            // Hard limit in money on realized + open P&L (belt and braces behind the stop orders).
            if (Position.MarketPosition != MarketPosition.Flat)
            {
                double open = Position.GetUnrealizedProfitLoss(PerformanceUnit.Currency, Close[0]);
                if (sessionRealized + open <= -MaxDailyLossCurrency)
                {
                    ExitLong("DailyLossLimit", "");
                    ExitShort("DailyLossLimit", "");
                    entryCount = MaxEntries;  // no more entries this session
                    return;
                }
                UpdateCycleStop(Position.AveragePrice, Position.Quantity, Position.MarketPosition, sessionRealized, pointValue);
            }

            double price = Close[0];
            double change = (price - openPrice) / openPrice * 100.0;
            double entryPct = EntryPct * scale;
            double stepMove = lastEntryPrice * StepPct * scale / 100.0;
            SetProfitTarget(CalculationMode.Percent, TargetPct * scale / 100.0);

            if (Position.MarketPosition == MarketPosition.Flat && entryCount == 0)
            {
                double trend = UseTrendFilter ? EMA(BarsArray[1], TrendDays)[0] : 0;
                bool longOk = !UseTrendFilter || Closes[1][0] > trend;
                bool shortOk = !UseTrendFilter || Closes[1][0] < trend;

                if (change <= -entryPct && longOk)
                {
                    UpdateCycleStop(price, ContractsPerEntry, MarketPosition.Long, sessionRealized, pointValue);
                    EnterLong(ContractsPerEntry, "Long_fade");
                    lastEntryPrice = price;
                    entryCount++;
                }
                else if (change >= entryPct && shortOk)
                {
                    UpdateCycleStop(price, ContractsPerEntry, MarketPosition.Short, sessionRealized, pointValue);
                    EnterShort(ContractsPerEntry, "Short_fade");
                    lastEntryPrice = price;
                    entryCount++;
                }
            }
            else if (Position.MarketPosition != MarketPosition.Flat && entryCount < MaxEntries)
            {
                int qty = Position.Quantity + ContractsPerEntry;
                if (Position.MarketPosition == MarketPosition.Long && price <= lastEntryPrice - stepMove)
                {
                    double avg = (Position.AveragePrice * Position.Quantity + price * ContractsPerEntry) / qty;
                    UpdateCycleStop(avg, qty, MarketPosition.Long, sessionRealized, pointValue);
                    EnterLong(ContractsPerEntry, "ReBuy");
                    lastEntryPrice = price;
                    entryCount++;
                }
                else if (Position.MarketPosition == MarketPosition.Short && price >= lastEntryPrice + stepMove)
                {
                    double avg = (Position.AveragePrice * Position.Quantity + price * ContractsPerEntry) / qty;
                    UpdateCycleStop(avg, qty, MarketPosition.Short, sessionRealized, pointValue);
                    EnterShort(ContractsPerEntry, "ReSell");
                    lastEntryPrice = price;
                    entryCount++;
                }
            }
        }

        // One stop price for the whole position: where realized + open P&L of the
        // session reaches -min(CycleStopPct of one entry's notional, MaxDailyLossCurrency).
        private void UpdateCycleStop(double avgPrice, int quantity, MarketPosition side, double sessionRealized, double pointValue)
        {
            if (quantity <= 0)
                return;
            double entryNotional = openPrice * pointValue * ContractsPerEntry;
            double allowed = Math.Min(CycleStopPct * scale / 100.0 * entryNotional, MaxDailyLossCurrency);
            double room = allowed + sessionRealized;  // realized profit today widens the room, a loss narrows it
            if (room <= 0)
                room = TickSize * pointValue * quantity;  // at least one tick
            double distance = room / (quantity * pointValue);
            double stopPrice = side == MarketPosition.Long ? avgPrice - distance : avgPrice + distance;
            SetStopLoss(CalculationMode.Price, Instrument.MasterInstrument.RoundToTickSize(stopPrice));
        }

        #region Properties
        [NinjaScriptProperty]
        [Range(1, int.MaxValue)]
        [Display(Name = "Contratos por entrada", Order = 1, GroupName = "Tamaño")]
        public int ContractsPerEntry { get; set; }

        [NinjaScriptProperty]
        [Range(1, 10)]
        [Display(Name = "Máximo de entradas (promediado)", Order = 2, GroupName = "Tamaño")]
        public int MaxEntries { get; set; }

        [NinjaScriptProperty]
        [Range(0.05, 5)]
        [Display(Name = "Entrada: % desde la apertura", Order = 1, GroupName = "Niveles")]
        public double EntryPct { get; set; }

        [NinjaScriptProperty]
        [Range(0.05, 5)]
        [Display(Name = "Promediado: % entre entradas", Order = 2, GroupName = "Niveles")]
        public double StepPct { get; set; }

        [NinjaScriptProperty]
        [Range(0.01, 5)]
        [Display(Name = "Objetivo: % por entrada", Order = 3, GroupName = "Niveles")]
        public double TargetPct { get; set; }

        [NinjaScriptProperty]
        [Range(0.01, 10)]
        [Display(Name = "Stop del ciclo: % del nocional de UNA entrada", Order = 1, GroupName = "Protección")]
        public double CycleStopPct { get; set; }

        [NinjaScriptProperty]
        [Range(1, double.MaxValue)]
        [Display(Name = "Pérdida máxima diaria ($)", Order = 2, GroupName = "Protección")]
        public double MaxDailyLossCurrency { get; set; }

        [NinjaScriptProperty]
        [Display(Name = "Escalar niveles por volatilidad", Order = 3, GroupName = "Protección")]
        public bool UseVolScaling { get; set; }

        [NinjaScriptProperty]
        [Range(0.1, 10)]
        [Display(Name = "Rango diario de referencia %", Order = 4, GroupName = "Protección")]
        public double ReferenceAdrPct { get; set; }

        [NinjaScriptProperty]
        [Range(2, 60)]
        [Display(Name = "Días para el rango medio", Order = 5, GroupName = "Protección")]
        public int AdrDays { get; set; }

        [NinjaScriptProperty]
        [Display(Name = "Filtro de tendencia diaria", Order = 6, GroupName = "Protección")]
        public bool UseTrendFilter { get; set; }

        [NinjaScriptProperty]
        [Range(2, 200)]
        [Display(Name = "Días de la EMA de tendencia", Order = 7, GroupName = "Protección")]
        public int TrendDays { get; set; }
        #endregion
    }
}
