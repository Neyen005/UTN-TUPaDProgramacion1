
# Práctico 4: Estructuras repetitivas


# Descripción: Resolución de ejercicios con bucles (for y while).

# ---------------------------------------------------------------------------------
# Ejercicio 1: Imprimir números del 0 al 100 en orden creciente.
def ejercicio1():
    print("Ejercicio 1: Números del 0 al 100")
    for i in range(101):
        print(i)
    print("-" * 20)

# Ejercicio 2: Contar la cantidad de dígitos de un número.

def ejercicio2():
    print("Ejercicio 2: Cantidad de dígitos")
    try:
        numero = int(input("Ingrese un número entero: "))
        if numero == 0:
            print("El número tiene 1 dígito.")
        else:
            contador = 0
            # Convertimos el número a positivo para que funcione con negativos
            if numero < 0:
                numero = -numero
            while numero > 0:
                numero = numero // 10
                contador += 1
            print(f"El número tiene {contador} dígitos.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
    print("-" * 20)


# Ejercicio 3: Sumar números entre dos valores (sin incluir los extremos).
def ejercicio3():
    print("Ejercicio 3: Suma entre dos valores")
    try:
        val1 = int(input("Ingrese el primer número: "))
        val2 = int(input("Ingrese el segundo número: "))
        
        # Nos aseguramos de que el primer valor sea el menor
        if val1 > val2:
            val1, val2 = val2, val1
        
        suma = 0
        for i in range(val1 + 1, val2):
            suma += i
        
        print(f"La suma de los números entre {val1} y {val2} es: {suma}")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese números enteros.")
    print("-" * 20)

# Ejercicio 4: Sumar números enteros hasta que el usuario ingrese 0.

def ejercicio4():
    print("Ejercicio 4: Suma hasta ingresar 0")
    suma = 0
    while True:
        try:
            numero = int(input("Ingrese un número (0 para terminar): "))
            if numero == 0:
                break
            suma += numero
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
    print(f"El total acumulado es: {suma}")
    print("-" * 20)

# Ejercicio 5: Adivinar un número aleatorio entre 0 y 9.
import random
def ejercicio5():
    print("Ejercicio 5: Adivina el número")
    numero_secreto = random.randint(0, 9)
    intentos = 0
    while True:
        try:
            adivinanza = int(input("Adivina el número entre 0 y 9: "))
            intentos += 1
            if adivinanza == numero_secreto:
                print(f"¡Adivinaste! El número era {numero_secreto}.")
                print(f"Te tomó {intentos} intentos.")
                break
            else:
                print("Incorrecto, intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    print("-" * 20)

# Ejercicio 6: Imprimir números pares entre 0 y 100 en orden decreciente.
def ejercicio6():
    print("Ejercicio 6: Pares del 100 al 0")
    # range(inicio, fin, paso)
    for i in range(100, -1, -2):
        print(i)
    print("-" * 20)

# Ejercicio 7: Sumar todos los números hasta un entero positivo dado.

def ejercicio7():
    print("Ejercicio 7: Suma hasta un número dado")
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("Por favor, ingrese un número positivo.")
            return
        
        suma = 0
        for i in range(numero + 1):
            suma += i
        
        print(f"La suma de todos los números hasta {numero} es: {suma}")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
    print("-" * 20)

# Ejercicio 8: Contar números pares, impares, positivos y negativos de 100 entradas.

def ejercicio8():
    print("Ejercicio 8: Conteo de números")
    cantidad_numeros = 10  # Para probar más rápido, cambiar a 100 para la versión final
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    
    for i in range(cantidad_numeros):
        try:
            numero = int(input(f"Ingrese el número {i+1} de {cantidad_numeros}: "))
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
            
            if numero > 0:
                positivos += 1
            elif numero < 0:
                negativos += 1
        except ValueError:
            print("Entrada no válida. Se ignorará y se continuará con el siguiente número.")
            continue
    
    print(f"\nResultados del análisis:")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")
    print("-" * 20)

# Ejercicio 9: Calcular la media de 100 números enteros.

def ejercicio9():
    print("Ejercicio 9: Cálculo de la media")
    cantidad_numeros = 10  # Para probar más rápido, cambiar a 100 para la versión final
    suma = 0
    for i in range(cantidad_numeros):
        try:
            numero = int(input(f"Ingrese el número {i+1} de {cantidad_numeros}: "))
            suma += numero
        except ValueError:
            print("Entrada no válida. Se considerará 0.")
            continue
    
    if cantidad_numeros > 0:
        media = suma / cantidad_numeros
        print(f"La media de los números ingresados es: {media}")
    else:
        print("No se ingresaron números.")
    print("-" * 20)

# Ejercicio 10: Invertir los dígitos de un número.
def ejercicio10():
    print("Ejercicio 10: Invertir un número")
    try:
        numero_str = input("Ingrese un número entero: ")
        # Convertimos la cadena a lista, la invertimos y la volvemos a unir
        numero_invertido_str = numero_str[::-1]
        print(f"El número invertido es: {numero_invertido_str}")
    except Exception as e:
        print("Ocurrió un error. Por favor, intente de nuevo con un número válido.")
    print("-" * 20)


# Menú de ejecución

def menu():
    while True:
        print("\n--- Menú de Ejercicios - Práctico 4 ---")
        print("1. Imprimir números del 0 al 100")
        print("2. Contar dígitos de un número")
        print("3. Sumar números entre dos valores")
        print("4. Sumar números hasta ingresar 0")
        print("5. Adivinar un número")
        print("6. Imprimir pares del 100 al 0")
        print("7. Sumar hasta un número dado")
        print("8. Conteo de números (pares, impares, etc.)")
        print("9. Calcular la media de números")
        print("10. Invertir un número")
        print("0. Salir")
        
        opcion = input("Seleccione un ejercicio para ejecutar (0-10): ")
        
        if opcion == '1':
            ejercicio1()
        elif opcion == '2':
            ejercicio2()
        elif opcion == '3':
            ejercicio3()
        elif opcion == '4':
            ejercicio4()
        elif opcion == '5':
            ejercicio5()
        elif opcion == '6':
            ejercicio6()
        elif opcion == '7':
            ejercicio7()
        elif opcion == '8':
            ejercicio8()
        elif opcion == '9':
            ejercicio9()
        elif opcion == '10':
            ejercicio10()
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()