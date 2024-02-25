    # Desarrollar un algoritmo para el cálculo de la hipotenusa:
def raizCuadrada():     
    # Importar la librería math para obtener la raíz cuadrada (import math).
    import math
    # Mostrar mensaje de ingreso y guardar cateto A en A.
    A= float(input("Ingresar el valor del cateto A: \n"))
    # Mostrar mensaje de ingreso y guardar cateto B en B.
    B= float(input("Ingresar el valor del cateto B: \n"))
    # Calcular y guardar hipotenusa en C “C = math.sqrt( pow(A,2) + pow(B,2) )” o “C = math.sqrt(A ** 2 + B ** 2)”
    C= math.sqrt(pow(A,2) + pow(B,2))
    # Mostrar mensaje con el resultado de C.
    print(f"Resultado de la operacion: {C:.2f}")
    
raizCuadrada()
