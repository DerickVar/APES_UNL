"""Implementa la recurrencia del LCG indicada en la guía APE 05."""

A = 1664525
C = 1013904223
M = 2**32
SEMILLA_INICIAL = 12345
CANTIDAD = 10_000


def generar_lcg(semilla: int):
    """Genera (n, X_n, U_n) desde X_1 hasta X_10000."""
    x = semilla  # Estado inicial X_0.
    for n in range(1, CANTIDAD + 1):
        x = (A * x + C) % M
        yield n, x, x / M
