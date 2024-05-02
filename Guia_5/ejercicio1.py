# Ejercicio 1:
def buscadorPalabra(texto):
    from colorama import Fore
    # 1. A partir de una cadena de texto:
    # 2. Mostrar en pantalla la cadena completa.
    print(f"Texto completo:\n{texto}")
    # 3. Añadir una estructura de control while.
    while True:
        # 4. Solicitar al usuario ingrese una palabra a buscar en el texto.
        try:
            palabra = input("\nIngrese la palabra a buscar: ").lower()
            # 5. Salir con enter o sea cuando palabra sea igual ‘’
            if palabra == "":
                print("programa finalizado")
                break
            else:
                # 6. Para buscar utilizar texto.find
                busqueda = texto.lower().find(" " + palabra + " ")
                # 7. Si la búsqueda devuelve -1, mostrar el cartel “La palabra no se encuentra”
                if busqueda != -1:
                    textoNuevo = texto.split()
                    for x in textoNuevo:
                        if x.lower() == palabra.lower():
                            print(Fore.RED + x, end=" ")
                        else:
                            print(Fore.RESET + x, end=" ")
                # 8. Si la palabra se encuentra mostrar el texto con la palabra coloreada en rojo.
                if busqueda == -1:
                    print("La palabra no se encuentra")
        except:
            print("Ingrese caracteres alfabeticos")

if __name__ == "__main__":             
    texto = "matias se fue a pasear al parque"
    buscadorPalabra(texto)