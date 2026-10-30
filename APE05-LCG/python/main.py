"""Coordina el experimento y compara Python con el JAR sin archivos auxiliares."""

from pathlib import Path
import subprocess

from generador_lcg import CANTIDAD, SEMILLA_INICIAL, generar_lcg
from grafica import graficar_secuencia

RAIZ = Path(__file__).resolve().parent.parent
JAR = RAIZ / "java/target/lcg-java-1.0.0.jar"
SEMILLA_ALTERNATIVA = 54321


def leer_java(semilla):
    """Recibe las 10 000 observaciones por la salida estándar del JAR."""
    resultado = subprocess.run(
        ["java", "-jar", str(JAR), "--semilla", str(semilla), "--secuencia"],
        capture_output=True, text=True, check=True,
    )
    return [
        (int(n), int(x), float(u))
        for n, x, u in (linea.split() for linea in resultado.stdout.splitlines())
    ]


def mostrar_tabla(python_datos, java_datos):
    """El redondeo solo afecta a la presentación; se comparan valores completos."""
    print(f"{'n':>3} {'X Python':>10} {'X Java':>10} {'U Python':>14} {'U Java':>14}  Iguales")
    for p, j in zip(python_datos[:20], java_datos[:20]):
        print(f"{p[0]:3d} {p[1]:10d} {j[1]:10d} {p[2]:14.10f} {j[2]:14.10f}  {'Sí' if p == j else 'No'}")


def comparar_implementaciones(semilla):
    python_datos = list(generar_lcg(semilla))
    java_datos = leer_java(semilla)
    print(f"\nSemilla: {semilla}")
    mostrar_tabla(python_datos, java_datos)
    if len(python_datos) != CANTIDAD or len(java_datos) != CANTIDAD:
        raise ValueError("Ambas implementaciones deben generar 10 000 observaciones.")
    diferencias = sum(p != j for p, j in zip(python_datos, java_datos))
    print(f"Python: {len(python_datos)}; Java: {len(java_datos)}; diferencias: {diferencias}.")
    if diferencias:
        raise ValueError("Las secuencias Python y Java no coinciden.")
    return python_datos


def guardar_grafica(datos):
    destino = RAIZ / "graficas/grafica_lcg.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    graficar_secuencia(
        [n for n, _, _ in datos], [u for _, _, u in datos], SEMILLA_INICIAL, destino,
    )
    print(f"Gráfica: {destino}")


def main():
    """Ejecuta las dos semillas, compara y guarda únicamente la gráfica inicial."""
    try:
        inicial = comparar_implementaciones(SEMILLA_INICIAL)
        alternativa = comparar_implementaciones(SEMILLA_ALTERNATIVA)
        diferencias = sum(p[1] != q[1] for p, q in zip(inicial, alternativa))
        print(f"\nCambio de semilla {SEMILLA_INICIAL} → {SEMILLA_ALTERNATIVA}: "
              f"{diferencias} de {CANTIDAD} estados distintos en las mismas posiciones.")
        guardar_grafica(inicial)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        raise SystemExit(f"Error: {error}\nComprueba Java y compila primero con: cd java && mvn clean package") from error


if __name__ == "__main__":
    main()
