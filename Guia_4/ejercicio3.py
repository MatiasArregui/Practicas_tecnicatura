def generadorLista():
    from random import randint
    # Generar lista
    lista = [randint(100,999) for x in range(20)]
    # a. Generar una lista de 20 números enteros al azar de 3 dígitos.
    # b. Mostrar toda lista.
    print(f"Lista creada: {lista}")
    for x in lista:
        # c. Marcar con * (asterisco) los divisibles por 2.
        if x % 2 == 0:
            print(f"* {x}")
        # d. Marcar con # (numeral) los divisibles por 3.
        if x % 3 == 0:
            print(f"# {x}")
        # e. Marcar con $ (peso) los divisible por 4.
        if x % 4 == 0:
            print(f"$ {x}")
        # f. Marcar con & (per se and per sand – por sí mismo) los divisibles por 5.
        if x % 5 == 0:
            print(f"& {x}")
    
generadorLista()
