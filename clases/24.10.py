

# listas compresion


listas_nombres = ['Lucas', 'Roberto', 'Goku', 'Lucas',
                  'Roberto', 'Goku', 'Lucas', 'Roberto', 'Goku']


nombres_minus = [nombre.lower() for nombre in listas_nombres]

nombres_capitalizados = [nombre.capitalize() for nombre in listas_nombres]


print(nombres_minus)


numeros = [numero + 1 for numero in range(0, 10)]

print(numeros)


numeros = [1, 2, 3, 4, 5]

numeros_dobles = [numero * 2 for numero in numeros]

print(numeros_dobles)


'''




lista_dobles_2 = list(map(lambda numero: numero * 2, numeros))


print(lista_dobles_2)


def multiplicar_por_dos(numero):

    return numero * 2


# map agarra una lista y le aplica la funcion

listas_dobles_3 = list(map(multiplicar_por_dos, numeros))



'''
