import json
import os


'''
{
    "nombre": "Deadpool",
    "identidad": "Wade Wilson",
    "altura": 188.0,
    "peso": 95.32,
    "fuerza": 35,
    "inteligencia": "good"
}

1 - Listar los primeros N heroes
2 - Ordenar heroes por altura [Ascendente o Descendente]
3 - Ordenar heroes por fuerza [Ascendente o Descendente]
4 - Buscar heroes por inteligencia [good, average, high] 
5 - Exportar lista Ordenada de heroes ordenada [ASC o DESC] por una clave que decida el usuario a CSV
7 - Salir
'''


def limpiar_consola():
    '''
    Limpia la consola al presionar la tecla enter.
    '''
    _ = input('Presione Enter para continuar...')
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')


def cargar_datos():
    with open(r'Ejercicios\tp\data_stark.json', 'r', encoding='utf-8') as archivo_json:

        data = json.load(archivo_json)

        heroes = data.get('heroes')

    return heroes


def listar_primeros_heroes(heroes, numero_a_listar: int):
    for i, hero in enumerate(heroes[:numero_a_listar], 1):
        print(f"{i}. Nombre: {hero['nombre']}, Identidad: {hero['identidad']}")


def ordenar_heroes_por_atributo(heroes, atributo: str, descendente=False):
    heroes_ordenados = sorted(
        heroes, key=lambda heroe: heroe[atributo], reverse=descendente)
    return heroes_ordenados


def imprimir_heroes_por_atributo(heroes_ordenados, atributo):
    for i, hero in enumerate(heroes_ordenados, 1):
        valor_atributo = hero.get(atributo, "No disponible")
        print(f"{i}. Nombre: {hero['nombre']}, {atributo}: {valor_atributo}")


def buscar_heroe_por_inteligencia(heroes, inteligencia):

    heroes_inteligentes = []

    for heroe in heroes:
        heroe_inteligencia = heroe['inteligencia']

        # Tratar los valores en blanco como "average"
        if heroe_inteligencia == "":
            heroe_inteligencia = "average"

        if heroe_inteligencia == inteligencia:
            heroes_inteligentes.append(heroe)

    return heroes_inteligentes


def imprimir_nombres_de_heroes(heroes_inteligentes):
    for i, hero in enumerate(heroes_inteligentes, 1):
        print(f"{i}. Nombre: {hero['nombre']}")


def crear_encabezados(lista_heroes: list, texto: str) -> str:
    for heroe in lista_heroes:
        primer_campo_de_datos = True
        for key in heroe.keys():
            if primer_campo_de_datos:
                texto += f'{key}'
                primer_campo_de_datos = False
            else:
                texto += f',{key}'
        texto += '\n'
        break
    return texto


def crear_datos(lista_heroes: list, texto: str):
    for heroe in lista_heroes:
        primer_campo = True
        for valor in heroe.values():
            if primer_campo:
                texto += f'{valor}'
                primer_campo = False
            else:
                texto += f',{valor}'
        texto += '\n'
    return texto


def crear_csv(path: str, modo: str, lista: list) -> None:
    with open(path, modo) as archivo_heroes:
        texto = ''
        texto = crear_encabezados(lista, texto)
        texto = crear_datos(lista, texto)

        print(texto)
        archivo_heroes.write(texto)
