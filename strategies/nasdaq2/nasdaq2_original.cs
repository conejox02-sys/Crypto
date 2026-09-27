#region Using declarations
using System;
using NinjaTrader.Cbi;
using NinjaTrader.NinjaScript;
using NinjaTrader.NinjaScript.Strategies;
#endregion

namespace NinjaTrader.NinjaScript.Strategies
{
    public class nasdaq2 : Strategy
    {
        private double openPrice = 0;
        private double lastEntryPrice = 0;
        private bool canAverageDown = false;
        private int entryCount = 0;
        private int maxEntries = 5; // máximo de entradas por día
        private int contractsPerEntry = 3; // AHORA usa 3 contratos por operación

        private double sessionPnl = 0; // PnL de la sesión
        private double stopLossTotal = -3000; // Stop loss total

        protected override void OnStateChange()
        {
            if (State == State.SetDefaults)
            {
                Name = "nasdaq2";
                Calculate = Calculate.OnBarClose;
                EntriesPerDirection = maxEntries;
                EntryHandling = EntryHandling.AllEntries;
                IsExitOnSessionCloseStrategy = true;
                ExitOnSessionCloseSeconds = 30;
                IncludeCommission = true;
                IsInstantiatedOnEachOptimizationIteration = false;
            }
        }

        protected override void OnBarUpdate()
        {
            if (CurrentBar < 1) return;

            // Reset diario
            if (Bars.IsFirstBarOfSession)
            {
                openPrice = Open[0];
                lastEntryPrice = 0;
                canAverageDown = false;
                entryCount = 0;
                sessionPnl = 0; // Reinicia PnL diario
                return;
            }

            // Revisa el PnL acumulado y cierra si se excede el stop loss total
            sessionPnl = SystemPerformance.AllTrades.TradesPerformance.Currency.CumProfit;
            if (sessionPnl <= stopLossTotal && Position.MarketPosition != MarketPosition.Flat)
            {
                ExitLong("StopLossTotal", "");
                ExitShort("StopLossTotal", "");
                return;
            }

            if (openPrice == 0) return;

            double currentPrice = Close[0];
            double percentChange = (currentPrice - openPrice) / openPrice * 100;
            double tpPercent = 0.001; // 0.1%
            double tickMove = 200 * TickSize;

            if (Position.MarketPosition == MarketPosition.Flat && entryCount == 0)
            {
                if (percentChange <= -0.5)
                {
                    SetProfitTarget(CalculationMode.Percent, tpPercent);
                    EnterLong(contractsPerEntry, "Long_0.5");
                    lastEntryPrice = currentPrice;
                    canAverageDown = true;
                    entryCount++;
                }
                else if (percentChange >= 0.5)
                {
                    SetProfitTarget(CalculationMode.Percent, tpPercent);
                    EnterShort(contractsPerEntry, "Short_0.5");
                    lastEntryPrice = currentPrice;
                    canAverageDown = true;
                    entryCount++;
                }
            }

            if (canAverageDown && entryCount < maxEntries)
            {
                if (Position.MarketPosition == MarketPosition.Long && currentPrice <= lastEntryPrice - tickMove)
                {
                    SetProfitTarget(CalculationMode.Percent, tpPercent);
                    EnterLong(contractsPerEntry, "ReBuy");
                    lastEntryPrice = currentPrice;
                    entryCount++;
                }
                else if (Position.MarketPosition == MarketPosition.Short && currentPrice >= lastEntryPrice + tickMove)
                {
                    SetProfitTarget(CalculationMode.Percent, tpPercent);
                    EnterShort(contractsPerEntry, "ReSell");
                    lastEntryPrice = currentPrice;
                    entryCount++;
                }
            }
        }
    }
}
