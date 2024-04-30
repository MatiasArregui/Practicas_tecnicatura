def generarLista():
    from random import randint
    # 5. Generar lista:
    # a. Generar una lista de 20 números enteros al azar de 3 dígitos.
    lista = [randint(100,999) for x in range(20)]
    
    cont1 = acum1 = 0
    for x in lista:
        # b. Mostrar los números mayores a 300 y menores a 700 inclusivos.
        if 300 <= x <= 700:
            print(f"Valor entre 300 y 700 de la lista: {x}") 
            # c. Acumular los números del rango.
            acum1+=x
            # d. Contar los números del rango.
            cont1+=1
    print(f"Valores acumulados: {acum1}")
    print(f"Cantidad de valores: {cont1}")

if __name__ == "__main__":
    generarLista()