def promedios()->None:    
    men7, may7, promMen7, promMay7, contMen7, contMay7 = 0, 0, 0, 0, 0, 0
    # De un grupo de n notas de calificación de alumnos ingresadas por teclado:
    while True:
        try:
            entrada = int(input("Ingrese la nota del alumno: "))
        # Salir con -1.
            if entrada == -1:
                print("Programa finalizado\n")
                break
        # Ingresar valores enteros entre 1 y 10.
            if 10 < entrada or entrada < 1:
                print("ingrese un valor entre 1 y diez inclusive")
                continue
            else:
                if entrada < 7:
                    # Contar cuantas notas son menores a 7.
                    men7+=entrada
                    contMen7+=1
                    # Sacar el promedio de notas menores a 7.
                if entrada >=7:
                    # Contar cuantas notas son mayores o iguales a 7
                    may7+=entrada
                    contMay7+=1
                    # Sacar el promedio de notas mayores o iguales a 7.
        except:
            print("Ingrese un valor entero")
    # Mostrar los resultados de la cantidad de notas y los promedios
    print(f"Notas menores a 7: {contMen7} Promedio de notas: {men7/contMen7}")
    print(f"Notas mayores o iguales a 7: {contMay7} Promedio de notas: {may7/contMay7}")
            
promedios()