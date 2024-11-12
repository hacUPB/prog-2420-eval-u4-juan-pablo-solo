import os
import csv

# Funciones para el menú de archivos de texto (.txt)
def contar_palabras(archivo):
    with open(archivo, 'r') as f:
        texto = f.read()
        palabras = texto.split()
        print(f"Número de palabras en el archivo: {len(palabras)}")

def reemplazar_palabra(archivo, palabra_a_buscar, palabra_nueva):
    with open(archivo, 'r') as f:
        texto = f.read()
    texto_modificado = texto.replace(palabra_a_buscar, palabra_nueva)
    with open(archivo, 'w') as f:
        f.write(texto_modificado)
    print(f"Reemplazo realizado. '{palabra_a_buscar}' fue cambiado por '{palabra_nueva}'.")

def contar_caracteres(archivo):
    with open(archivo, 'r') as f:
        texto = f.read()
        total_caracteres = len(texto)
        sin_espacios = len(texto.replace(" ", ""))
        print(f"Total de caracteres (incluyendo espacios): {total_caracteres}")
        print(f"Total de caracteres (sin contar espacios): {sin_espacios}")

# Funciones para el menú de archivos CSV (.csv)
def mostrar_primeras_filas(archivo):
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 15:
                break
            print(row)

def calcular_estadisticas(archivo, columna):
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        encabezado = next(reader)
        
        if columna not in encabezado:
            print("Columna no encontrada.")
            return
        
        indice_columna = encabezado.index(columna)
        datos = []
        
        for fila in reader:
            try:
                valor = float(fila[indice_columna])
                datos.append(valor)
            except ValueError:
                continue
        
        if not datos:
            print("No hay datos numéricos en la columna seleccionada.")
            return
        
        n_datos = len(datos)
        promedio = sum(datos) / n_datos
        datos_ordenados = sorted(datos)
        mediana = datos_ordenados[n_datos // 2] if n_datos % 2 != 0 else (datos_ordenados[n_datos // 2 - 1] + datos_ordenados[n_datos // 2]) / 2
        valor_maximo = max(datos)
        valor_minimo = min(datos)
        
        print(f"Número de datos: {n_datos}")
        print(f"Promedio: {promedio}")
        print(f"Mediana: {mediana}")
        print(f"Valor máximo: {valor_maximo}")
        print(f"Valor mínimo: {valor_minimo}")

def graficar_columna(archivo, columna):
    try:
        import turtle  # Usaremos turtle para una representación gráfica básica
    except ImportError:
        print("El módulo turtle no está disponible.")
        return

    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        encabezado = next(reader)
        
        if columna not in encabezado:
            print("Columna no encontrada.")
            return
        
        indice_columna = encabezado.index(columna)
        datos = []
        
        for fila in reader:
            try:
                valor = float(fila[indice_columna])
                datos.append(valor)
            except ValueError:
                continue
    
    if not datos:
        print("No hay datos numéricos en la columna seleccionada.")
        return

    # Configuración del gráfico con turtle
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()

    escala = 400 / max(datos) if max(datos) != 0 else 1

    for i, valor in enumerate(datos):
        x = -200 + (400 / len(datos)) * i
        y = -200 + valor * escala
        turtle.goto(x, y)
    
    turtle.done()

# Menú principal
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Listar archivos")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ruta = input("Ingrese una ruta o presione Enter para usar la actual: ")
            ruta = ruta if ruta else os.getcwd()
            try:
                archivos = os.listdir(ruta)
                print("Archivos en la ruta:")
                for archivo in archivos:
                    print(archivo)
            except FileNotFoundError:
                print("Ruta no válida.")
        
        elif opcion == '2':
            archivo = input("Ingrese el nombre del archivo de texto (.txt): ")
            if not os.path.isfile(archivo) or not archivo.endswith('.txt'):
                print("Archivo no encontrado o no es un archivo de texto.")
                continue

            while True:
                print("\n--- Submenú Archivos de Texto ---")
                print("1. Contar número de palabras")
                print("2. Reemplazar una palabra por otra")
                print("3. Contar el número de caracteres")
                print("4. Volver al menú principal")

                subopcion = input("Seleccione una opción: ")

                if subopcion == '1':
                    contar_palabras(archivo)
                elif subopcion == '2':
                    palabra_a_buscar = input("Ingrese la palabra a buscar: ")
                    palabra_nueva = input("Ingrese la palabra nueva: ")
                    reemplazar_palabra(archivo, palabra_a_buscar, palabra_nueva)
                elif subopcion == '3':
                    contar_caracteres(archivo)
                elif subopcion == '4':
                    break
                else:
                    print("Opción no válida.")
        
        elif opcion == '3':
            archivo = input("Ingrese el nombre del archivo CSV (.csv): ")
            if not os.path.isfile(archivo) or not archivo.endswith('.csv'):
                print("Archivo no encontrado o no es un archivo CSV.")
                continue

            while True:
                print("\n--- Submenú Archivos CSV ---")
                print("1. Mostrar las 15 primeras filas")
                print("2. Calcular Estadísticas")
                print("3. Graficar una columna completa")
                print("4. Volver al menú principal")

                subopcion = input("Seleccione una opción: ")

                if subopcion == '1':
                    mostrar_primeras_filas(archivo)
                elif subopcion == '2':
                    columna = input("Ingrese el nombre de la columna: ")
                    calcular_estadisticas(archivo, columna)
                elif subopcion == '3':
                    columna = input("Ingrese el nombre de la columna: ")
                    graficar_columna(archivo, columna)
                elif subopcion == '4':
                    break
                else:
                    print("Opción no válida.")
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()