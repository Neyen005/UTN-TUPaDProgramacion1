# UTN - Práctico 5 Listas

import random

# EJERCICIO 1, 2, 3 - Notas

print("--- Ejercicio 1, 2, 3: Notas de estudiantes ---")
notas_estudiantes = [random.randint(1, 10) for _ in range(10)]
print("Lista completa de notas:")
print(notas_estudiantes)
promedio_notas = sum(notas_estudiantes) / len(notas_estudiantes)
print(f"El promedio de las notas es: {promedio_notas:.2f}")
nota_mas_alta = max(notas_estudiantes)
nota_mas_baja = min(notas_estudiantes)
print(f"La nota más alta es: {nota_mas_alta}")
print(f"La nota más baja es: {nota_mas_baja}")
print("\n")


# EJERCICIO 3 - Productos

print("--- Ejercicio 3: Lista de productos ---")
productos = []
for i in range(5):
    producto = input(f"Ingresa el producto número {i+1}: ")
    productos.append(producto)
productos_ordenados = sorted(productos)
print("Lista de productos ordenada alfabéticamente:")
print(productos_ordenados)
producto_a_eliminar = input("¿Qué producto deseas eliminar de la lista? ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print("Producto eliminado. Lista actualizada:")
    print(productos)
else:
    print(f"'{producto_a_eliminar}' no se encuentra en la lista.")
print("\n")


# EJERCICIO 4 - Pares e Impares

print("--- Ejercicio 4: Pares e impares ---")
numeros_aleatorios = [random.randint(1, 100) for _ in range(15)]
print("Lista original de números:", numeros_aleatorios)
pares = []
impares = []
for numero in numeros_aleatorios:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("Lista de números pares:", pares)
print("Lista de números impares:", impares)
print(f"Cantidad de números pares: {len(pares)}")
print(f"Cantidad de números impares: {len(impares)}")
print("\n")


# EJERCICIO 4 - Sin Repetidos

print("--- Ejercicio 4: Sin repetidos ---")
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
print("Lista original:", datos)
lista_sin_repetidos = []
for elemento in datos:
    if elemento not in lista_sin_repetidos:
        lista_sin_repetidos.append(elemento)
print("Lista sin elementos repetidos:", lista_sin_repetidos)
print("\n")


# EJERCICIO 5 - Gestión de estudiantes

print("--- Ejercicio 5: Gestión de estudiantes ---")
estudiantes = ["Ana", "Pedro", "Sofía", "Juan", "María", "Carlos", "Luisa", "Diego"]
print("Lista de estudiantes original:", estudiantes)
accion = input("¿Quieres 'agregar' o 'eliminar' un estudiante? ").lower()
if accion == "agregar":
    nuevo_estudiante = input("Ingresa el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print("Estudiante agregado. Lista actualizada:")
    print(estudiantes)
elif accion == "eliminar":
    estudiante_a_eliminar = input("Ingresa el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
        print("Estudiante eliminado. Lista actualizada:")
        print(estudiantes)
    else:
        print(f"'{estudiante_a_eliminar}' no se encuentra en la lista.")
else:
    print("Acción no válida.")
print("\n")


# EJERCICIO 6 - Rotar lista

print("--- Ejercicio 6: Rotar lista ---")
numeros = [1, 2, 3, 4, 5, 6, 7]
print("Lista original:", numeros)
ultimo_elemento = numeros.pop()
numeros.insert(0, ultimo_elemento)
print("Lista rotada a la derecha:", numeros)
print("\n")


# EJERCICIO 7 - Matriz de temperaturas

print("--- Ejercicio 7: Matriz de temperaturas ---")
temperaturas = []
for _ in range(7):
    temp_min = random.randint(5, 15)
    temp_max = random.randint(16, 30)
    temperaturas.append([temp_min, temp_max])
print("Matriz de temperaturas (Mínimas, Máximas):")
for dia in temperaturas:
    print(dia)
suma_minimas = 0
suma_maximas = 0
for dia in temperaturas:
    suma_minimas += dia[0]
    suma_maximas += dia[1]
promedio_minimas = suma_minimas / len(temperaturas)
promedio_maximas = suma_maximas / len(temperaturas)
print(f"Promedio de temperaturas mínimas: {promedio_minimas:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maximas:.2f}°C")
mayor_amplitud = 0
dia_mayor_amplitud = 0
for i, dia in enumerate(temperaturas):
    amplitud_termica = dia[1] - dia[0]
    if amplitud_termica > mayor_amplitud:
        mayor_amplitud = amplitud_termica
        dia_mayor_amplitud = i + 1
print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C y se registró en el día {dia_mayor_amplitud}.")
print("\n")


# EJERCICIO 8 - Matriz de notas

print("--- Ejercicio 8: Matriz de notas ---")
notas = []
for _ in range(5):
    estudiante_notas = [random.randint(1, 10) for _ in range(3)]
    notas.append(estudiante_notas)
print("Matriz de notas (filas: estudiantes, columnas: materias):")
for fila in notas:
    print(fila)
print("Promedio de cada estudiante:")
for i, estudiante_notas in enumerate(notas):
    promedio_estudiante = sum(estudiante_notas) / len(estudiante_notas)
    print(f"Estudiante {i+1}: {promedio_estudiante:.2f}")
print("Promedio de cada materia:")
for j in range(len(notas[0])):
    suma_materia = 0
    for i in range(len(notas)):
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / len(notas)
    print(f"Materia {j+1}: {promedio_materia:.2f}")
print("\n")


# EJERCICIO 9 - Ta-Te-Ti

print("--- Ejercicio 9: Ta-Te-Ti ---")
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
def mostrar_tablero(t):
    for fila in t:
        print(" | ".join(fila))
jugador = "X"
for _ in range(9):
    print(f"Turno del jugador '{jugador}'")
    mostrar_tablero(tablero)
    try:
        fila = int(input("Ingresa la fila (0, 1, o 2): "))
        columna = int(input("Ingresa la columna (0, 1, o 2): "))
        if 0 <= fila <= 2 and 0 <= columna <= 2 and tablero[fila][columna] == "-":
            tablero[fila][columna] = jugador
            if jugador == "X":
                jugador = "O"
            else:
                jugador = "X"
        else:
            print("Posición no válida o ya ocupada. Intenta de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")
print("Juego terminado.")
print("\n")

# EJERCICIO 10 - Ventas

print("--- Ejercicio 10: Ventas de la tienda ---")
ventas = []
for _ in range(4):
    ventas_producto = [random.randint(50, 200) for _ in range(7)]
    ventas.append(ventas_producto)
print("Matriz de ventas:")
for fila in ventas:
    print(fila)
print("Total vendido por cada producto:")
for i, producto_ventas in enumerate(ventas):
    total_producto = sum(producto_ventas)
    print(f"Producto {i+1}: {total_producto}")
ventas_por_dia = []
for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][j]
    ventas_por_dia.append(suma_dia)
dia_mayor_venta = ventas_por_dia.index(max(ventas_por_dia)) + 1
print(f"El día con mayores ventas totales fue el día {dia_mayor_venta}.")
total_producto = [sum(ventas_producto) for ventas_producto in ventas]
producto_mas_vendido = total_producto.index(max(total_producto)) + 1
print(f"El producto más vendido en la semana fue el producto {producto_mas_vendido}.")
