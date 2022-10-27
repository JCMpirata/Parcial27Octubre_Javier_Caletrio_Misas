# Creo una lista con numeros repetidos

lista = [12, 23, 87, 26, 45, 98, 26, 76, 26, 26, 56, 74, 37, 39]


# Creo la funcion
def modificar():
    lista1 = list(set(lista))
    print(lista1)

    lista1 = lista1.sort(reverse = True)
    print(lista1)

    
    for numeros in lista1:
        if numeros %2 == 0:
            print(lista1.append(numeros))
            print(lista1.sort())
        

        
    
    return


print(modificar())




