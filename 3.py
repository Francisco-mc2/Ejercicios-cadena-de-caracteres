#Version
#Enunciado del algoritmo:

cadena = input("Introduce una cadena: ")
cadena_convertida = ""

for caracter in cadena:
    if caracter.isupper():
        cadena_convertida += caracter.lower()
    elif caracter.islower():
        cadena_convertida += caracter.upper()
    else:
        cadena_convertida += caracter  

print("Cadena con mayúsculas y minúsculas invertidas:", cadena_convertida)