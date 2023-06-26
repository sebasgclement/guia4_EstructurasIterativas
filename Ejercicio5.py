inversion = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
anios = int(input("¿Años?"))
for i in range(anios):
    inversion *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(inversion, 2)))