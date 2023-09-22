
from datos_stark import lista_personajes

# B Recorrer la lista imprimiendo por consola el nombre de cada superhéroe


def recorrer_nombre_superheroe(lista_personajes: list[dict]):
    nombres_personajes = []

    for personaje in lista_personajes:

        nombre = personaje.get('nombre', 'No se encontro nombre')
        nombres_personajes.append(nombre)

    return nombres_personajes


resultado = recorrer_nombre_superheroe(lista_personajes)


# nombres_superheroes = recorrer_nombre_superheroe(lista_personajes)

# print(nombres_superheroes)

# c
# Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo


def reccorer_nombre_superheroe_con_altura(lista_personajes: list[dict]):

    for personaje in lista_personajes:

        nombre = personaje.get('nombre', 'No se encontro nombre')
        altura = personaje.get('altura', 'No se encontro altura')

        print(f'Nombre:{nombre} Altura: {altura}')


# reccorer_nombre_superheroe_con_altura(lista_personajes)

# D
# Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)


def determina_superheroe_mas_alto(lista_personajes: list[dict]):

    superheroe_mas_alto = None

    for personaje in lista_personajes:

        altura = personaje.get('altura', 'No se encontro altura')
        altura = float(altura)

        if superheroe_mas_alto == None or altura > superheroe_mas_alto:
            superheroe_mas_alto = altura
            nombre = personaje.get('nombre', 'No se encontro altura')
    return superheroe_mas_alto, nombre


superheroe_mas_alto, nombre = determina_superheroe_mas_alto(lista_personajes)

# print(
#     f'El superheroe mas alto es {nombre} y su altura es {superheroe_mas_alto}')


# E
# Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

def determina_superheroe_mas_bajo(lista_personajes: list[dict]):

    superheroe_mas_bajo = None

    for personaje in lista_personajes:

        altura = personaje.get('altura', 'No se encontro altura')
        altura = float(altura)

        if superheroe_mas_bajo == None or altura < superheroe_mas_bajo:
            superheroe_mas_bajo = altura
            nombre = personaje.get('nombre', 'No se encontró nombre')
    return superheroe_mas_bajo, nombre


super_heroe_mas_bajo, nombre_super_heroe_mas_bajo = determina_superheroe_mas_bajo(
    lista_personajes)

# print(
#     f"El superhéroe más bajo es {nombre} con una altura de {super_heroe_mas_bajo} cm.")
# F
# Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)


def determina_altura_promedio(lista_personajes: list[dict]):

    acumulador_altura_personajes = 0
    contador_personajes = 0
    for personaje in lista_personajes:

        altura = personaje.get('altura', 'No se encontro altura')
        altura = float(altura)

        acumulador_altura_personajes += altura
        contador_personajes += 1

    promedio_altura_personajes = acumulador_altura_personajes / contador_personajes

    return promedio_altura_personajes


promedio_altura_personajes = determina_altura_promedio(lista_personajes)

# print(promedio_altura_personajes)

# Calcular e informar cual es el superhéroe más y menos pesado


def calcular_mas_pesado(lista_personajes: list[dict]):

    personaje_peso_maximo = None
    for personaje in lista_personajes:

        peso_personaje = personaje.get('peso', 'No se encontro peso...')
        peso_personaje = float(peso_personaje)

        if personaje_peso_maximo == None or peso_personaje > personaje_peso_maximo:
            personaje_peso_maximo = peso_personaje
            nombre_personaje = personaje.get('nombre', 'No se encontro nombre')

    return personaje_peso_maximo, nombre_personaje


personaje_peso_maximo, nombre_personaje = calcular_mas_pesado(lista_personajes)

# print(
#     f'El personaje mas pesado es {nombre_personaje} y su peso {personaje_peso_maximo}')


def calcular_menos_pesado(lista_personajes: list[dict]):

    personaje_peso_min = None
    for personaje in lista_personajes:

        peso_personaje = personaje.get('peso', 'No se encontro peso...')
        peso_personaje = float(peso_personaje)

        if personaje_peso_min == None or peso_personaje < personaje_peso_min:
            personaje_peso_min = peso_personaje
            nombre_personaje = personaje.get('nombre', 'No se encontro nombre')

    return personaje_peso_min, nombre_personaje


personaje_peso_min, nombre_personaje = calcular_menos_pesado(lista_personajes)

# print(
#     f'El personaje mas liviano es {nombre_personaje} y su peso {personaje_peso_min}')


def pedir_opcion_menu() -> str:
    return input("Elija una opcion: ")


def mostrar_menu() -> str:
    menu =\
        """
    1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    5 - Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
    6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    7 - Calcular e informar cual es el superhéroe más y menos pesado.
    8 - Salir
    """
    print(menu)
    return pedir_opcion_menu()


"""
J - Construir un menú que permita elegir qué dato obtener
"""


def main_app(lista_heroes: list[dict]):
    """
    Ejecuta todo nuestro programa.
    Recibe la lista de heroes
    """

    while True:

        opcion_elegida = mostrar_menu()

        match opcion_elegida:
            case "1":
                (recorrer_nombre_superheroe(lista_personajes))

            case "2":
                determina_superheroe_mas_bajo(lista_heroes)
            case "3":
                heroe_mas_alto = determina_superheroe_mas_alto(
                    lista_heroes, 'max')
            case "4":
                super_heroe_mas_bajo = determina_superheroe_mas_bajo(
                    lista_heroes, 'min')
            case "5":
                pass
            case "6":
                nombre_super_heroe_mas_bajo
            case "7":
                pass
            case "8":
                break
            case _:
                print('Opcion incorrecta, elija entre 1 y 9')
