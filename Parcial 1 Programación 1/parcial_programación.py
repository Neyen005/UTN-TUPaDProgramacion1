elecciones_menu =  ["1. Ingresá solo el titulo",
                     "2. Ingresa ejemplares disponibles (sin titulos)",
                     "3. Mostrar catálogo",
                     "4. Consultar disponibilidad de un titulo específico",
                     "5. Listar agotados",
                     "6. Agregar titulos (con ejemplares)",
                     "7. Actualizar ejemplares (prestamos/devolución)",
                     "8. Ver catálogo completo",
                     "9. Salir"]
titulos = []
ejemplares = []

while True: 
    print ("Menú Librería")
    for seleccion in elecciones_menu: 
        print (seleccion) 
    seleccion = input ("Seleccione elección ")

    print ("------------------")
            
    if seleccion == "1":
        titulo = input ( " Ingresá solo el titulo " )
                
        while titulo in titulos or titulo == "": 
            print ("..............")
            print ("Titulo ya ingresado o no ingreso titulo")
            titulo = input("Ingresa otra vez un titulo")
            print (".............")
                
        print(f"Titulo ingresado: {titulo}")
        titulos.append(titulo)
        posicion = titulos.index(titulo)
        ejemplares.insert(posicion,0)      
    
    elif seleccion == "2":
        
        if not titulos:
            print ("No hay titulos ingresados, deben existir estos para poder ingresar la cantidad de ejemplares.")
            continue
        for i, titulo in enumerate(titulos):
            print(f"{i + 1}. {titulo}")

        posicion = int(input("Elija el numero de titulo para ingresar ejemplares: ")) - 1

        while posicion < 0 or posicion >= len(titulos):      
            print ("Posición incorrecta, intente nuevamente")
            posicion = int(input("Elija el numero de titulo para ingresar ejemplares: ")) - 1
        cantidad = int(input("Ingrese cantidad de ejemplares: "))
        ejemplares[posicion] += cantidad    
        print(f"Ejemplares disponibles actualmente para {titulos[posicion]}: {ejemplares[posicion]} ") 
    elif seleccion == "3":
        if not titulos:
            print ("No hay titulos ingresados, deben existir estos para poder ingresar la cantidad de ejemplares.")
            continue
        print ("Catálogo")
        for i, titulo in enumerate(titulos):
            print(f"{i + 1}. {titulo}")
            print("----------------")      
    elif seleccion == "4":
        if not titulos:
            print ("No hay titulos ingresados, deben existir estos para poder ingresar la cantidad de ejemplares.")
            continue
        titulo_pregunta = input ("Ingresar titulo a consultar: ")

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
    elif seleccion == "5":
        if not titulos:
            print ("No hay titulos ingresados, deben existir estos para poder ingresar la cantidad de ejemplares.")
            continue
        sin_titulos = False
        for i, ejemplar in enumerate(ejemplares):
        if ejemplar == 0:
        sin_titulos = True
        print(titulos[i])
                    print(titulo)
    elif seleccion == "6":
        titulo_nuevo = input("Ingrese un nuevo libro: ")
        if titulo_nuevo in titulos:
            print(f"El libro ingresado {titulo_nuevo} ya existe")
        else:
            titulos.append(titulo_nuevo)
            cantidad = int(input(f"Indica la cantidad de ejemplares de {titulo_nuevo}: "))
            posicion = titulos.index(titulo_nuevo)
            ejemplares.insert(posicion, cantidad)
            print(f"Libro'{titulo_nuevo}' se agregado al catalogo con {cantidad} de ejemplares.")

    elif seleccion == "7":
        if not titulos:
            print ("No hay titulos ingresados, deben existir estos para poder ingresar la cantidad de ejemplares.")
            continue
        for i, titulo in enumerate(titulos):
            print(f"{i + 1}. {titulo}")
        posicion = int(input("Ingresá el numero de libro: ")) - 1
            
        while posicion < 0 or posicion >= len(titulos):      
            print ("Posición incorrecta, intente nuevamente")
            posicion = int(input("Elija el numero de titulo para ingresar ejemplares: ")) - 1
        accion = input("Ingresa que acción queres realizar 'p' prestamo / 'd' devolución: ").lower()
        if accion == "p":
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

    elif seleccion == "8":
        if not titulos:
            print ("No hay titulos ingresados, deben existir estos para poder ingresar la cantidad de ejemplares.")
            continue
        print("Catálogo completo")
        for i, titulo in enumerate(titulos):
            print(f"{i + 1}. {titulo} Cantidad de ejemplares: {ejemplares[i]}")

    elif seleccion == "9":
        print ("Nos vemos")
        break
            