
import os
import json


# Primer parte
def limpiar_consola():
    _ = input('Presione Enter para continuar...')
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')


def imprimir_dato(dato: list) -> None:
    print(dato)


def leer_archivo(nombre_archivo: str):

    try:
        with open(nombre_archivo, 'r') as archivo:

            lista_heroes = json.load(archivo)

            return lista_heroes

    except FileNotFoundError:

        print(f'El archivo {nombre_archivo} no se encuentra')
        return []


def guardar_archivo(nombre_archivo, contenido):

    try:
        with open(nombre_archivo, 'w') as archivo:

            archivo.write(contenido)

        print(f'Se creo el archivo {nombre_archivo}')

        return True

    except Exception:

        print(f"Error al crear el archivo: {nombre_archivo}")

        return False


def capitalizar_palabras(texto: str):

    # dividimos las palabras en listas
    palabras = texto.split()
    # capitalizamos en compresion de lista cada palabra de la lista
    lista_palabras_capitalizadas = [
        palabra.capitalize() for palabra in palabras]

    # convertimos la lista en string
    return ''.join(lista_palabras_capitalizadas)


def obtener_nombre_capitalizado(heroe: dict):

    nombre = heroe.get('nombre', 'N/A')

    return f'nombre:{capitalizar_palabras(nombre)}'


def obtener_nombre_y_dato(heroe: dict, key: str) -> str:

    nombre = heroe.get('nombre', 'N/A')

    valor = heroe.get(key, 'N/A')

    return f'Nombre: {capitalizar_palabras(nombre)} | {capitalizar_palabras(key)} {capitalizar_palabras(valor)}'
