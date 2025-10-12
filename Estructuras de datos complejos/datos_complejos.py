# Diccionario inicial 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# 1) Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200, Manzana = 1500, Pera = 2300
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("--- Actividad 1 ---")
print("Diccionario después de añadir:", precios_frutas)

# Diccionario resultante de la Actividad 1
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# 2) Actualizar los precios:
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\n--- Actividad 2 ---")
print("Diccionario después de actualizar:", precios_frutas)

# 3) Crear una lista que contenga únicamente las frutas (claves) 
lista_frutas = list(precios_frutas.keys())

print("\n--- Actividad 3 ---")
print("Lista de frutas:", lista_frutas)

# 4) Almacenar y consultar números telefónicos 
contactos = {} # Diccionario vacío para los contactos 
NUM_CONTACTOS = 5

print("\n--- Actividad 4: Carga de contactos ---")
# Cargar 5 contactos 
for i in range(NUM_CONTACTOS):
    print(f"Ingresa el contacto {i + 1} de {NUM_CONTACTOS}:")
    nombre = input("Nombre (clave): ")
    numero = input("Número (valor): ")
    contactos[nombre] = numero

print("\n--- Actividad 4: Consulta de número ---")
# Pedir un nombre y mostrar el número asociado 
nombre_a_consultar = input("Ingresa el nombre del contacto a consultar: ")

if nombre_a_consultar in contactos:
    numero_encontrado = contactos[nombre_a_consultar]
    print(f"El número de {nombre_a_consultar} es: {numero_encontrado}")
else:
    print(f"El contacto '{nombre_a_consultar}' no existe en la agenda.")

    # 5) Análisis de frase
print("\n--- Actividad 5 ---")
frase = input("Ingresa una frase: ").lower() # Convertir a minúsculas para un conteo uniforme
palabras = frase.split() # Separa la frase en una lista de palabras

# a) Palabras únicas (usando un set) 
palabras_unicas = set(palabras)

# b) Diccionario con la cantidad de veces que aparece cada palabra 
recuento = {}
for palabra in palabras:
    # Si la palabra ya está en el diccionario, incrementa el contador
    if palabra in recuento:
        recuento[palabra] += 1
    # Si no está, la añade con un contador inicial de 1
    else:
        recuento[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)


# 6) Promedio de notas de alumnos
alumnos = {}
NUM_ALUMNOS = 3
NUM_NOTAS = 3

print("\n--- Actividad 6: Carga de alumnos y notas ---")
for i in range(NUM_ALUMNOS):
    nombre = input(f"Ingresa el nombre del alumno {i + 1}: ")
    notas = []
    print(f"Ingresa las {NUM_NOTAS} notas para {nombre}:")
    for j in range(NUM_NOTAS):
        
        nota = float(input(f"  Nota {j + 1}: ")) 
        notas.append(nota)
            
    # La tupla de notas es el valor del diccionario
    alumnos[nombre] = tuple(notas)

print("\n--- Actividad 6: Promedios ---")
for nombre, notas_tupla in alumnos.items():
    promedio = sum(notas_tupla) / len(notas_tupla)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

    # 7) Operaciones con Sets de estudiantes 
parcial_1 = {101, 105, 110, 115, 120, 125, 130} # Estudiantes que aprobaron Parcial 1
parcial_2 = {105, 115, 130, 135, 140, 145}     # Estudiantes que aprobaron Parcial 2

print("\n--- Actividad 7: Sets de estudiantes ---")
print("P1:", parcial_1)
print("P2:", parcial_2)

# a) Los que aprobaron ambos parciales (Intersección) 
ambos_aprobados = parcial_1.intersection(parcial_2)
print("Aprobaron AMBOS parciales:", ambos_aprobados)

# b) Los que aprobaron solo uno de los dos (Diferencia Simétrica) 
solo_uno = parcial_1.symmetric_difference(parcial_2)
print("Aprobaron SOLO UNO de los dos:", solo_uno)

# c) La lista total de estudiantes que aprobaron al menos un parcial (Unión, sin repetir) 
total_aprobados = parcial_1.union(parcial_2)
print("TOTAL de estudiantes que aprobaron al menos uno:", total_aprobados)



# 9) Agenda con clave de Tupla 
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:30"): "Entrenamiento",
    ("viernes", "18:00"): "Cena con clientes"
}

print("\n--- Actividad 9: Agenda (Clave: Tupla) ---")

# Pedir al usuario el día y la hora 
dia_consulta = input("Ingresa el día (ej. lunes): ").lower()
hora_consulta = input("Ingresa la hora (ej. 10:00): ")

clave_consulta = (dia_consulta, hora_consulta)

# Consultar actividad 
if clave_consulta in agenda:
    evento = agenda[clave_consulta]
    print(f"El evento programado para el {dia_consulta} a las {hora_consulta} es: '{evento}'")
else:
    print(f"No hay actividades programadas para el {dia_consulta} a las {hora_consulta}.")

# 10) Invertir Diccionario 
original = {
    "Argentina": "Buenos Aires", 
    "Chile": "Santiago", 
    "Perú": "Lima",
    "Uruguay": "Montevideo"
}

# Construir el nuevo diccionario invirtiendo clave y valor 
invertido = {}
# Iterar sobre las claves (países) y valores (capitales) del diccionario original
for pais, capital in original.items():
    # Asignar la capital como clave y el país como valor en el nuevo diccionario
    invertido[capital] = pais

print("\n--- Actividad 10: Invertir Diccionario ---")
print("Diccionario Original (País: Capital):", original)
print("Diccionario Invertido (Capital: País):", invertido)