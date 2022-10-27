var_1 = "Javier"
variable = var_1.upper()
print(variable)
variable1 = var_1.lower()
print(variable1)

variable2 = len(var_1)
print(variable2)

variable3 = variable2 / 7
print(variable3)

def funcion1():
    operacion1 = 12 - (4 * 2) - (2 + 2)
    print(operacion1)
    return
print(funcion1())

def funcion2():
    operacion = 12 - 4 * (2 - 2) + 2
    print(operacion)
    return
print(funcion2())
    


edad = int(input("Introduce su edad: "))

def funcion3():
    
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

    return
print(funcion3())