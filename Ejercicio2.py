
# Creo una funcion, en la que la cadena le doy la vuelta para que el texto salga en orden
cadena = "zeréP nauJ, 01"

def cadena_funcion():
    cadena1 = cadena[::-1].split(",")
    print("{} ha sacado un {} de nota".format(cadena1[1], cadena1[0]))
    return

print(cadena_funcion())


