def promedio():
# Desarrollar un algoritmo para calcular el promedio de 5 valores enteros:
    # Mostrar mensaje de ingreso y guardar en uno.
    uno= float(input("Ingresar el valor del primer valor: \n"))
    # Mostrar mensaje de ingreso y guardar en dos.
    dos= float(input("Ingresar el valor del segundo valor: \n"))
    # Mostrar mensaje de ingreso y guardar en tres.
    tres= float(input("Ingresar el valor del tercer valor: \n"))
    # Mostrar mensaje de ingreso y guardar en cuatro.
    cuatro= float(input("Ingresar el valor del cuarto valor: \n"))
    # Mostrar mensaje de ingreso y guardar en cinco.
    cinco= float(input("Ingresar el valor del quinto valor: \n"))
    # Calcular el promedio y guardar en promedio.
    promedio= (uno + dos + tres + cuatro + cinco)/5
    # Mostrar mensaje y el valor de promedio.
    print(f"Promedio de la suma de los cinco valores: {promedio}")
    
promedio()
