# **Solemne 1 — Minería de Datos 2026**

## **Análisis de Datos Económicos y Financieros** 📈

---

## **Introducción**

Los mercados financieros y los indicadores económicos generan uno de los flujos de datos más ricos y accesibles del mundo. Detrás de cada variación de precio, cada reporte de PIB o cada índice de desempleo hay señales que pueden ser extraídas, analizadas y comunicadas con las herramientas que han aprendido durante el curso.

En esta evaluación aplicarán técnicas de minería de datos sobre datos económicos y financieros reales. El foco no está en predecir mercados ni en conocer economía de antemano — está en **explorar datos de manera estructurada, identificar patrones y comunicar hallazgos con evidencia**.

---

## **Objetivo**

Aplicar un flujo completo de análisis exploratorio de datos (EDA) sobre un dataset económico o financiero real: desde la obtención y limpieza de los datos hasta la visualización e interpretación de resultados.

---

## **Instrucciones**

### 1. Obtención de Datos

Seleccionen **al menos una fuente de datos** de las opciones disponibles más abajo. Pueden combinar fuentes si lo consideran útil, pero no es obligatorio.

Antes de extraer los datos, escriban en el notebook **qué esperan encontrar** — no hace falta que sea correcto, es simplemente su intuición inicial. Esa hipótesis va a ser importante más adelante.

---

### 2. Limpieza y Transformación

- Carguen los datos en **Pandas**.
- La primera celda de análisis debe mostrar: número de filas y columnas, tipos de variables, rango temporal exacto y conteo de valores nulos. No como texto — como output del código.
- Comenten ese output: ¿qué les dice sobre la calidad y el alcance real de los datos?
- Apliquen las transformaciones necesarias (normalización, filtros temporales/espaciales, combinación de fuentes si corresponde).
- Justifiquen cada decisión de limpieza en términos de **sus datos específicos**: si eliminan columnas, digan cuáles y por qué esas; si imputan valores, expliquen qué criterio usaron y por qué tiene sentido para este dataset.

---

### 3. Análisis Exploratorio (EDA)

Antes de graficar, planteen por escrito **al menos 2 preguntas analíticas**. Cada pregunta debe estar acompañada de la observación concreta que la motivó — algo que vieron en los datos durante la exploración inicial (una columna particular, un rango de fechas, una distribución llamativa). No se aceptan preguntas genéricas de economía que podrían hacerse sin haber mirado los datos.

Ejemplo de lo que **no** se busca: *"¿Cómo ha evolucionado el PIB en Latinoamérica?"*

Ejemplo de lo que **sí** se busca: *"Al explorar el dataset noté que hay un quiebre brusco en los valores de Chile entre 2019 y 2020. ¿Qué tan distinto es ese comportamiento respecto al promedio regional en ese período?"*

Como mínimo, el EDA debe incluir:

- Estadísticas descriptivas por grupo o variable relevante (media, mediana, desviación estándar, rangos).
- Identificación de outliers o comportamientos anómalos.
- Al menos una correlación o comparación entre variables.

**Decisiones descartadas:** al final de esta sección incluyan una subsección breve donde indiquen al menos una transformación, visualización o hipótesis que consideraron pero descartaron, explicando por qué. Por ejemplo: *"Descartamos un boxplot por país porque la muestra por grupo era muy desigual"* o *"Pensamos cruzar inflación con desempleo pero había poca superposición temporal entre los datasets"*.

---

### 4. Visualizaciones

Creen **al menos 4 visualizaciones**, usando las librerías que ya conocen (`Matplotlib`, `Seaborn`, u otras que estimen conveniente).

Como mínimo deben incluir:

- Una **serie temporal** (evolución de una variable en el tiempo).
- Una **comparación entre grupos** (barras, boxplot o similar).
- Una **distribución** de alguna variable de interés (histograma o KDE).
- Una visualización **libre** que responda directamente una de sus preguntas analíticas.

Cada visualización debe tener título, etiquetas en los ejes, unidades donde corresponda y leyenda si hay más de una serie.

Para la serie temporal, **identifiquen y comenten en el notebook al menos un período o punto específico que les llame la atención**, indicando fechas concretas y qué ven ahí. No basta con describir la forma general de la curva.

---

### 5. Interpretación de Resultados

- Respondan las preguntas analíticas planteadas en el paso 3, apoyándose en las visualizaciones.
- **Contrasten sus resultados con la hipótesis inicial** que escribieron antes de extraer los datos: ¿qué se cumplió? ¿qué no? ¿qué encontraron que no esperaban? Si todo resultó exactamente como esperaban, probablemente no miraron los datos con suficiente profundidad.
- Describan algo en los datos que **contradiga o matice** lo que esperaban encontrar, explicando por qué les sorprendió. Esto debe ser específico — fechas, países, variables, magnitudes concretas del dataset que usaron.
- Señalen al menos **una limitación real** del análisis: no una limitación genérica ("los datos pueden tener errores"), sino algo concreto que encontraron en *sus* datos — un período sin cobertura, un país con valores sospechosos, una variable que hubiera sido útil y no estaba disponible.

---

### 6. Entrega

- **Repositorio en GitHub** con el código del proyecto (se darán lineamientos por separado sobre el flujo de trabajo esperado en Git).
- Notebook Jupyter (`.ipynb`) ordenado y ejecutable de arriba a abajo sin errores.
- Archivo `requirements.txt` con las librerías utilizadas.
- **README.md** que describa brevemente: el dataset elegido, las preguntas que se plantearon y los principales hallazgos.

---

## **Fuentes de Datos**

Pueden usar cualquier combinación de las siguientes fuentes. No están limitados a estas opciones — si encuentran un dataset relevante y de calidad, pueden usarlo.

### 📊 BigQuery — Google Cloud Public Datasets

| Dataset | Descripción | Enlace |
|---|---|---|
| World Bank Global Economy | PIB, inflación, desempleo, deuda por país y año | [bigquery-public-data.world_bank_global_economy](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2sworld_bank_global_economy) |
| World Bank Health Population | Indicadores de salud y demografía con contexto económico | [bigquery-public-data.world_bank_health_population](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2sworld_bank_health_population) |
| FDIC Bankfind | Datos históricos de bancos en EE.UU. (activos, depósitos, quiebras) | [bigquery-public-data.fdic_banks](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2sfdic_banks) |

### 🌐 APIs Públicas

| API | Descripción | Enlace |
|---|---|---|
| Yahoo Finance (`yfinance`) | Precios históricos de acciones, ETFs, criptomonedas e índices | [pypi.org/project/yfinance](https://pypi.org/project/yfinance/) |
| Alpha Vantage | Series temporales financieras, divisas, indicadores económicos | [alphavantage.co](https://www.alphavantage.co/documentation/) |
| World Bank API | Indicadores económicos por país vía REST, sin necesidad de BigQuery | [data.worldbank.org/developers](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589) |
| FRED (Federal Reserve) | Indicadores macroeconómicos de EE.UU. (inflación, tasas, empleo) | [fred.stlouisfed.org/docs/api](https://fred.stlouisfed.org/docs/api/fred/) |

---

## **Evaluación**

| Criterio | Puntos |
|---|---|
| Calidad del EDA (descripción del dataset, limpieza justificada, estadísticas, decisiones descartadas) | 1.5 |
| Visualizaciones (claridad, variedad, etiquetado, comentario de serie temporal) | 1.5 |
| Interpretación (preguntas ancladas a los datos, contraste con hipótesis inicial, hallazgo inesperado específico) | 2.0 |
| Limitaciones reales del dataset | 0.5 |
| GitHub + README + notebook ejecutable | 0.5 |
| **Total** | **7** |
