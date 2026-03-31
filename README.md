# Solemne 1 — Minería de Datos 2026

## Descripción del proyecto

Este trabajo realiza un análisis exploratorio de datos (EDA) sobre un conjunto de precios históricos del S&P 500.  
A partir de un dataset amplio, se seleccionaron 11 empresas para comparar el comportamiento de dos grupos:

- **Gigantes tecnológicos:** Apple, Microsoft, Nvidia, Google, Amazon, Meta, Netflix y Tesla.
- **Consumo estable:** Coca-Cola, Pepsi y McDonald's.

El objetivo fue identificar patrones relevantes en la evolución de sus precios, su volatilidad y su respuesta frente a eventos económicos importantes.

## Dataset utilizado

Se trabajó con precios históricos diarios de acciones del S&P 500, reorganizados y limpiados para poder analizarlos correctamente en Pandas.

Durante la preparación se realizó lo siguiente:

- corrección de encabezados y estructura del archivo
- conversión de columnas a formato numérico
- selección de 11 empresas de interés
- tratamiento de valores nulos

## Preguntas de investigación

Antes del análisis se plantearon las siguientes preguntas:

1. **¿Cómo afectó el shock de la pandemia (marzo de 2020) a las acciones analizadas?**
2. **¿Se observa un crecimiento más marcado en empresas como Nvidia y Microsoft durante el auge de la inteligencia artificial (2023–2024)?**
3. **¿Las empresas tecnológicas presentan mayor volatilidad que las empresas de consumo básico?**
4. **¿Se nota una caída general en 2022 asociada al contexto de inflación e incertidumbre económica?**

## Principales hallazgos

- En **marzo de 2020** se observa una caída brusca en prácticamente todos los activos, consistente con el impacto global de la pandemia.
- Las empresas tecnológicas muestran una **recuperación más rápida** y un crecimiento más pronunciado en los años posteriores, especialmente **Nvidia** y **Microsoft**.
- Al analizar los **retornos diarios**, los activos tecnológicos presentan una **mayor volatilidad** que las empresas de consumo, confirmando una diferencia clara en nivel de riesgo.
- Durante **2022** se aprecia un periodo de desaceleración o caída en varios activos, aunque con intensidades distintas según la empresa.
- La comparación entre activos muestra que el análisis con **retornos** entrega una visión más realista que trabajar solo con precios absolutos.

## Conclusión

El análisis muestra que los eventos económicos globales sí dejan huellas visibles en los precios de las acciones, pero no afectan a todas las empresas de la misma forma.  
Los activos tecnológicos resultan más sensibles a cambios de mercado, mientras que las empresas de consumo tienden a mantener un comportamiento más estable.