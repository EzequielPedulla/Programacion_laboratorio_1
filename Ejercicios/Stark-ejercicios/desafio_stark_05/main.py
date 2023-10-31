from biblioteca_stark_05 import *
import re


def imprimir_menu_desafio_5():
    print("\nMenú:")
    print("A.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
    print("B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F"
          )
    print("C. Superhéroe más alto de género M")
    print("D. Superhéroe más alto de género F")
    print("E. Superhéroe más bajo de género M")
    print("F. Superhéroe más bajo de género F")
    print("G. Altura promedio de superhéroes de género M")
    print("H. Altura promedio de superhéroes de género F")
    print("I. Cantidad de superhéroes por color de ojos")
    print("J. Cantidad de superhéroes por color de pelo")
    print("K. Cantidad de superhéroes por tipo de inteligencia")
    print("L. Listar superhéroes agrupados por color de ojos")
    print("M. Listar superhéroes agrupados por color de pelo")
    print("N. Listar superhéroes agrupados por tipo de inteligencia")
    print("0. Salir")


def stark_menu_principal_5(lista_personajes):
    while True:
        limpiar_consola()
        imprimir_menu_desafio_5()
        opcion = input("Ingrese la letra de la opción que desea ejecutar: ")
        # Expresión regular para verificar que la entrada sea una letra (mayúscula o minúscula).
        if re.match("^[A-Za-z]$", opcion):
            return opcion
        else:
            print("Opción no válida. Debe ingresar una letra.")
            input("Presione Enter para continuar...")
            return -1  # Retorna -1 en caso de entrada no válida.


def stark_marvel_app_5(lista_personajes):

    while True:
        limpiar_consola()
        stark_menu_principal_5()
        # Utiliza la función que validará la opción.
        opcion = stark_menu_principal_5()


'''
        if opcion == -1:
            print("Opción no válida. Intente de nuevo.")
        elif opcion == 'A':
            stark_agregar_personaje(lista_personajes)
        elif opcion == 'B':
            stark_listar_personajes(lista_personajes)
        elif opcion == 'C':
            stark_buscar_personaje(lista_personajes)
        elif opcion == 'D':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
'''


stark_marvel_app_5()


if __name__ == "__main__":
    limpiar_consola()
    stark_marvel_app_5(lista_personajes)
