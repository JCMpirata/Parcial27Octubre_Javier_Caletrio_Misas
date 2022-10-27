numero = int(input("Introduzca un numero de 4 cifras: "))
def numero1():
    mil = numero - (numero%100) / 100
    resto = numero%1000
    centena = (resto - resto%100) / 100
    resto = numero%100
    decena = (resto - resto%10) / 10
    resto = numero%10
    unidad = resto %10

    print("Mil: ", mil)
    print("Centena: ", centena)
    print("Decena: ", decena)
    print("Unidad: ", unidad)
    return

print(numero1())