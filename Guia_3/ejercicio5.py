# Realice un algoritmo que:
def generadorLista():
    from random import randint
    # Genere una lista de 30 números al azar de hasta 2 dígitos.
    lista= [randint(0,99) for x in range(30)]
    # Mostrar los pares con un “*” asterisco delante. (nro % 2 = 0)
    # Mostrar los impares con un “#” numeral delante. (else)
    # Contar y acumular los pares.
    # Contar y acumular los impares.
    # Mostrar el resultado de la cuenta y el acumulado de cada grupo.
    
generadorLista()
