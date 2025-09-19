opcion = int(input("Seleccione una opcion:\n1- De decimal a binario\n2- De binario a decimal\n"))
 
if opcion == 1:
    print("Convertidor de Decimal a Binario")
    numero = int(input("Ingrese el Numero Decimal: "))
    num_binario = ""
    
    if numero == 0:
        num_binario = "0"
    else:
        while numero > 0:
            resto = numero % 2
            num_binario = str(resto) + num_binario
            numero //= 2
            
    print(f"El numero a binario es: {num_binario}")

elif opcion == 2:
    print("Convertidor de Binario a Decimal")
    numero = input("Ingrese el Numero Binario: ")
    
    es_binario = True
    for digito in numero:
        if digito not in '01':
            es_binario = False
            break
    
    if es_binario:
        num_decimal = 0
        for digito in numero:
            num_decimal = num_decimal * 2 + int(digito)
        print(f"El numero a decimal es: {num_decimal}")
    else:
        print("Error: El número ingresado no es binario. Debe contener solo 0s y 1s.")

else:
    print("Error en eleccion.")