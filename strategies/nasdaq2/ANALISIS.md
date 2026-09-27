# Análisis de la estrategia `nasdaq2`

## Cómo opera (exactamente, según el código)

1. **Apertura de sesión:** guarda el precio de apertura. La primera vela no opera.
2. **Primera entrada (solo una por sesión):**
   - si el cierre de una vela queda **0,5% por debajo** de la apertura → compra 3 contratos;
   - si queda **0,5% por encima** → vende en corto 3 contratos.
   Una vez hecha, no vuelve a entrar ese día aunque cierre con ganancia.
3. **Promediado:** cada 200 ticks en contra (en NQ, 50 puntos, ~0,2%) desde la
   última entrada, añade 3 contratos más, hasta 5 entradas (15 contratos).
4. **Salida con ganancia:** cada entrada tiene su **propio objetivo del +0,1%**
   desde su precio. Al rebotar, primero cierran las entradas más recientes (las
   de mejor precio); las primeras siguen en pérdida.
5. **Salida con pérdida:** en la práctica, **no hay stop**. Todo se cierra 30 s
   antes del final de la sesión, gane o pierda.

La idea de fondo es de reversión a la media: "si se alejó 0,5% de la apertura,
volverá un poco". Casi siempre es verdad, y por eso parece tan certera.

## Por qué parece tan certera, y por qué es peligrosa

Backtest fiel al código, 1 año de SOL-USDT en velas de 1 minuto (525.592 velas),
con costes tipo NQ (casi cero):

| | Original tal cual | Original sin el fallo del stop |
|---|---|---|
| Días ganadores | 71,8% | **97,8%** |
| Ganancia media de un día ganador | +0,11% | +0,14% |
| Pérdida media de un día perdedor | -0,45% | **-7,36%** |
| Peor día | -19,4% | -19,4% |
| Resultado del año | -3,5% | -1,5% |
| Factor de beneficio | 0,62 | 0,88 |

*(% del nocional de una entrada; el resultado del año es % del capital = 5 entradas.)*

**Gana 357 de 365 días, y aun así pierde en el año.** La pérdida media es 50
veces la ganancia media, así que 8 días malos borran casi un año de días buenos.
Es el perfil de "recoger monedas delante de una apisonadora": tasa de acierto
altísima con un riesgo de cola enorme. El promediado lo agrava, porque en un día
de tendencia fuerte suma contratos justo cuando más se equivoca. Su peor día
costó el 3,9% de todo el capital, y solo en febrero de 2026 perdió el 7,1%.

## Fallos en el código

1. **`StopLossTotal` no hace lo que dice el comentario.**
   `SystemPerformance.AllTrades...CumProfit` es la ganancia **realizada de toda
   la historia** de la estrategia, no la de la sesión, y el reinicio
   `sessionPnl = 0` se sobrescribe en la línea siguiente. Tiene dos efectos:
   - **Nunca protege de la pérdida abierta**, que es donde está el riesgo (15
     contratos en contra sin stop).
   - Una vez que la historia acumula -3.000 $, **cierra cada posición nueva en
     la vela siguiente a abrirla**. La estrategia queda "muerta" y sangrando
     comisiones. Por eso el original tal cual gana solo el 71,8% de los días: en
     184 de 365 días lo echó este fallo.
2. **Objetivo del 0,1% frente a los costes:** en NQ se cubre (comisión ~0,001%).
   En KuCoin spot (0,1% por lado) **es imposible ganar**: el objetivo es menor
   que las comisiones (0 aciertos de 298 en el backtest). En KuCoin futuros
   (0,06% taker / 0,02% maker) pierde un 10% en el año.
3. **Objetivos por entrada con promediado:** al rebotar se cierran las entradas
   de mejor precio y quedan abiertas las peores, así que el promediado casi
   nunca "rescata" la posición.

## Cómo la blindé (`nasdaq2_blindada.cs`)

Mantiene la misma idea (fade desde la apertura, promediado, objetivo por
entrada, una sola vez por sesión) y añade:

| Protección | Por qué |
|---|---|
| **Stop del ciclo completo** (realizado + abierto) = 0,2% del nocional de una entrada, como orden stop real | Es lo que corta la cola: el peor día pasa de -19,4% a -1,6% |
| **Niveles escalados por volatilidad** (rango diario medio de 14 días / 1,3%) | En un día normal de NQ son los niveles del original; en días locos, entrada, promediado, objetivo y stop se alejan en proporción |
| **Filtro de tendencia**: comprar caídas solo si el cierre diario está sobre la EMA de 40 días; vender subidas solo si está por debajo | Evita pelear contra las tendencias largas, que es donde vienen los días catastróficos |
| **Objetivo 0,3%** (en vez de 0,1%) | Con stop, un objetivo tan pequeño no compensa las pérdidas |
| **Límite diario en dinero** (3.000 $ por defecto) sobre realizado + abierto | El tope absoluto que el original quería tener |

Resultado (mismo año y datos, costes tipo NQ):

| | Original sin fallo | **Blindada** |
|---|---|---|
| Días operados | 365 | 143 |
| Ganancia media / pérdida media de un día | +0,14% / -7,36% | +1,13% / -0,83% |
| Días ganadores | 97,8% | 46,9% |
| Resultado del año (sin apalancar) | -1,5% | **+2,5%** |
| Caída máxima | 8,3% | **1,2%** |
| Peor día | -19,4% | **-1,6%** |
| Factor de beneficio | 0,88 | **1,20** |

**Sí, ahora "acierta" menos de la mitad de los días.** Esa es la parte honesta:
la certeza del original era una ilusión que se pagaba en los días malos. Con
stop, gana poco y de forma constante, y ningún día puede hundir la cuenta.

**¿Es por suerte con estos parámetros?** Validé de dos formas:
- Elegí mirando solo los primeros 8 meses y comprobé en los últimos 4 (datos
  que no vio).
- Probé las 12 combinaciones cercanas (stop 0,2–0,4%, objetivo 0,2–0,3%,
  tendencia de 20 o 40 días): **las 12 terminan el año en positivo** y las 12
  son positivas en el periodo de prueba. La ventaja es pequeña (factor de
  beneficio 1,05–1,2), pero estable.

## Adaptación a crypto (SOL-USDT, comisiones reales de KuCoin futuros)

Probado con 0,06% taker / 0,02% maker y 0,01% de deslizamiento, 1 año de velas
de 1 minuto, eligiendo en los primeros 8 meses y comprobando en los últimos 4.

| Variante | Configuraciones probadas | En positivo el año |
|---|---|---|
| Blindada con promediado, entradas a mercado | 18 | **0** |
| Blindada con promediado, entradas con orden límite | 18 | **0** |
| Sin promediado, entrada más lejana (búsqueda amplia) | 108 | 15 |

- **Con promediado no hay forma de ganar en crypto:** la ventaja que tenía con
  costes tipo NQ (+0,5% a +3,6% al año) la comen las comisiones (~3–4% al año).
- **Las entradas con orden límite son peores:** cuando el precio atraviesa tu
  nivel, suele ser porque sigue de largo (selección adversa).
- **Lo que sí funciona: una sola entrada, sin promediar**, cuando el precio se
  ha alejado de la apertura ~0,75 veces su rango diario medio (en SOL, ~4%).
  Objetivo ~1,3% y stop ~2,1% (escalados por volatilidad), y solo a favor de
  la tendencia de 40 días.

| Crypto, sin promediar (preset `CRYPTO`) | Resultado |
|---|---|
| Año completo | **+11,8%** sin apalancar |
| Primeros 8 meses / últimos 4 (no vistos) | +8,7% / **+8,1%** |
| Caída máxima | 6,3% |
| Operaciones | 48 al año (~1 por semana), 73% ganadoras |
| Ganancia media / pérdida media | +1,02% / -1,84% |
| Peor operación | -3,3% |
| Meses positivos | 9 de 13 |
| Largos / cortos | 14 largos (+9,3%) / 34 cortos (+2,4%) |

En el vecindario (entrada 0,8–1,25 × objetivo × stop, 45 combinaciones), 28
son positivas y la zona de entrada 0,9–1,1 es sólida. Pero con entrada 0,8
todas pierden, así que **el margen es estrecho**. Con 48 operaciones al año la
muestra es pequeña: es una ventaja prometedora, no probada. Requiere futuros
(dos tercios de las operaciones son cortos), y con apalancamiento se
multiplican por igual la ganancia y la caída máxima.

### Prueba en otras 5 monedas (datos nunca vistos): no se sostiene

La versión sin promediar se eligió con SOL. Aplicada tal cual a BTC, ETH, XRP,
DOGE y BNB (1 año, velas de 1 minuto, comisiones de KuCoin futuros; informe
completo en `reports/multi-coin-fade.md`):

| Moneda | Resultado del año (entrada 1,0) |
|---|---|
| SOL (donde se eligió) | +11,7% |
| BTC | -3,2% |
| ETH | -3,7% |
| BNB | -7,9% |
| XRP | -12,2% |
| DOGE | -20,8% |
| **Cartera de las 6** | **-6,0%**, 0,8 operaciones al día |

Con entrada 0,9 la cartera da -6,5%, y con 1,1 da -1,7%. **La ganancia en SOL
era casualidad de esa moneda, no una ventaja real:** en 5 de las 6 monedas
pierde. Veredicto: **no usar esta estrategia en crypto.**

## Lo que falta para dar un veredicto sobre NQ

Todo esto está medido en **SOL**, con niveles escalados y costes tipo NQ,
porque aquí no tengo datos de NQ. SOL se mueve unas 4 veces más que NQ (rango
diario medio 5,5% frente a ~1,3%) y cotiza 24 h, sin sesión. **El siguiente
paso imprescindible es probarla en NQ/MNQ:**

1. En NinjaTrader: *Tools → Historical Data → Export*, instrumento NQ o MNQ,
   *1 Minute*, *Last*, el mayor rango posible (idealmente 1–2 años).
2. Sube el `.txt` a este repo (o pásamelo) y ejecuto:
   `python3 strategies/nasdaq2/run_backtest.py --nt NQ_1min.txt --session-start 18`
   Compara el original y la blindada con exactamente estas mismas reglas.
3. En paralelo, importa `nasdaq2_blindada.cs` en NinjaTrader (*New → NinjaScript
   Editor*, pégalo y compila con F5). Pruébala en el *Strategy Analyzer* y
   después en **simulación con MNQ** (1/10 del tamaño de NQ) antes de nada real.

No he podido compilar el `.cs` aquí (necesita NinjaTrader). Si te da cualquier
error de compilación, pégamelo y lo corrijo.

## Veredicto

- **La lógica tiene algo real:** los alejamientos del 0,5% desde la apertura
  suelen revertir. Eso es lo que detectaste, y es correcto.
- **Tal como está, no es la mejor estrategia: es una con la ruina garantizada
  a plazo.** Sin stop y con promediado, un solo día de tendencia fuerte (NQ se
  mueve 3–4% en los días de noticias grandes) con 15 contratos puede costar
  decenas de miles de dólares.
- **Blindada, es una ventaja pequeña con riesgo controlado.** Merece probarse
  en NQ con datos reales. En KuCoin no es viable por las comisiones.
