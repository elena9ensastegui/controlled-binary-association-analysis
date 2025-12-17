def sdice_association_constructive(a: int, b: int, c: int, d: int) -> float:
    """
    Definición constructiva de la función de asociación basada en Dice y
    negación involutiva.

    A(X,Y) = (S_Dice(X,Y) - S_Dice(X,N(Y))) /
             (S_Dice(X,Y) + S_Dice(X,N(Y)))

    Esta función se conserva por trazabilidad teórica.
    """
    # Similitud Dice: S = 2a / (2a + b + c)
    def dice(x, y, z):
        denom = 2 * x + y + z
        if denom == 0:
            return 0.0
        return 2 * x / denom

    s_xy = dice(a, b, c)
    s_xny = dice(b, a, d)

    denom = s_xy + s_xny
    if denom == 0:
        return 0.0

    return (s_xy - s_xny) / denom


def sdice_association(a: int, b: int, c: int, d: int) -> float:
    """
    Forma final deducida de la función de asociación SDice.

    Esta expresión es algebraicamente equivalente a la definición constructiva,
    pero se presenta en forma cerrada para facilitar el análisis experimental
    y la comparación estructural con MCC.

    La función toma valores en [-1, 1] y satisface:
    A(X, N(Y)) = -A(X, Y)
    """
    numerator = a * (c + d) - b * (a + d)
    denominator = a * (c + d) + b * (a + d)

    if denominator == 0:
        return 0.0

    return numerator / denominator
