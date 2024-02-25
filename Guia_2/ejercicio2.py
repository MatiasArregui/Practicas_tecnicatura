def mayorOIgual():
# Desarrollar un algoritmo para determinar el mayor de dos números enteros, que pueden ser distintos o iguales.
    # Mostrar un mensaje de presentación explicando que hace el programa.
    print("El programa permite el ingreso de dos numeros y comparara ambos, determinando cual es el mayor o si el valor de ambos es igual")
    # Mostrar mensaje de ingreso de un valor y guardarlo en la variable a.
    variableA= int(input("Ingresar el valor de la variable A: \n"))
    # Mostrar mensaje de ingreso de un valor y guardarlo en la variable b.
    variableB= int(input("Ingresar el valor de la variable B: \n"))
    # Comparar si a == b.
    if variableA == variableB:
        # Por la salida del Sí indicar que a y b son iguales, terminar el programa.
        print(f"La variable A {variableA} es igual a la variable B {variableB}")
        print("\nPrograma finalizado")
    else:    
        # Por la salida del No comprobar Si a > b.
        if variableA > variableB:
            print(f"La variable A {variableA} es mayor a la variable B {variableB}")
        # Por la salida del Sí indicar que a es mayor que b.
        # Por la salida del No indicar que b es mayor que a.
        else:
            print(f"La variable B {variableB} es mayor a la variable A {variableA}")
            print("\nPrograma finalizado")
        # Mostrar Fin del programa.
    
mayorOIgual()
