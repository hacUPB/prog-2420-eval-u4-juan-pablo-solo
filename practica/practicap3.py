import random

# Definir los parámetros
tiempo_total_horas = 5
intervalo_minutos = 10
num_intervalos = (tiempo_total_horas * 60) // intervalo_minutos

# Función para generar la matriz con valores aleatorios
def generar_datos_vuelo(num_intervalos):
    datos_vuelo = []
    for _ in range(num_intervalos):
        # Generar altitud entre 0 y 12,000 metros
        altitud = random.randint(0, 12000)
        # Generar velocidad entre 200 y 900 km/h
        velocidad = random.randint(200, 900)
        # Añadir el par altitud, velocidad a la lista
        datos_vuelo.append([altitud, velocidad])
    return datos_vuelo

# Generar la matriz de datos de vuelo
datos_vuelo = generar_datos_vuelo(num_intervalos)

# a) Calcular la altitud promedio durante el vuelo
altitudes = [dato[0] for dato in datos_vuelo]
altitud_promedio = sum(altitudes) / len(altitudes)

# b) Determinar el intervalo de tiempo en el que se alcanzó la velocidad máxima
velocidades = [dato[1] for dato in datos_vuelo]
velocidad_maxima = max(velocidades)
intervalo_max_velocidad = velocidades.index(velocidad_maxima)

# Mostrar los resultados
print("Altitud promedio durante el vuelo:", altitud_promedio, "metros")
print("Velocidad máxima alcanzada:", velocidad_maxima, "km/h")
print(f"El intervalo de tiempo en el que se alcanzó la velocidad máxima fue entre los {intervalo_max_velocidad * 10} y {(intervalo_max_velocidad + 1) * 10} minutos.")