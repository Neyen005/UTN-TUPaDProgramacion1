# Parcial 2 Programación 1
# Importamos el archivo CSV
import csv 
import os
NOMBRE_ARCHIVO = "catalogo.csv"
# Creamos la lista donde guardamos todo
def cargar_catalogo(nombre_del_archivo):
    catalogo_cargado = []
    with open(nombre_del_archivo, 'r') as archivo:
        lector_csv = csv.DictReader(archivo) 
        for fila in lector_csv:
            fila["CANTIDAD"] = int(fila["CANTIDAD"]) 
            catalogo_cargado.append(fila)
    return catalogo_cargado
def guardar_catalogo(nombre_del_archivo, catalogo_a_guardar):
    # Los nombres de las columnas deben coincidir con las claves del diccionario
    columnas = ["TITULO", "CANTIDAD"] 

    # 'newline=""' es necesario al escribir CSVs
    with open(nombre_del_archivo, 'w', newline='') as archivo:
        
        # Creamos el escritor de diccionarios
        escritor_csv = csv.DictWriter(archivo, fieldnames=columnas)
        
        # Escribimos el encabezado (TITULO, CANTIDAD)
        escritor_csv.writeheader() 
        
        # Escribimos todas las filas (la lista de diccionarios)
        escritor_csv.writerows(catalogo_a_guardar)
def mostrar_menu():
    print("\n--- Menú de la Biblioteca ---")
    print("1. Ingresar títulos (múltiples)")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título (individual)")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    
def normalizar_titulo(titulo):
    # Limpia un string de espacios y lo pasa a minúsculas.
    return titulo.strip().lower()

def buscar_libro(catalogo_actual, titulo_buscado):
    #  Normaliza el título que queremos buscar
    titulo_norm_buscado = normalizar_titulo(titulo_buscado)
    
    #  Recorre cada diccionario 'libro' en la lista
    for libro in catalogo_actual:
        #  Normaliza el título del libro actual del catálogo
        titulo_norm_catalogo = normalizar_titulo(libro['TITULO'])
        
        #  Compara las dos versiones normalizadas
        if titulo_norm_buscado == titulo_norm_catalogo:
            #  Si son iguales, devuelve el diccionario COMPLETO
            return libro
            
    #  Si el bucle termina, es que no lo encontró. Devuelve None.
    return None
    # case 1
def ingresar_titulos(catalogo_actual):
    print("\n--- 1. Ingresar Títulos Múltiples ---")
    
    # Preguntar y validar cuántos libros
    while True:
        cantidad_str = input("¿Cuántos libros querés ingresar? ")
        if cantidad_str.isdigit() and int(cantidad_str) > 0:
            cantidad_a_ingresar = int(cantidad_str)
            break
        else:
            print("Error: Ingresá un número entero positivo.")
            
    #  Bucle FOR para cada libro
    for i in range(cantidad_a_ingresar):
        print(f"\n--- Ingresando Libro {i + 1} de {cantidad_a_ingresar} ---")
        
        #  Bucle WHILE para validar el TÍTULO
        while True:
            titulo_ingresado = input("Ingresá el Título: ")
            
            # Validación 1: No vacío
            if normalizar_titulo(titulo_ingresado) == "":
                print("Error: El título no puede estar vacío. Intentá de nuevo.")
                continue # Vuelve a pedir el título
                
            # Validación 2: No duplicado
            libro_existente = buscar_libro(catalogo_actual, titulo_ingresado)
            if libro_existente is not None:
                print("Error: Este título ya existe en el catálogo. Intentá de nuevo.")
                continue # Vuelve a pedir el título
            
            # Si ambas validaciones pasan, salimos del while
            break
            
        #  Bucle WHILE para validar la CANTIDAD
        while True:
            cantidad_str = input(f"Ingresá la cantidad inicial para '{titulo_ingresado}': ")
            if cantidad_str.isdigit():
                cantidad_int = int(cantidad_str)
                break # El número es válido (>= 0 por default con isdigit)
            else:
                print("Error: Ingresá un número entero (0 o mayor).")
                
        # Crear el diccionario y agregarlo
        # Usamos .strip() para guardar el título sin espacios extra al inicio/final
        nuevo_libro = {"TITULO": titulo_ingresado.strip(), "CANTIDAD": cantidad_int}
        catalogo_actual.append(nuevo_libro)
        print(f"¡Libro '{titulo_ingresado.strip()}' agregado al catálogo!")
        
    #  Retornar la lista COMPLETA Y MODIFICADA
    return catalogo_actual 

    # case 2
def ingresar_ejemplares(catalogo_actual):
    print("\n--- 2. Ingresar Ejemplares (Sumar Stock) ---")

    # Comprobar si hay libros en el catálogo
    if not catalogo_actual:
        print("Error: El catálogo está vacío. No podés sumar ejemplares.")
        # Devuelve 'False' para indicar que no hubo cambios
        return catalogo_actual, False

    # Pedir y buscar el título
    titulo_ingresado = input("Ingresá el título del libro al que querés sumar stock: ")
    
    libro_encontrado = buscar_libro(catalogo_actual, titulo_ingresado)

    # Validar si el libro existe
    if libro_encontrado is None:
        print(f"Error: El título '{titulo_ingresado}' no fue encontrado en el catálogo.")
        # Devuelve 'False' para indicar que no hubo cambios
        return catalogo_actual, False
    
    # Si existe, pedir la cantidad a sumar
    print(f"Libro encontrado: {libro_encontrado['TITULO']} (Stock actual: {libro_encontrado['CANTIDAD']})")
    
    while True:
        cantidad_str = input("¿Cuántos ejemplares querés agregar? ")
        if cantidad_str.isdigit():
            cantidad_a_sumar = int(cantidad_str)
            break
        else:
            print("Error: Ingresá un número entero (0 o mayor).")
            
    # Actualizar el stock
    libro_encontrado['CANTIDAD'] += cantidad_a_sumar
    
    print(f"¡Stock actualizado! Nuevo stock de '{libro_encontrado['TITULO']}': {libro_encontrado['CANTIDAD']}")
    
    # Devuelve 'True' para indicar que SÍ hubo cambios
    return catalogo_actual, True 

    # case 3
def mostrar_catalogo(catalogo_actual):
    print("\n--- Mostrando Catálogo Completo ---")
    
    #  Verificar si el catálogo está vacío
    if not catalogo_actual:
        print("El catálogo está vacío. No hay libros para mostrar.")
    else:
        #  Si no está vacío, recorrerlo e imprimir cada libro
        for libro in catalogo_actual:
            # Accedemos a los valores usando las claves del diccionario
            print(f"Título: {libro['TITULO']} | Stock: {libro['CANTIDAD']}")
            
        print(f"\nTotal de títulos en el catálogo: {len(catalogo_actual)}")

    # case 4
def consultar_disponibilidad(catalogo_actual):
    print("\n--- 4. Consultar Disponibilidad de Título ---")

    #  Verificar si hay libros en el catálogo
    if not catalogo_actual:
        print("Error: El catálogo está vacío. No podés consultar.")
        return # Termina la función aquí

    #  Pedir y buscar el título
    titulo_ingresado = input("Ingresá el título del libro que querés consultar: ")
    
    libro_encontrado = buscar_libro(catalogo_actual, titulo_ingresado)

    #  Informar el resultado
    if libro_encontrado is None:
        print(f"Error: El título '{titulo_ingresado}' no fue encontrado en el catálogo.")
    else:
        # Mostrar la cantidad
        titulo_real = libro_encontrado['TITULO']
        cantidad_real = libro_encontrado['CANTIDAD']
        print(f"¡Libro encontrado! Hay {cantidad_real} ejemplares disponibles de '{titulo_real}'.")

    # case 5
def listar_agotados(catalogo_actual):
    print("\n--- 5. Listar Libros Agotados ---")

    # Verificar si hay libros en el catálogo
    if not catalogo_actual:
        print("Error: El catálogo está vacío.")
        return # Termina la función aquí

    # Usamos una variable "bandera" para saber si encontramos alguno
    se_encontraron_agotados = False
    
    # Recorremos la lista buscando libros con stock 0
    for libro in catalogo_actual:
        if libro['CANTIDAD'] == 0:
            print(f"- {libro['TITULO']}")
            se_encontraron_agotados = True # Marcamos que encontramos al menos uno
            
    # Si la bandera nunca cambió, es que no había agotados
    if not se_encontraron_agotados:
        print("¡Buenas noticias! No hay libros agotados en el catálogo.")

    # case 6
def agregar_titulo(catalogo_actual):
    print("\n--- 6. Agregar Título Individual ---")
    
    # Bucle de validación para el TÍTULO
    while True:
        titulo_ingresado = input("Ingresá el Título del nuevo libro: ")
        
        # Chequea que no esté vacío
        if normalizar_titulo(titulo_ingresado) == "":
            print("Error: El título no puede estar vacío. Intentá de nuevo.")
            continue 
            
        # Chequea que no sea duplicado
        if buscar_libro(catalogo_actual, titulo_ingresado) is not None:
            print("Error: Este título ya existe en el catálogo. Intentá de nuevo.")
            continue 
        
        break
        
    # Bucle de validación para la CANTIDAD
    while True:
        cantidad_str = input(f"Ingresá la cantidad inicial para '{titulo_ingresado}': ")
        
        if cantidad_str.isdigit():
            cantidad_int = int(cantidad_str)
            break
        else:
            print("Error: Ingresá un número entero (0 o mayor).")
    
    # Crea el nuevo diccionario
    nuevo_libro = {"TITULO": titulo_ingresado.strip(), "CANTIDAD": cantidad_int}
    
    # Lo agrega a la lista
    catalogo_actual.append(nuevo_libro)
    
    print(f"¡Libro '{titulo_ingresado.strip()}' agregado al catálogo!")
    
    # Devuelve la lista modificada
    return catalogo_actual

    # case 7
def actualizar_ejemplares(catalogo_actual):
    print("\n--- 7. Actualizar Ejemplares (Préstamo/Devolución) ---")

    #  Verificar si hay libros en el catálogo
    if not catalogo_actual:
        print("Error: El catálogo está vacío.")
        return catalogo_actual, False  
    # Pedir y buscar el título
    titulo_ingresado = input("Ingresá el título del libro que querés actualizar: ")
    libro_encontrado = buscar_libro(catalogo_actual, titulo_ingresado)
    # Validar si el libro exist
    if libro_encontrado is None:
        print(f"Error: El título '{titulo_ingresado}' no fue encontrado.")
        return catalogo_actual, False  
    
    
    
    while True:
        accion = input("¿Qué operación querés hacer? [p = préstamo / d = devolución]: ").lower()
    # Lógica para Préstamo
        if accion == 'p':
            if libro_encontrado['CANTIDAD'] > 0:
                libro_encontrado['CANTIDAD'] -= 1
                print(f"¡Préstamo registrado! Nuevo stock: {libro_encontrado['CANTIDAD']}")
                # Esta fue una operación exitosa
                return catalogo_actual, True 
            else:
                print("Error: No hay stock disponible para realizar un préstamo.")
                # Esto fue un error (no se hizo cambio)
                return catalogo_actual, False 
    # Lógica para Devolución
            
        elif accion == 'd':
            libro_encontrado['CANTIDAD'] += 1
            print(f"¡Devolución registrada! Nuevo stock: {libro_encontrado['CANTIDAD']}")
            # Esta fue una operación exitosa
            return catalogo_actual, True 
    # Error si no es 'p' ni 'd'    
        else:
            print("Error: Opción no válida. Ingresá 'p' o 'd'.")
            # (El bucle while se repite)

    # Devolver la lista modificada
    

# --- INICIO DEL PROGRAMA ---

#  la variable principal
catalogo = [] 

# la comprobación
if os.path.exists(NOMBRE_ARCHIVO):
    print("El archivo existe. Cargando datos...")
    
    
    catalogo = cargar_catalogo(NOMBRE_ARCHIVO) 
else:
    print("El archivo no existe. Empezando con un catálogo vacío.")




#  Bucle principal del menú
while True:
    mostrar_menu()
    opcion = input("Seleccioná una opción: ")

    match opcion:
        case '1':
            # 1. Llama a la función y "atrapa" la lista modificada
            catalogo = ingresar_titulos(catalogo) 
            # 2. Como se modificó, guardamos en el CSV
            guardar_catalogo(NOMBRE_ARCHIVO, catalogo)
            print("¡Títulos ingresados y guardados!")

        case '2':
            # Atrapa los dos valores que devuelve la función
            catalogo, se_hizo_un_cambio = ingresar_ejemplares(catalogo)
            
            # Solo guarda y muestra el éxito SI el indicador es True
            if se_hizo_un_cambio:
                guardar_catalogo(NOMBRE_ARCHIVO, catalogo)
                print("¡Ejemplares actualizados y guardados!")
            
        case '3':
            # Esta función "solo lee", no modifica nada.
            # No necesita return ni guardar.
            mostrar_catalogo(catalogo)
            
        case '4':
            consultar_disponibilidad(catalogo)
            
        case '5':
            listar_agotados(catalogo)
            
        case '6':
            catalogo = agregar_titulo(catalogo)
            guardar_catalogo(NOMBRE_ARCHIVO, catalogo)
            print("¡Título agregado y guardado!")
            
        case '7':
            catalogo, se_hizo_un_cambio = actualizar_ejemplares(catalogo)
            
            # Solo guarda y muestra el éxito SI el indicador es True
            if se_hizo_un_cambio:
                guardar_catalogo(NOMBRE_ARCHIVO, catalogo)
                print("¡Préstamo/devolución registrado y guardado!")
            
        case '8':
            print("Saliendo del sistema. ¡Adiós!")
            break
            
        case _:
            print("Error: Opción no válida. Intentá de nuevo.")
    
    # Una pequeña "pausa" para que el usuario pueda leer el resultado
    input("\n...Presioná Enter para continuar...")