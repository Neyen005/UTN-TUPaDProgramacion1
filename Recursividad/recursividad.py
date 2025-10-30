# UTN - Programación I
# Trabajo Práctico 7: Aplicación de la Recursividad
# -------------------------------------------------------------------

def ejercicio1():
    """
    Función principal para el Ejercicio 1: Factorial.
    Pide un número y muestra los factoriales desde 1 hasta ese número.
    """
    print("\n--- Ejercicio 1: Factorial ---")

    def factorial(n):
        """Calcula el factorial de n recursivamente."""
        # Caso Base: factorial de 0 o 1 es 1.
        if n == 0 or n == 1:
            return 1
        # Paso Recursivo: n * factorial(n-1)
        else:
            return n * factorial(n - 1)

    # Validación de entrada
    while True:
        numero_str = input("Ingresá un número entero (0 o mayor): ")
        if numero_str.isdigit():
            numero = int(numero_str)
            break # El número es válido, salimos del bucle
        else:
            print("Error: Debés ingresar un número entero positivo.")

    print(f"Calculando factoriales desde 1 hasta {numero}:")
    for i in range(1, numero + 1):
        print(f"Factorial de {i}! = {factorial(i)}")


def ejercicio2():
    """
    Función principal para el Ejercicio 2: Fibonacci.
    Pide una posición y muestra la serie de Fibonacci hasta esa posición.
    """
    print("\n--- Ejercicio 2: Fibonacci ---")

    def fibonacci(n):
        """Calcula el valor de Fibonacci en la posición n recursivamente."""
        # Caso Base 1: fib(0) = 0
        if n == 0:
            return 0
        # Caso Base 2: fib(1) = 1
        elif n == 1:
            return 1
        # Paso Recursivo: fib(n-1) + fib(n-2)
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    # Validación de entrada
    while True:
        posicion_str = input("Ingresá la posición de Fibonacci que querés ver (0 o mayor): ")
        if posicion_str.isdigit():
            posicion = int(posicion_str)
            break # El número es válido, salimos del bucle
        else:
            print("Error: Debés ingresar un número entero positivo.")
            
    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"fib({i}) = {fibonacci(i)}")


def ejercicio3():
    """
    Función principal para el Ejercicio 3: Potencia.
    Pide una base y un exponente y calcula la potencia.
    """
    print("\n--- Ejercicio 3: Potencia ---")

    def potencia(base, exponente):
        """Calcula la potencia recursivamente usando n * n^(m-1)."""
        # Caso Base: n^0 = 1
        if exponente == 0:
            return 1
        # Paso Recursivo: base * potencia(base, exponente - 1)
        else:
            return base * potencia(base, exponente - 1)

    # Función interna para validar si es entero (positivo o negativo)
    def es_entero(cadena):
        if cadena.startswith('-'):
            return cadena[1:].isdigit() # Verifica si lo que sigue al '-' son dígitos
        return cadena.isdigit()

    # Validación de la base (puede ser negativa)
    while True:
        base_str = input("Ingresá el número base (puede ser negativo): ")
        if es_entero(base_str):
            base = int(base_str)
            break
        else:
            print("Error: Debés ingresar un número entero.")

    # Validación del exponente (debe ser 0 o mayor)
    while True:
        exponente_str = input("Ingresá el exponente (0 o mayor): ")
        if exponente_str.isdigit():
            exponente = int(exponente_str)
            break
        else:
            print("Error: Debés ingresar un número entero positivo (0 o mayor).")
        
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es = {resultado}")


def ejercicio4():
    """
    Función principal para el Ejercicio 4: Decimal a Binario.
    Pide un número decimal y lo convierte a binario.
    """
    print("\n--- Ejercicio 4: Decimal a Binario ---")

    def decimal_a_binario(n):
        """Convierte un número decimal a binario recursivamente."""
        # Caso Base: Si n es 0 o 1, su binario es el mismo número.
        if n < 2:
            return str(n)
        # Paso Recursivo: 
        # Llama a la función con el cociente (n // 2)
        # y concatena el resto (n % 2) al final.
        else:
            return decimal_a_binario(n // 2) + str(n % 2)

    # Validación de entrada
    while True:
        numero_str = input("Ingresá un número entero (0 o mayor) para convertir: ")
        if numero_str.isdigit():
            numero = int(numero_str)
            break
        else:
            print("Error: Debés ingresar un número entero positivo.")
            
    resultado = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {resultado}")


def ejercicio5():
    """
    Función principal para el Ejercicio 5: Palíndromo.
    Pide una palabra y verifica si es un palíndromo.
    """
    print("\n--- Ejercicio 5: Palíndromo ---")

    def es_palindromo(palabra):
        """Verifica si una palabra es palíndromo recursivamente."""
        # Pre-procesamiento: quitar espacios y pasar a minúsculas
        palabra = palabra.replace(" ", "").lower()
        
        # Caso Base: Si la palabra tiene 0 o 1 letra, es palíndromo.
        if len(palabra) <= 1:
            return True
        # Paso Recursivo:
        # Compara la primera y la última letra.
        # Si son iguales, llama recursivamente a la sub-cadena del medio.
        else:
            return (palabra[0] == palabra[-1]) and es_palindromo(palabra[1:-1])

    palabra_usuario = input("Ingresá una palabra (sin tildes): ")
    if es_palindromo(palabra_usuario):
        print(f'"{palabra_usuario}" SÍ es un palíndromo.')
    else:
        print(f'"{palabra_usuario}" NO es un palíndromo.')


def ejercicio6():
    """
    Función principal para el Ejercicio 6: Suma de Dígitos.
    Pide un número y suma sus dígitos.
    """
    print("\n--- Ejercicio 6: Suma de Dígitos ---")

    def suma_digitos(n):
        """Suma los dígitos de n recursivamente usando % y //."""
        # Caso Base: Si n tiene un solo dígito, la suma es n.
        if n < 10:
            return n
        # Paso Recursivo:
        # Suma el último dígito (n % 10)
        # con la suma recursiva del resto del número (n // 10).
        else:
            return (n % 10) + suma_digitos(n // 10)

    # Validación de entrada
    while True:
        numero_str = input("Ingresá un número entero (0 o mayor): ")
        if numero_str.isdigit():
            numero = int(numero_str)
            break
        else:
            print("Error: Debés ingresar un número entero positivo.")

    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")


def ejercicio7():
    """
    Función principal para el Ejercicio 7: Pirámide de Bloques.
    Calcula el total de bloques en una pirámide.
    """
    print("\n--- Ejercicio 7: Pirámide de Bloques ---")

    def contar_bloques(n):
        """Calcula el total de bloques en una pirámide de base n."""
        # Caso Base: Si la base es 1, solo hay 1 bloque.
        if n == 1:
            return 1
        # Paso Recursivo: 
        # Los bloques de la base (n) + el total de una pirámide de base (n-1).
        else:
            return n + contar_bloques(n - 1)

    # Validación de entrada (debe ser 1 o mayor)
    while True:
        base_str = input("Ingresá el número de bloques en la base (n >= 1): ")
        if base_str.isdigit():
            base = int(base_str)
            if base > 0:
                break # El número es válido y positivo
            else:
                print("Error: El número debe ser 1 o mayor.")
        else:
            print("Error: Debés ingresar un número entero.")

    resultado = contar_bloques(base)
    print(f"Una pirámide con base {base} tiene un total de {resultado} bloques.")


def ejercicio8():
    """
    Función principal para el Ejercicio 8: Contar Dígito.
    Cuenta cuántas veces aparece un dígito en un número.
    """
    print("\n--- Ejercicio 8: Contar Dígito ---")

    def contar_digito(numero, digito):
        """Cuenta las apariciones de 'digito' en 'numero' recursivamente."""
        
        # Caso Base: Si el número es 0 (o se quedó sin dígitos), no hay más apariciones.
        if numero == 0:
            return 0
        
        # Paso Recursivo:
        # Si el último dígito coincide, sumamos 1 al resultado recursivo
        if (numero % 10) == digito:
            return 1 + contar_digito(numero // 10, digito)
        # Si no coincide, solo devolvemos el resultado recursivo
        else:
            return contar_digito(numero // 10, digito)

    # Validación del número (0 o mayor)
    while True:
        numero_largo_str = input("Ingresá el número entero (0 o mayor): ")
        if numero_largo_str.isdigit():
            numero_largo = int(numero_largo_str)
            break
        else:
            print("Error: Debés ingresar un número entero positivo.")

    # Validación del dígito (0-9)
    while True:
        digito_buscado_str = input("Ingresá el dígito (0-9) que querés contar: ")
        # Verificamos que sea dígito Y que sea un solo caracter
        if digito_buscado_str.isdigit() and len(digito_buscado_str) == 1:
            digito_buscado = int(digito_buscado_str)
            break
        else:
            print("Error: Debés ingresar un *único* dígito (del 0 al 9).")

    # Caso especial: si el número es 0 y se busca el 0
    if numero_largo == 0 and digito_buscado == 0:
        resultado = 1
    else:
        resultado = contar_digito(numero_largo, digito_buscado)
    
    print(f'El dígito {digito_buscado} aparece {resultado} veces en {numero_largo}.')


def mostrar_menu():
    """Imprime el menú de opciones."""
    print("\n===========================================")
    print("  TRABAJO PRÁCTICO 7: RECURSIVIDAD")
    print("===========================================")
    print("1. Ejercicio 1: Factorial")
    print("2. Ejercicio 2: Fibonacci")
    print("3. Ejercicio 3: Potencia")
    print("4. Ejercicio 4: Decimal a Binario")
    print("5. Ejercicio 5: Palíndromo")
    print("6. Ejercicio 6: Suma de Dígitos")
    print("7. Ejercicio 7: Pirámide de Bloques")
    print("8. Ejercicio 8: Contar Dígito")
    print("9. Salir")
    print("-------------------------------------------")


def main():
    """Función principal que ejecuta el menú."""
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción (1-9): ")
        
        # Validamos la opción del menú
        if not opcion.isdigit() or not ('1' <= opcion <= '9'):
            print("Opción no válida. Por favor, intentá de nuevo.")
            input("\n...Presioná Enter para volver al menú...")
            continue # Vuelve al inicio del bucle while

        # Si la opción es válida, continuamos
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
            print("Saliendo del programa...")
            break
        
        input("\n...Presioná Enter para volver al menú...")

# -------------------------------------------------------------------
# Ejecución del programa principal
# -------------------------------------------------------------------
if __name__ == "__main__":
    main()
            
            
