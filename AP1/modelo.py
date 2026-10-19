# Datos de entrada que da la guia
horas = ["06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]
humedad = [65, 70, 68, 60, 75, 85, 92, 88, 80]
nubosidad = [40, 50, 45, 30, 70, 85, 95, 90, 75]
temperatura = [14, 16, 18, 22, 20, 18, 16, 17, 15]

# Funcion para sacar el factor de temperatura (Tf) segun la tabla
def obtener_tf(temp):
    if temp <= 10:
        return 1.00
    elif temp <= 12:
        return 0.90
    elif temp <= 14:
        return 0.80
    elif temp <= 16:
        return 0.70
    elif temp <= 18:
        return 0.60
    elif temp <= 20:
        return 0.50
    elif temp <= 22:
        return 0.40
    elif temp <= 24:
        return 0.30
    elif temp <= 26:
        return 0.20
    else:
        return 0.10

# Funcion para ver si llueve o no segun el indice I
def obtener_estado(indice):
    if indice < 0.40:
        return "Sin lluvia"
    elif indice < 0.60:
        return "Baja posibilidad"
    elif indice < 0.75:
        return "Lluvia probable"
    else:
        return "Lluvia"

# Funcion que calcula la formula I = peso_h*H + peso_n*N + peso_tf*Tf e imprime la tabla
def calcular_tabla(peso_h, peso_n, peso_tf):
    lista_indices = []
    print("Hora  | Hum | Nub | Temp | H    | N    | Tf   | Indice | Estado")
    print("-" * 68)
    
    for i in range(len(horas)):
        # Normalizamos dividiendo para 100
        H = humedad[i] / 100
        N = nubosidad[i] / 100
        Tf = obtener_tf(temperatura[i])
        
        # Aplicamos la ecuacion del modelo
        I = (peso_h * H) + (peso_n * N) + (peso_tf * Tf)
        lista_indices.append(I)
        estado = obtener_estado(I)
        
        print(f"{horas[i]} | {humedad[i]}  | {nubosidad[i]}  | {temperatura[i]}   | {H:.2f} | {N:.2f} | {Tf:.2f} | {I:.3f}  | {estado}")
        
    return lista_indices