
# 10
# Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.

lista_palabras = ['Hola', 'Dafasd', 'Holla', 'Casda', 'Gasxcdzcx']


def palabra_larga(lista_palabras):
    palabra_mas_larga = lista_palabras[0]

    if lista_palabras:

        for palabra in lista_palabras:

            if len(palabra) > len(palabra_mas_larga):
                palabra_mas_larga = palabra

    return palabra_mas_larga


resultado = palabra_larga(lista_palabras)

# print(resultado)

# 11
# Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.


def cantidad_vocales(cadena_texto):

    vocales = "aeiou"

    contador_vocales = 0

    for letra in cadena_texto:

        if letra in vocales:
            contador_vocales += 1

    return contador_vocales


cadena_texto = 'Haeiounoi'

resultado = cantidad_vocales(cadena_texto)

# print(resultado)

# 12
# Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas

lista_uno = ['Pepe', 'Raul', 'Dardo', 'Lucas']
lista_dos = ['Pepe', 'Dario', 'Coco', 'Lucas']


def lista_nombres_ambas_listas(lista_uno, lista_dos):
    nombres_repetidos = []
    for nombre1 in lista_uno:
        for nombre2 in lista_dos:
            if nombre1 == nombre2:
                nombres_repetidos.append(nombre1)
    return nombres_repetidos


resultado = lista_nombres_ambas_listas(lista_uno, lista_dos)
# print(f'Los nombres que se repiten en las dos listas son {resultado}')

# ------------------------------------------------------------------------------------------------------------------

# 13
# Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.


lista_palabras = ['Hola', 'Como', 'Estas',]


def recibe_palabra_devuelve_dict(lista_palabras: list):
    diccionario_palabras = {}

    for palabra in lista_palabras:
        diccionario_palabras[palabra] = len(palabra)

    return diccionario_palabras


diccionario_final = recibe_palabra_devuelve_dict(lista_palabras)

for clave, valor in diccionario_final.items():
    # print(f'La palabra {clave} tiene {valor} letras')

    # ---------------------------------------------------------------------------------------------------------------------------

    # 14
    # Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo,
    # el valor máximo y el promedio de los números en la lista.

    lista_numeros = [0, 2, 5, 6, 8, 40]

    def devuelve_valor_maximo_minimo_promedio(lista_numeros: list[int]) -> dict[int]:

        numero_min = None
        numero_max = None
        acumulador_numeros = 0

        for numero in lista_numeros:

            acumulador_numeros += numero

            if numero_min == None:
                numero_min = numero
            else:
                if numero < numero_min:
                    numero_min = numero

            if numero_max == None:
                numero_max = numero
            else:
                if numero > numero_max:
                    numero_max = numero

        promedio_lista = acumulador_numeros / len(lista_numeros)

        resultados = {
            'minimo': numero_min,
            'maximo': numero_max,
            'promedio': promedio_lista,
        }

        return resultados

    resultado = devuelve_valor_maximo_minimo_promedio(lista_numeros)

    # print(resultado)

# 15
# Crear una función que recibe una lista de diccionarios con información de películas
# (título, género, director) y devuelve un diccionario con la cantidad de películas por género.

lista_peliculas = [{
    'titulo': 'Shrek',
    'genero': 'animada',
    'director': 'Mike Mitchell',
},
    {
        'titulo': 'Shrek 2',
        'genero': 'animada',
        'director': 'Mike Mitchell',
},
    {
        'titulo': 'Busqueda implacable',
        'genero': 'accion',
        'director': 'Pierre Morel',
}
]


def devuelve_cantidad_peliculas_por_genero(lista_peliculas: list[dict]) -> dict:

    informe_cantidades = {}

    for pelicula in lista_peliculas:

        genero = pelicula.get('genero', 'sin genero')

        if not genero in informe_cantidades.keys():
            informe_cantidades[genero] = 1
        else:
            informe_cantidades[genero] += 1

    return informe_cantidades


# informe = devuelve_cantidad_peliculas_por_genero(lista_peliculas)
# print(informe)
