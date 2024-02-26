# Realice un algoritmo que:
def ingreso():
    # Permitir el ingreso de 12 valores entre 1 y 100.
    print("Bienvenido! El siguiente prgrama solo permite el ingreso de 12 valores, entre 1 y 100. Se sale del programa con -1.\n")
    x=0
    acum1, cont1, acum2, cont2 = 0, 0, 0, 0
    while (x <=11):
        ingreso= int(input("Ingrese un valor entre 1 y 100: \n"))
        # Salir con -1 en caso de no completar la lista de los 12 números.
        if ingreso == -1:
            print("Programa finalizado")
            break
        # Validar que el valor ingresado esté entre 1 y 100 inclusivos.
        if 1 <= ingreso <= 100:
            x+=1
            # Contar y acumular los divisibles por 2. (número % 2)
            if ingreso % 2 == 0:
                cont1+=1
                acum1+=ingreso
            # Contar y acumular los no divisibles por 2. (else)
            if ingreso % 2 != 0:
                cont2+=1
                acum2+=ingreso
        else:
            print("Ingreso no valido")
            continue
    # Mostrar los resultados en caso de completar la lista.
    if x == 12:
        print(f"Valores divisbles por 2: {cont1}, acumulados: {acum1}")
        print(f"Valores no divisibles por 2: {cont2}, acumulados: {acum2}")
    # En caso de no completar la lista mostrar el mensaje “No ha completado la lista de 12 números”
    else:
        print("No ha completado la lista de 12 números")
        
ingreso()
