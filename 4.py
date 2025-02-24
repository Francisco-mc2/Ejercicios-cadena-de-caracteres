#Version
#Enunciado del algoritmo

cadena = input("Introduce la cadena principal: ")
subcadena = input("Introduce la subcadena a buscar: ")

if subcadena in cadena:
    print(f"La cadena '{subcadena}' está contenida en '{cadena}'.")
else:
    print(f"La cadena '{subcadena}' NO está contenida en '{cadena}'.")