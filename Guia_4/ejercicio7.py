    # Realizar un algoritmo que:
def generadorLista():    
    # a. Generar una lista al azar de 20 números enteros de hasta 2 dígitos.
    from random import randint
    lista1=[randint(10,99) for x in range(20)]
    # b. Obtener una segunda lista con los elementos no repetidos de la primera lista.
    lista2=[]
    for x in lista1:
        if x not in lista2:
            lista2.append(x)
    # c. Mostrar la lista original.
    print(f"Lista original: {lista1}")
    # d. Mostrar la nueva lista.
    print(f"Lista nueva sin repetidos: {lista2}")
    
if __name__ == "__main__":    
    generadorLista()