

from biblioteca_stark_00 import *

from datos_stark import lista_personajes


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
