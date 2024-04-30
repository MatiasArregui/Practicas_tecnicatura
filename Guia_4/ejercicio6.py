    # Realizar un algoritmo que:
def ingresoValores():    
    # a. Permite ingresar una serie de números enteros entre 100 y 500 inclusivos.
    acum1 = cont1 = 0
    while True:
        try:
            entrada = int(input("Ingresa un valor entre 100 y 500 inclusive: "))
            if 100 <= entrada <= 500:
                # b. Acumular los valores.
                acum1+=entrada
                # c. Contar los valores.
                cont1+=1
            elif entrada == -1:
                # e. Salir con -1.
                print("Programa finalizado")
                break
            else:
                print("Ingrese un valor entre 100 y 500 inclusive")
                continue
        except:
            print("Ingrese un valor entero")
    # d. Sacar el promedio de los valores.
    if acum1 != 0:
        return acum1 / cont1
    else:
        return 0

if __name__ == "__main__":
    print(f"Promedio de valores: {ingresoValores()}")