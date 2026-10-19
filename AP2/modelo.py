import numpy as np

def modelo_deterministico(P0, r, tiempo):
    """Calcula el modelo exponencial continuo analitico P(t) = P0 * e^(rt)."""
    t_vector = np.linspace(0, tiempo, 100)
    poblacion = P0 * np.exp(r * t_vector)
    return t_vector, poblacion


def modelo_discreto(P0, r, tiempo):
    """Calcula el modelo discreto paso a paso: P_{t+1} = P_t + r*P_t."""
    t_vector = list(range(tiempo + 1))
    poblacion = [P0]
    for _ in range(1, tiempo + 1):
        p_actual = poblacion[-1]
        incremento = r * p_actual
        poblacion.append(p_actual + incremento)
    return t_vector, poblacion


def modelo_estocastico(P0, r, sigma, tiempo):
    """Calcula el modelo estocastico sumando ruido gaussiano normal(0, sigma)."""
    t_vector = list(range(tiempo + 1))
    poblacion = [P0]
    for _ in range(1, tiempo + 1):
        p_actual = poblacion[-1]
        ruido = np.random.normal(0, sigma)
        nueva_p = p_actual + (r * p_actual) + ruido
        if nueva_p < 0:
            nueva_p = 0
        poblacion.append(nueva_p)
    return t_vector, poblacion


def modelo_continuo_euler(P0, r, tiempo, dt):
    """Aproximacion numerica de Euler: P_{t+dt} = P_t + dt * (r*P_t)."""
    t_vector = np.arange(0, tiempo + dt, dt)
    poblacion = [P0]
    for _ in range(len(t_vector) - 1):
        p_actual = poblacion[-1]
        cambio = r * p_actual
        nueva_p = p_actual + (dt * cambio)
        poblacion.append(nueva_p)
    return t_vector, poblacion