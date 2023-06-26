# Solicitar al usuario un número entero
numero = int(input("Ingresa un número entero: "))


if numero < 2:  # Los números menores a 2 no son primos
    """
    En este caso utilizamos una variable conocida como "flag"
    (bandera en inglés). Al ser un booleano, podemos manipu-
    lar la variable como si fuera una tecla de encendido
    -apagado de la luz.
    """
    es_primo = False
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

# Mostrar el resultado
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
