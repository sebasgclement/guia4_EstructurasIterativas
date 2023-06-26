# Solicitar al usuario una palabra
palabra = input("Ingresa una palabra: ")

# Recorrer la palabra de forma inversa
for i in range(len(palabra)-1, -1, -1):
    letra = palabra[i]
    print(letra)
