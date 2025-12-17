from itertools import product
from typing import List, Dict

from src.mcc import mcc
from src.sdice_association import sdice_association


def generate_contingency_tables(n: int):
    """
    Genera todas las tablas de contingencia 2x2 (a,b,c,d)
    tales que a + b + c + d = n y a,b,c,d >= 0.
    """
    for a in range(n + 1):
        for b in range(n - a + 1):
            for c in range(n - a - b + 1):
                d = n - a - b - c
                yield a, b, c, d


def run_level_A(n: int) -> List[Dict]:
    """
    Ejecuta el análisis Nivel A para un valor fijo de n.
    Retorna una lista de diccionarios con los resultados.
    """
    results = []

    for a, b, c, d in generate_contingency_tables(n):
        value_mcc = mcc(a, b, c, d)
        value_sdice = sdice_association(a, b, c, d)

        results.append({
            "a": a,
            "b": b,
            "c": c,
            "d": d,
            "n": n,
            "MCC": value_mcc,
            "SDice": value_sdice
        })

    return results


if __name__ == "__main__":
    # Valor de n para el análisis (ajustable)
    n = 20

    results = run_level_A(n)

    # Resumen simple
    print(f"Nivel A completado para n = {n}")
    print(f"Total de tablas analizadas: {len(results)}")

    # Mostrar algunos ejemplos
    for r in results[:5]:
        print(r)
