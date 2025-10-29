# --- Actividad 1: Crear archivo inicial ---
print("Actividad 1: Creando archivo productos.txt...")
# Abrir en modo 'w' (write) para crear o sobrescribir
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,300.0,15\n")
    archivo.write("Goma,80.0,50\n")
print("Archivo productos.txt creado con éxito.")
print("-" * 30)


# --- Actividad 2: Leer y mostrar productos ---
print("Actividad 2: Leyendo y mostrando productos desde productos.txt...")
# Abrir en modo 'r' (read) para leer
with open("productos.txt", "r") as archivo:
    print("Contenido inicial del archivo:")
    for linea in archivo:
        # Limpiar la línea y separarla por comas
        partes = linea.strip().split(',')
        # Asegurarnos de que tenemos 3 partes antes de intentar usarlas
        if len(partes) == 3:
            nombre = partes[0]
            precio = partes[1]
            cantidad = partes[2]
            # Mostrar con el formato pedido
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        else:
            # Informar si una línea no tiene el formato esperado
            print(f"Línea ignorada (formato incorrecto): {linea.strip()}")
print("-" * 30)


# --- Actividad 3: Agregar productos desde teclado ---
print("Actividad 3: Agregando un nuevo producto...")
# Pedir datos al usuario
nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevo_precio = input(f"Ingrese el precio de {nuevo_nombre}: ")
nueva_cantidad = input(f"Ingrese la cantidad de {nuevo_nombre}: ")

# Formatear la línea para guardar
linea_para_guardar = f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n"

# Abrir en modo 'a' (append) para agregar sin borrar
with open("productos.txt", "a") as archivo:
    archivo.write(linea_para_guardar)
print(f"Producto '{nuevo_nombre}' agregado con éxito.")
print("-" * 30)


# --- Actividad 4: Cargar productos en una lista de diccionarios ---
print("Actividad 4: Cargando productos en lista de diccionarios...")
productos_lista = [] # Inicializar la lista vacía
# Abrir en modo 'r' para leer el archivo actualizado
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(',')
        if len(partes) == 3:
            # Intentar convertir precio y cantidad a números, manejar posible error
            try:
                precio_float = float(partes[1])
                cantidad_int = int(partes[2])
                # Crear diccionario para cada producto
                producto_dic = {
                    "nombre": partes[0],
                    "precio": precio_float,
                    "cantidad": cantidad_int
                }
                productos_lista.append(producto_dic) # Agregar diccionario a la lista
            except ValueError:
                # Informar si precio o cantidad no son números válidos en una línea
                print(f"Línea ignorada (precio o cantidad no válidos): {linea.strip()}")
        else:
            print(f"Línea ignorada (formato incorrecto): {linea.strip()}")

print("Productos cargados en la lista:")
# Mostrar la lista de diccionarios (opcional, para verificar)
for p in productos_lista:
    print(p)
print("-" * 30)


# --- Actividad 5: Buscar producto por nombre ---
print("Actividad 5: Buscando un producto por nombre...")
if not productos_lista: # Verificar si la lista no está vacía
     print("No hay productos cargados en la lista para buscar.")
else:
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for producto in productos_lista:
        # Comparar ignorando mayúsculas/minúsculas y espacios extra
        if producto["nombre"].strip().lower() == nombre_buscar.strip().lower():
            print("Producto encontrado:")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']:.2f}") # Formatear precio con 2 decimales
            print(f"  Cantidad: {producto['cantidad']}")
            encontrado = True
            break # Salir del bucle una vez encontrado
    if not encontrado:
        print(f"Producto '{nombre_buscar}' no encontrado en la lista.")
print("-" * 30)


# --- Actividad 6: Guardar los productos actualizados ---
print("Actividad 6: Guardando la lista actualizada en productos.txt...")
if not productos_lista: # Verificar si hay algo que guardar
    print("La lista de productos está vacía, no se guardará nada.")
else:
    # Abrir en modo 'w' para sobrescribir el archivo completo
    with open("productos.txt", "w") as archivo:
        for producto in productos_lista:
            # Formatear cada producto del diccionario a string CSV
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Archivo productos.txt actualizado con la lista de diccionarios.")
print("-" * 30)

print("Fin del programa práctico.")