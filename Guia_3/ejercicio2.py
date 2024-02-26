def generador():
# Genera una serie de 30 números al azar de hasta 3 dígitos.
    # Importar la biblioteca random (import random).
    from random import randint
    cont1, acum1, cont2, acum2, cont3, acum3 = 0, 0, 0, 0, 0, 0
    # Generar números aleatorios entre 0 y 999 (random.randint(0, 999).
    for x in range(30):
        numero= randint(0,999)
        print(f"valor: {numero} vuelta: {x}", end=" ")
        # Contar y acumular los valores entre 0 y 300 inclusivos.
        if 300 >= numero >= 0:
            cont1+=1
            acum1+=numero
        # Contar y acumular los valores entre 301 y 600 inclusivos.
        if 600 >= numero >= 301:
            cont2+=1
            acum2+=numero
        # Contar y acumular los valores entre 601 y 1000 inclusivos.
        if 1000 >= numero >= 601:
            cont3+=1
            acum3+=numero
    # Mostrar los resultados.
    print(f"\nlos valores entre 0 y 300 inclusivos: {cont1}, acumulado: {acum1}")
    print(f"los valores entre 301 y 600 inclusivos: {cont2}, acumulado: {acum2}")
    print(f"los valores entre 601 y 1000 inclusivos: {cont3}, acumulado: {acum3}")
    
generador()
