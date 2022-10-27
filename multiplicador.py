
def numero():
    numero_magico = 12345679
    numero_usuario = int(input("Introduzca un numero entre 1 y 9: "))
    print(numero_usuario)

    numero_usuario1 = numero_usuario * 9
    print(numero_usuario1)

    numero_magico1 = numero_usuario1 * numero_magico
    print(numero_magico1)
    return

print(numero())
