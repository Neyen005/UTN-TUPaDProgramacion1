1- print ("Hola Mundo")
2- nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(f"¡Hola {nombre_usuario}!")
3-nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Ahora, ingresa tu apellido: ")
edad = input("¿Qué edad tienes?: ")
lugar_residencia = input("¿Dónde resides?: ")
oracion_completa = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}."
print(oracion_completa)
4-radio = float(input("Por favor, ingresa el radio del círculo: "))
pi = 3.14
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print(f"El área del círculo con radio {radio} es: {area:.2f}")
print(f"El perímetro del círculo con radio {radio} es: {perimetro:.2f}")
5-segundos = int(input("Por favor, ingresa la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")
6-numero = int(input("Por favor, ingresa un número para ver su tabla de multiplicar: "))
print(f"\nTabla de multiplicar del {numero}:")
print("-" * 25)

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

print("-" * 25)
7- num1 = int(input("Por favor, ingresa el primer número entero (distinto de 0): "))
num2 = int(input("Ahora, ingresa el segundo número entero (distinto de 0): "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"\nResultados para los números {num1} y {num2}:")
print("-" * 30)
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division:.2f}") # Formateamos la división a dos decimales
print("-" * 30)
8-peso = float(input("Por favor, ingresa tu peso en kg: "))
altura = float(input("Ahora, ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
9-celsius = float(input("Por favor, ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura de {celsius}°C equivale a {fahrenheit:.2f}°F.")
10-num1 = float(input("Por favor, ingresa el primer número: "))
num2 = float(input("Ahora, ingresa el segundo número: "))
num3 = float(input("Finalmente, ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")
