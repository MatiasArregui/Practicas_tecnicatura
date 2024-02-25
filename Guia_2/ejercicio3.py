def tresNumerosMayor():
# Desarrollar un algoritmo para determinar el mayor de tres números distintos.
    # Muestra un mensaje de presentación.
    print("Binevenido! Este programa compara tres numeros, determinando el mayor\n")
    # Mostrar mensaje de ingreso de un valor y guardarlo en la variable a.
    a= int(input("Ingrese el valor de a: \n"))
    # Mostrar mensaje de ingreso de un valor y guardarlo en la variable b.
    b= int(input("Ingrese el valor de b: \n"))
    # Mostrar mensaje de ingreso de un valor y guardarlo en la variable c.
    c= int(input("Ingrese el valor de c: \n"))
    # Implementar tres comparaciones para determinar cuál es el mayor.
    if c < a > b:
        print(f"La variable A es mayor a la variable B y C")
    elif a < b > c:
        print(f"La variable B es mayor a la variable A y C")
    elif a < c > b:
        print(f"La variable C es mayor a la variable A y B")
    elif a == b != c:
        print("La variable A tiene el mismo valor a la variable B")
    elif a == c != b:
        print("La variable A tiene el mismo valor a la variable C")
    elif b == c != a:
        print("La variable B tiene el mismo valor a la variable C")
    else:
        print("La variable A tiene el mismo valor a la variable C y B")
            
    # Mostrar el mensaje correspondiente para cada resultado de la comparación.
    # Mostrar Fin del programa.
tresNumerosMayor()