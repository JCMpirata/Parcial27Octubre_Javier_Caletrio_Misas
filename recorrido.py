lista = [18, 50, 210, 80, 145, 333, 70, 30]

def multiplo():
    for numero in lista:
        if numero %10 == 0 and numero < 200:
            print(numero)
        elif numero > 300:
            break
    return
print(multiplo())
