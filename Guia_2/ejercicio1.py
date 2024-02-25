def mayorDosNumeros():
# Desarrollar un algoritmo para determinar el mayor de dos números enteros distintos.
    # Mostrar un mensaje de presentación explicando que hace el programa.
    print("El programa se encargara de realizar la comparacion de dos numeros, dictaminando cual es el mayor\n")
    # Mostrar mensaje de ingreso de un valor y guardarlo en la variable a.
    variableA= int(input("Ingrese el primer valor a comparar: \n"))
    # Mostrar mensaje de ingreso de un valor y guardarlo en la variable b.
    variableB= int(input("Ingrese el segundo valor a comparar: \n"))
    # Por la salida del No comprobar Si a > b.
    if variableA > variableB:
        print(f"La variable A {variableA} es mayor que la variable B {variableB}")
    # Por la salida del Sí indicar que a es mayor que b.
    else:
        print(f"La variable B {variableB} es mayor que la variable A {variableA}")
    # Por la salida del No indicar que b es mayor que a.
    # Mostrar Fin del programa.
    print("Fin del programa")

mayorDosNumeros()