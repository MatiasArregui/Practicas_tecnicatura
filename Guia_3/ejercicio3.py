# Realice un algoritmo que:
def ingreso():
    # Permite ingresar una serie de números enteros entre 1 y 999.
    acum1, cont1, acum2, cont2 = 0, 0, 0, 0
    while True:
        ingreso= int(input("Ingresar numeros enteros entre 1 y 999: \n"))
        # Salir con cero (0).
        if ingreso == 0:
            print("Programa finalizado")
            break
        # Validar que no se ingresen valores fuera del rango y mostrar un mensaje “Valor fuera de rango”.
        if ingreso > 999 or ingreso < 0:
            print("Valor fuera de rango")
            continue
        # Contar y acumular los menores o igual a 500.
        if ingreso <= 500:
            cont1+=1
            acum1+=ingreso
        # Contar y acumular los valores mayores a 500.
        if ingreso > 500:
            cont2+=1
            acum2+=ingreso
    # Mostrar los resultados.
    print(f"Valores menores o iguales a 500: {cont1}, acumulado: {acum1}")
    print(f"Valores mayores a 500: {cont2}, acumulado: {acum2}")
    
ingreso()
