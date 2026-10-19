import matplotlib.pyplot as plt
import modelo

# 1. Ejecutamos el modelo original de la guia (0.5H + 0.3N + 0.2Tf)
print("\n=== TABLA 1: MODELO ORIGINAL ===")
indices_original = modelo.calcular_tabla(0.5, 0.3, 0.2)

# 2. Ejecutamos el modelo ajustado (0.4H + 0.4N + 0.2Tf)
print("\n=== TABLA 2: MODELO AJUSTADO ===")
indices_ajustado = modelo.calcular_tabla(0.4, 0.4, 0.2)

# 3. Graficamos los dos resultados para compararlos
plt.plot(modelo.horas, indices_original, marker='o', label="Modelo Original (0.5, 0.3, 0.2)")
plt.plot(modelo.horas, indices_ajustado, marker='s', label="Modelo Ajustado (0.4, 0.4, 0.2)")

# Linea guia a partir de 0.75 donde ya se considera Lluvia
plt.axhline(0.75, color='red', linestyle='--', label="Limite Lluvia (0.75)")

plt.title("Comparacion del Indice de Lluvia durante el dia")
plt.xlabel("Hora")
plt.ylabel("Indice (I)")
plt.legend()
plt.grid(True)

# Guardamos la imagen para el README y la mostramos
plt.savefig("grafica_lluvia.png")
plt.show()