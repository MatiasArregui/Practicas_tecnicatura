def generador():
# Generar una serie de 20 números al azar de hasta 3 dígitos.
    # Importar la biblioteca random (import random).
    from random import randint
    # Contar y acumular los divisibles por 2 (operador módulo %).
    # Contar y acumular los divisibles por 3.
    # Contar y acumular los divisibles por 4. 
    # Contar y acumular los divisibles por 5. 
    div2, div3, div4, div5, acum2, acum3, acum4, acum5 = 0, 0, 0, 0, 0, 0, 0, 0
    # Generar números aleatorios entre 100 y 999 (random.randint(100, 999).
    for x in range(20):
        numeroRandom= randint(100,999)
        if numeroRandom % 2 == 0:
            acum2+=numeroRandom
            div2+=1
        if numeroRandom % 3 == 0:
            acum3+=numeroRandom
            div3+=1
        if numeroRandom % 4 == 0:
            acum4+=numeroRandom
            div4+=1
        if numeroRandom % 5 == 0:
            acum5+=numeroRandom
            div5+=1
    # Mostrar los resultados al finalizar el bucle.
    print(f"\nValores acumulados en total {acum2}, cantidad de divisibles por {div2}")
    print(f"Valores acumulados en total {acum3}, cantidad de divisibles por {div3}")
    print(f"Valores acumulados en total {acum4}, cantidad de divisibles por {div4}")
    print(f"Valores acumulados en total {acum5}, cantidad de divisibles por {div5}")

generador()


    
