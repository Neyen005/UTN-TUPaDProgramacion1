# 1.
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamada a la función
imprimir_hola_mundo()

# 2.
def saludar_usuario(nombre):
    saludo = f"Hola {nombre}!"
    return saludo

# Programa principal
nombre_usuario = input("Ingresa tu nombre: ")
mensaje_final = saludar_usuario(nombre_usuario)
print(mensaje_final)

# 3.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nom = input("Nombre: ")
ape = input("Apellido: ")
edad = input("Edad: ")
res = input("Residencia: ")

informacion_personal(nom, ape, edad, res)

# 4.
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
try:
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    
    print(f"Área: {area:.2f} unidades cuadradas")
    print(f"Perímetro: {perimetro:.2f} unidades")
except ValueError:
    print("Error: Ingresa un número válido para el radio.")

# 5.
def segundos_a_horas(segundos):
    # 1 hora = 3600 segundos
    horas = segundos / 3600
    return horas

# Programa principal
try:
    seg = float(input("Ingresa la cantidad de segundos: "))
    resultado_horas = segundos_a_horas(seg)
    print(f"{seg:.0f} segundos equivalen a {resultado_horas:.3f} horas.")
except ValueError:
    print("Error: Ingresa solo números.")

# 6.
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
try:
    num = int(input("Ingresa el número para ver su tabla: "))
    tabla_multiplicar(num)
except ValueError:
    print("Error: Ingresa un número entero válido.")

# 7.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (División por cero)"
        
    return (suma, resta, multiplicacion, division)

# Programa principal
try:
    num1 = float(input("Ingresa el primer número (a): "))
    num2 = float(input("Ingresa el segundo número (b): "))

    # Desempaqueta la tupla
    s, r, m, d = operaciones_basicas(num1, num2)
    
    print("\n--- Resultados ---")
    print(f"Suma: {s}")
    print(f"Resta: {r}")
    print(f"Multiplicación: {m}")
    print(f"División: {d}")
except ValueError:
    print("Error: Ingresa solo números válidos.")

# 8.
def calcular_imc(peso, altura):
    if altura > 0:
        imc = peso / (altura ** 2)
        return imc
    else:
        return "Error: Altura debe ser mayor a cero"

# Programa principal
try:
    p = float(input("Ingresa tu peso en kg: "))
    a = float(input("Ingresa tu altura en metros: "))
    
    resultado_imc = calcular_imc(p, a)
    
    if isinstance(resultado_imc, (float, int)):
        print(f"Tu Índice de Masa Corporal (IMC) es: {resultado_imc:.2f}")
    else:
        print(resultado_imc)
except ValueError:
    print("Error: Asegúrate de ingresar números válidos.")

# 9.
def celsius_a_fahrenheit(celsius):
    # Fórmula: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Programa principal
try:
    temp_c = float(input("Ingresa la temperatura en Celsius: "))
    temp_f = celsius_a_fahrenheit(temp_c)
    print(f"{temp_c:.1f}°C equivalen a {temp_f:.1f}°F.")
except ValueError:
    print("Error: Ingresa un número para la temperatura.")

# 10.
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# Programa principal
try:
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    n3 = float(input("Ingresa el tercer número: "))
    
    resultado_promedio = calcular_promedio(n1, n2, n3)
    print(f"El promedio de los tres números es: {resultado_promedio:.2f}")
except ValueError:
    print("Error: Ingresa solo números válidos.")