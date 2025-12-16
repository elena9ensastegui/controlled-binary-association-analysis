# Coeficiente de correlación de Matthews (MCC)

El coeficiente de correlación de Matthews (Matthews Correlation Coefficient,
MCC) es una medida ampliamente utilizada para evaluar la calidad de
clasificadores binarios. Sin embargo, desde un punto de vista estructural,
el MCC puede interpretarse como una función de asociación definida sobre
tablas de contingencia 2×2.

Dada una tabla de contingencia caracterizada por los valores (a, b, c, d),
el MCC se define como:

MCC(a, b, c, d) =
(ad − bc) / √((a + b)(a + c)(d + b)(d + c)).

Siempre que el denominador sea distinto de cero, el valor del MCC pertenece
al intervalo [-1, 1].

El valor MCC = 1 indica asociación positiva perfecta entre X e Y,
MCC = -1 indica asociación negativa perfecta, y MCC = 0 indica ausencia
de asociación lineal entre las variables.

En este trabajo, el MCC se considera explícitamente como una función de
asociación entre dos variables dicotómicas, definida únicamente en términos
de la estructura conjunta de la tabla de contingencia, sin referencia a
ningún modelo de clasificación subyacente.

Esta interpretación permite utilizar el MCC como punto de referencia para
comparar otras funciones de asociación definidas sobre el mismo dominio.
