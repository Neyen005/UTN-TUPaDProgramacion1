
# Lista de opciones del menú 
elecciones_menu = ["1. Ingresá solo el titulo",
                     "2. Ingresa ejemplares disponibles (sin titulos)",
                     "3. Mostrar catálogo",
                     "4. Consultar disponibilidad de un titulo específico",
                     "5. Listar agotados",
                     "6. Agregar titulos (con ejemplares)",
                     "7. Actualizar ejemplares (prestamos/devolución)",
                     "8. Salir"] 
                     
titulos = []
ejemplares = []

# --- BUCLE PRINCIPAL DEL PROGRAMA (MENÚ PERSISTENTE) ---
while True:
    print ("Menú Librería")
    # Imprime las opciones del menú.
    for opcion in elecciones_menu:
        print (opcion)
    seleccion = input ("Seleccione elección ")
    
    print ("------------------")

    # --- OPCIÓN 1: INGRESAR SOLO TÍTULOS ---
    if seleccion == "1":
        # Valida que la cantidad de títulos a ingresar sea un entero positivo.
        while True:
            cantidad_str = input("¿Cuantos titulos deseas ingresar? ")
            if cantidad_str.isdigit() and int(cantidad_str) > 0:
                cantidad_titulos = int(cantidad_str)
                break
            else:
                print("Por favor ingresá un número entero positivo.")
                
        for _ in range(cantidad_titulos):
            titulo = input("Ingresa el título: ")
            # Valida que el título no esté duplicado ni vacío.
            while titulo in titulos or titulo == "":
                print ("-----------------")
                print ("Título ya ingresado o no se ingreso ninguno")
                titulo = input("Ingresa otra vez un título: ")
                print ("----------------")
                
            print(f"Título ingresado: {titulo}")
            titulos.append(titulo)
            # Añade 0 ejemplares al nuevo título en la lista paralela.
            posicion = len(titulos) - 1
            ejemplares.insert(posicion, 0)

    # --- OPCIÓN 2: ASIGNAR EJEMPLARES A TÍTULOS EXISTENTES ---
    elif seleccion == "2":
        # Validación de existencia de títulos.
        if not titulos:
            print("No hay titulos ingresados para asignar ejemplares.")
            continue

        for i, titulo in enumerate(titulos):
            print(f"{i + 1}. {titulo}")

        # Valida la selección del número de título (posición).
        while True:
            posicion_str = input("Elija el numero de titulo para ingresar ejemplares: ")
            
            if posicion_str.isdigit():
                posicion = int(posicion_str) - 1
                if 0 <= posicion < len(titulos):
                    break
                else:
                    print("Número de título fuera de rango. Intente nuevamente.")
            else:
                print("Entrada inválida. Ingrese un número de la lista.")

        # Valida la cantidad de ejemplares.
        while True:
            cantidad_str = input("Ingrese cantidad de ejemplares: ")
            
            if cantidad_str.isdigit() and int(cantidad_str) >= 0:
                cantidad = int(cantidad_str)
                break
            else:
                print("Por favor, ingrese una cantidad numérica positiva o cero.")

        # Actualiza la lista de ejemplares.
        ejemplares[posicion] += cantidad
        print(f"Ejemplares disponibles actualmente para {titulos[posicion]}: {ejemplares[posicion]}")

    # --- OPCIÓN 3: MOSTRAR CATÁLOGO COMPLETO (TÍTULO Y STOCK) ---
    elif seleccion == "3":
        if not titulos:
            print ("No hay titulos ingresados. El catálogo está vacío.")
            continue
        
        print ("--- Catálogo Actual (Título y Stock) ---")
        
        # Usa enumerate para obtener el título y su stock simultáneamente.
        for i, titulo in enumerate(titulos):
            stock = ejemplares[i]
            print(f"{i + 1}. {titulo} | Stock: {stock}")
        
        print("-----------------------------------------")


    # --- OPCIÓN 4: CONSULTAR DISPONIBILIDAD DE UN TÍTULO ESPECÍFICO ---
    elif seleccion == "4":
        if not titulos:
            print ("No hay titulos ingresados, deben existir estos para poder ingresar la cantidad de ejemplares.")
            continue
        titulo_pregunta = input ("Ingresar titulo a consultar: ")

        # Bucle para validar si el título existe o dar la opción de volver al menú.
        while True:
            if titulo_pregunta in titulos:
                posicion = titulos.index(titulo_pregunta)
                print ("----------------")
                print(f"Ejemplares disponibles en {titulo_pregunta}: {ejemplares[posicion]}")
                print ("----------------")
                break
            else:
                print(f"El titulo: {titulo_pregunta} no esta dentro del catálogo.")
                print ("¿Queres ingresaar un titlulo nuevamente? (Si: ingresa de nuevo / No: Volver al menu)")
                if input().lower() == "si":
                    titulo_pregunta = input ("Ingresar titulo a consultar: ")
                else:
                    break

    # --- OPCIÓN 5: LISTAR AGOTADOS ---
    elif seleccion == "5":
        if not titulos:
            print ("No hay titulos ingresados. Deben existir estos para poder listar ejemplares.")
            continue

        hay_agotados = False
        print("--- Libros Agotados ---")

        # Recorre ejemplares y usa el índice para acceder al título si el stock es 0.
        for i, ejemplar in enumerate(ejemplares):
            if ejemplar == 0:
                print(f"- {titulos[i]}")
                hay_agotados = True
                
        # Muestra mensaje si no se encontraron libros agotados.
        if not hay_agotados:
            print("No hay libros agotados en el catálogo. ¡Todo disponible!")

    # --- OPCIÓN 6: AGREGAR TÍTULOS CON EJEMPLARES INICIALES ---
    elif seleccion == "6":
        titulo_nuevo = input("Ingrese un nuevo libro: ")
        if titulo_nuevo in titulos:
            print(f"El libro ingresado {titulo_nuevo} ya existe")
        else:
            titulos.append(titulo_nuevo)
            
            # Validación de la cantidad de ejemplares para el nuevo título.
            while True:
                cantidad_str = input(f"Indica la cantidad de ejemplares de {titulo_nuevo}: ")
                if cantidad_str.isdigit() and int(cantidad_str) >= 0:
                    cantidad = int(cantidad_str)
                    break
                else:
                    print("Por favor, ingrese una cantidad numérica positiva o cero.")
                    
            posicion = titulos.index(titulo_nuevo)
            ejemplares.insert(posicion, cantidad)
            print(f"Libro'{titulo_nuevo}' se agregado al catalogo con {cantidad} de ejemplares.")

    # --- OPCIÓN 7: ACTUALIZAR EJEMPLARES (PRÉSTAMO/DEVOLUCIÓN) ---
    elif seleccion == "7":
        if not titulos:
            print ("No hay titulos ingresados, deben existir estos para poder ingresar la cantidad de ejemplares.")
            continue
        for i, titulo in enumerate(titulos):
            print(f"{i + 1}. {titulo}")
            
        # Valida la selección del libro.
        while True:
            posicion_str = input("Ingresá el numero de libro: ")
            if posicion_str.isdigit():
                posicion = int(posicion_str) - 1
                if 0 <= posicion < len(titulos):
                    break
                else:
                    print("Número de libro fuera de rango. Intente nuevamente.")
            else:
                print("Entrada inválida. Ingrese un número de la lista.")

        accion = input("Ingresa que acción queres realizar 'p' prestamo / 'd' devolución: ").lower()
        if accion == "p":
            # No permite prestar si el stock es cero.
            if ejemplares[posicion] > 0:
                ejemplares[posicion] -= 1
                print(f"Prestamos realizado. Disponibles de {titulos[posicion]}: {ejemplares[posicion]}")
                print ("-------------")
            else:
                print(f"No hay ejemplares para {titulos[posicion]}")
                print("--------------")
        elif accion == "d":
            ejemplares[posicion] += 1
            print("Libro devuelto.")
            print("---------------")

    # --- OPCIÓN 8: SALIR DEL BUCLE PRINCIPAL
        print ("Nos vemos")
        break
    
    # Manejo de opciones inválidas.
    else:
        print("Opción no válida. Por favor, seleccione un número del 1 al 8.")