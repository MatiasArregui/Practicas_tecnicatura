def generadorLista():   
    from random import randint
    # Generar lista:
    # a. Generar una lista de 20 números enteros al azar de 3 dígitos.
    lista = [randint(100,999) for x in range(20)]
    acum1, acum2, acum3, acum4 = 0, 999, 0, 999
    for x in lista:
        print(f"equis: {x}")
        # b. Encontrar el mayor entre los menores a 500.
        if 500 > x > acum1:
            acum1=x
        # c. Encontrar el menor entre los menores a 500.
        if 500 > x < acum2:
            acum2=x
        # d. Encontrar el mayor entre los mayores a 500.
        if 500 < x > acum3:
            acum3=x
        # e. Encontrar el menor entre los mayores a 500.
        if 500 < x < acum4:
            acum4=x
            
    print(f"Mayor entre los menores a 500: {acum1}")
    print(f"Menor entre los menores a 500: {acum2}")
    print(f"Mayor entre los mayores a 500: {acum3}")
    print(f"Menor entre los mayores a 500: {acum4}")
        
generadorLista()