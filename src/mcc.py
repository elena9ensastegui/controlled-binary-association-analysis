import math


def mcc(a: int, b: int, c: int, d: int) -> float:
    """
    Coeficiente de correlación de Matthews (MCC) definido sobre
    una tabla de contingencia 2x2.

    Parámetros
    ----------
    a, b, c, d : int
        Valores no negativos de la tabla de contingencia.

    Retorna
    -------
    float
        Valor del MCC en el intervalo [-1, 1]. Si el denominador
        es cero, se retorna 0.0 por convención.
    """
    numerator = a * d - b * c
    denominator = math.sqrt((a + b) * (a + c) * (d + b) * (d + c))

    if denominator == 0:
        return 0.0

    return numerator / denominator
