# Desarrollar un algoritmo para permitir el ingreso de una serie de números enteros, hasta que el usuario ingrese el número 0, determinar cuál es el mayor.
def ingresoEnteros():
    # Muestre un mensaje de presentación.
    print("Bienvenido! El siguiemte programa permite el ingreso de numeros enteros y permite dictaminar el mayor de ellos")
    mayor=0
    while True:
        a = int(input("Ingrese un numero entero, ingresar 0 para salir del programa: \n"))
        # Iniciar una variable mayor en cero para obtener el mayor propiamente.
        # Hacer un bucle while que permita ingresar una serie de números enteros.
        # Dentro del bucle solicitar el ingreso de un valor entero para a.
        if a == 0:
            print("programa finalizado")
            break
        if a > mayor:
            mayor = a
        # Verificar si el número ingresado es cero para encontrar la salida de bucle con break.
        # Verificar si a es mayor que mayor y copiar a en mayor si es verdadero.
        # Por la línea siguiente fuera del bucle mostrar un mensaje y el mayor.
    print(f"El numero mayor ingresado es: {mayor}")

ingresoEnteros()