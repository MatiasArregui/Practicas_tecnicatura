# Realizar un algoritmo para ingresar una serie de temperaturas decimales entre -20 y 50.
def temperaturas():
    while True:
        entrada= int(input("Ingresar una temperatura entre -20 y 50: \n"))
        # Salir con 100.
        if entrada == 100:
            print("Programa finalizado")
            break
        # Validar que los valores estén entre -20 y 50.
        # Contar y sacar el promedio de los valores bajo cero.
        # Contar y sacar el promedio de los valores sobre cero.
        # Contar cuántos valores ingresados son iguales a cero.
        # Mostrar resultados.
