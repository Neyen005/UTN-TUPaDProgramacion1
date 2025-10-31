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

def mostrar_catalogo(catalogo_actual):
    print("\n--- Mostrando Catálogo Completo ---")
    
    # 1. Verificar si el catálogo está vacío
    if not catalogo_actual:
        print("El catálogo está vacío. No hay libros para mostrar.")
    else:
        # 2. Si no está vacío, recorrerlo e imprimir cada libro
        for libro in catalogo_actual:
            # Accedemos a los valores usando las claves del diccionario
            print(f"Título: {libro['TITULO']} | Stock: {libro['CANTIDAD']}")
            
        print(f"\nTotal de títulos en el catálogo: {len(catalogo_actual)}")

# --- INICIO DEL PROGRAMA ---

#  la variable principal
catalogo = [] 

# la comprobación
if os.path.exists(NOMBRE_ARCHIVO):
    print("El archivo existe. Cargando datos...")
    
    
    catalogo = cargar_catalogo(NOMBRE_ARCHIVO) 
else:
    print("El archivo no existe. Empezando con un catálogo vacío.")

print("Catálogo listo:", catalogo) 
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
            catalogo = ingresar_ejemplares(catalogo)
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
            catalogo = actualizar_ejemplares(catalogo)
            guardar_catalogo(NOMBRE_ARCHIVO, catalogo)
            print("¡Préstamo/devolución registrado y guardado!")
            
        case '8':
            print("Saliendo del sistema. ¡Adiós!")
            break
            
        case _:
            print("Error: Opción no válida. Intentá de nuevo.")
    
    # Una pequeña "pausa" para que el usuario pueda leer el resultado
    input("\n...Presioná Enter para continuar...")