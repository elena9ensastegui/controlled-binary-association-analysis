# Diseño experimental – Nivel A (análisis controlado)

## Objetivo

El objetivo del Nivel A es analizar de forma controlada y exhaustiva el
comportamiento de distintas funciones de asociación definidas sobre tablas
de contingencia 2×2.

Este nivel experimental se centra exclusivamente en la estructura matemática
de las medidas, sin introducir ruido asociado a datos reales, modelos de
clasificación o procesos de muestreo.

## Dominio experimental

El dominio del experimento está constituido por el conjunto de todas las
tablas de contingencia 2×2 válidas, caracterizadas por cuádruplas
(a, b, c, d) tales que:

- a, b, c, d ∈ ℕ₀
- a + b + c + d = n
- n > 0

Para valores fijados de n, se consideran todas las combinaciones posibles
de (a, b, c, d) que satisfacen estas condiciones.

## Medidas analizadas

En este nivel experimental se consideran las siguientes funciones de
asociación:

- El coeficiente de correlación de Matthews (MCC), utilizado como referencia.
- Una función de asociación construida a partir de una similitud tipo Dice
  y una negación involutiva, definida sobre el mismo dominio.

Ambas funciones se definen únicamente en términos de los valores
(a, b, c, d) de la tabla de contingencia.

## Protocolo de análisis

Para cada tabla de contingencia válida en el dominio experimental:

1. Se calcula el valor de MCC(a, b, c, d).
2. Se calcula el valor de la función de asociación propuesta.
3. Se analiza la relación estructural entre ambas medidas.

El análisis se realiza de manera exhaustiva para valores crecientes de n,
permitiendo observar patrones de comportamiento, simetrías y diferencias
entre las funciones consideradas.

## Alcance

Este nivel experimental no pretende evaluar desempeño predictivo ni
calidad de clasificación. Su propósito es caracterizar propiedades
estructurales fundamentales de las funciones de asociación, proporcionando
una base sólida para experimentos posteriores en contextos aplicados.
