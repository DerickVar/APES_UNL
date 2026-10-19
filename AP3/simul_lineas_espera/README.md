# Práctica 3: Simulación de Líneas de Espera (Sistema de Colas M/M/1)

## 1. Descripción del proyecto
* **Propósito:** Evaluar y contrastar el comportamiento dinámico de un sistema de líneas de espera mono-servidor (M/M/1) mediante la formulación analítica de estado estacionario frente a una simulación de eventos discretos estocástica implementada con la librería SimPy.
* **Problema resuelto:** Permite predecir y dimensionar la congestión, longitud de la cola y tiempos de espera de los usuarios en función de la tasa de llegadas ($\lambda$) y la tasa de atención ($\mu$), comprobando computacionalmente la condición de estabilidad ($\rho < 1$) para evitar la saturación y colapso del servicio.

## 2. Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Librerías principales:**
  * `SimPy`: Motor de simulación para modelar procesos basados en eventos discretos y recursos compartidos.
  * `NumPy`: Cálculos matemáticos vectorizados y generación de tiempos aleatorios con distribución exponencial.
  * `Matplotlib`: Construcción, renderizado y guardado de gráficas estadísticas y comparativas (.png).
  * `Pandas`: Tabulación, resumen y manipulación estructurada de métricas de desempeño.

## 3. Instalación
Pasos para preparar y configurar el entorno de trabajo:

```bash
# 1. Ingresar a la carpeta de la simulación
cd APES_UNL/AP3/simul_lineas_espera

# 2. Instalar los paquetes requeridos dentro del entorno virtual
pip install -r requirements.txt