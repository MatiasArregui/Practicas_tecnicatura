# Desarrollar un algoritmo para calcular el promedio de 4 números ingresados
def promedio()->float:
    # por teclado:
    # Mostrar mensaje de ingreso y guardar en uno.
    uno = float(input("Ingresar el primer valor a promediar: "))
    # Mostrar mensaje de ingreso y guardar en dos.
    dos = float(input("Ingresar el segundo valor a promediar: "))
    # Mostrar mensaje de ingreso y guardar en tres.
    tres = float(input("Ingresar el tercer valor a promediar: "))
    # Mostrar mensaje de ingreso y guardar en cuatro.
    cuatro = float(input("Ingresar el cuarto valor a promediar: "))
    # Sumar, dividir por cuatro y guardar en una variable resultado.
    resultado = (uno+dos+tres+cuatro) / 4
    # Mostrar mensaje de resultado y el valor de resultado.
    return resultado

print(promedio())