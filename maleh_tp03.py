# Ejercicio 1: Mayor de edad
edad = int(input("Por favor, ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
    
# Ejercicio 2: Aprobado o desaprobado
nota = int(input("Por favor, ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3: Número par
numero = int(input("Por favor, ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4: Categoría por edad
edad = int(input("Por favor, ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5: Longitud de la contraseña
contrasena = input("Por favor, ingrese una contraseña: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6: Sesgo estadístico
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

# Ejercicio 7: Frase con vocal
frase = input("Por favor, ingrese una frase o palabra: ")
# Chequea si el último caracter es una vocal
ultima_letra = frase[-1].lower()
if ultima_letra == 'a' or ultima_letra == 'e' or ultima_letra == 'i' or ultima_letra == 'o' or ultima_letra == 'u':
    print(frase + "!")
else:
    print(frase)

# Ejercicio 8: Formato de nombre
nombre = input("Por favor, ingrese su nombre: ")
opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para la primera letra mayúscula: ")
if opcion == '1':
    print(nombre.upper())
elif opcion == '2':
    print(nombre.lower())
elif opcion == '3':
    print(nombre.title())
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

# Ejercicio 9: Escala de Richter
magnitud = float(input("Por favor, ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else: # En caso de que sea mayor o igual a 7
    print("Extremo (puede causar graves daños a gran escala)")

# Ejercicio 10: Estaciones del año
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = input("¿Qué mes del año es?: ").lower()
dia = int(input("¿Qué día del mes es?: "))
if hemisferio == 'N':
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 20):
        print("Usted se encuentra en Invierno")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20):
        print("Usted se encuentra en Primavera")
    elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print("Usted se encuentra en Verano")
    else:
        print("Usted se encuentra en Otoño")
elif hemisferio == 'S':
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 20):
        print("Usted se encuentra en Verano")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20):
        print("Usted se encuentra en Otoño")
    elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print("Usted se encuentra en Invierno")
    else:
        print("Usted se encuentra en Primavera")
else:
    print("Error: Hemisferio no válido.")
