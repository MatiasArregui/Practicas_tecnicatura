def superTrianguloRectangulo():
    # Desarrollar un algoritmo para calcular la superficie de un triángulo rectángulo (base por altura dividido dos):
    # Mostrar el mensaje de ingreso y guardar en base.
    base= float(input("Ingrese el valor de base: \n"))
    # Mostrar el mensaje de ingreso y guardar en altura.
    altura= float(input("Ingrese el valor de altura: \n"))
    # Calcular y guardar en superficie.
    superficie= (base * altura) / 2
    # Mostrar mensaje y el valor de superficie.
    print(f"Valor de la superficie: {superficie}")

superTrianguloRectangulo()
