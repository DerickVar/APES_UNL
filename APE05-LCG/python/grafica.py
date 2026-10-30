"""Representación de la secuencia normalizada requerida por la guía."""

import matplotlib
matplotlib.use("Agg")  # Guarda el archivo PNG sin interfaz gráfica.
import matplotlib.pyplot as plt


def graficar_secuencia(indices, normalizados, semilla, destino):
    """Dibuja U_n frente al número de observación n."""
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.scatter(indices, normalizados, s=2)
    ax.set_title(f"Secuencia LCG normalizada (semilla {semilla})")
    ax.set_xlabel("Observación n")
    ax.set_ylabel("U_n = X_n / m")
    ax.set_ylim(0, 1)
    fig.tight_layout()
    fig.savefig(destino, dpi=160)
    plt.close(fig)
