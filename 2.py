#Version
#Enunciado del algoritmo: 

cadena = input("Introduce una cadena: ")

while True:
    char1 = input("Introduce el carácter que quieres sustituir: ")
    if len(char1) == 1:
        break
    print("Error: Debes introducir solo un carácter.")

while True:
    char2 = input("Introduce el nuevo carácter: ")
    if len(char2) == 1:
        break
    print("Error: Debes introducir solo un carácter.")

cadena_modificada = cadena.replace(char1, char2)
print("Cadena modificada:", cadena_modificada)
