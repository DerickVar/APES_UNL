import numpy as np
import matplotlib.pyplot as plt
import modelo

# 1. Datos iniciales de la guia
datos = [1000, 1100, 1250, 1400, 1600, 1850, 2100]

# 2. Parametros de configuracion
P0 = datos[0]             # Poblacion inicial (1000)
tiempo = len(datos) - 1   # Numero de periodos (6 periodos)
sigma = 50.0              # Nivel de ruido / aleatoriedad
dt = 0.1                  # Paso temporal para Euler

# Estimacion de la tasa media de crecimiento r
tasas = [(datos[i] - datos[i - 1]) / datos[i - 1] for i in range(1, len(datos))]
r = float(np.mean(tasas)) # Tasa aproximada


def ejecutar():
    # Llamadas al modulo con la logica matematica
    t_det, p_det = modelo.modelo_deterministico(P0, r, tiempo)
    t_disc, p_disc = modelo.modelo_discreto(P0, r, tiempo)
    t_est, p_est = modelo.modelo_estocastico(P0, r, sigma, tiempo)
    t_cont, p_cont = modelo.modelo_continuo_euler(P0, r, tiempo, dt)

    # Imprimir resumen de tablas en terminal
    print("=== RESULTADOS COMPARATIVOS DE LOS MODELOS ===")
    print(f"Poblacion inicial (P0): {P0} | Tasa r estimada: {r:.4f} | Ruido sigma: {sigma}")
    print("-" * 65)
    print(f"{'Periodo':<8} | {'Datos Guia':<12} | {'Discreto':<12} | {'Estocastico':<12}")
    print("-" * 65)
    for i in range(len(datos)):
        print(f"{i:<8} | {datos[i]:<12} | {p_disc[i]:<12.2f} | {p_est[i]:<12.2f}")

    # Generacion de la grafica
    plt.figure(figsize=(10, 6))
    plt.plot(t_det, p_det, 'b-', label="Deterministico (Exponencial Analitico)", linewidth=2)
    plt.plot(t_cont, p_cont, 'g--', label=f"Continuo (Euler dt={dt})", linewidth=1.5)
    plt.step(t_disc, p_disc, 'm.-', where='post', label="Discreto (P_{t+1})", linewidth=1.5)
    plt.plot(t_est, p_est, 'r*-', label=f"Estocastico (N(0, sigma={sigma}))", linewidth=1.5)
    plt.scatter(range(len(datos)), datos, color='black', zorder=5, label="Datos Reales Guia")

    plt.title("Comparacion de Modelos: Deterministico, Discreto, Estocastico y Continuo")
    plt.xlabel("Tiempo (Periodos)")
    plt.ylabel("Poblacion")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("grafica_comparativa_modelos.png")
    print("\nGrafica guardada exitosamente como 'grafica_comparativa_modelos.png'.")
    plt.show()


if __name__ == "__main__":
    ejecutar()