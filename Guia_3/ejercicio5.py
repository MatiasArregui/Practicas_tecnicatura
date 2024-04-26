# Realice un algoritmo que:
def generadorLista():
    from random import randint
    # Genere una lista de 30 números al azar de hasta 2 dígitos.
    lista= [randint(0,99) for x in range(30)]
    acum1, cont1, acum2, cont2 = 0, 0, 0, 0
    for x in lista:
        # Mostrar los pares con un “*” asterisco delante. (nro % 2 = 0)
        if x % 2 == 0:
            print(f"* {x}", end=" ")
            # Contar y acumular los pares.
            cont1+=1
            acum1+=x
        # Mostrar los impares con un “#” numeral delante. (else)
        else:
            print(f"# {x}", end=" ")
            # Contar y acumular los impares.
            cont2+=1
            acum2+=x
    
    # Mostrar el resultado de la cuenta y el acumulado de cada grupo.
    print(f"\nCantidad de numeros pares: {cont1}, acumulado: {acum1}")
    print(f"Cantidad de numeros impares: {cont2}, acumulado: {acum2}")
    
generadorLista()
