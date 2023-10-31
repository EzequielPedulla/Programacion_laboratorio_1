from biblioteca_stark_03 import *


def imprimir_menu_2():
    print("\nMenú:")
    print("1. Superhéroes de género M")
    print("2. Superhéroes de género F")
    print("3. Superhéroe más alto de género M")
    print("4. Superhéroe más alto de género F")
    print("5. Superhéroe más bajo de género M")
    print("6. Superhéroe más bajo de género F")
    print("7. Altura promedio de superhéroes de género M")
    print("8. Altura promedio de superhéroes de género F")
    print("9. Cantidad de superhéroes por color de ojos")
    print("10. Cantidad de superhéroes por color de pelo")
    print("11. Cantidad de superhéroes por tipo de inteligencia")
    print("12. Listar superhéroes agrupados por color de ojos")
    print("13. Listar superhéroes agrupados por color de pelo")
    print("14. Listar superhéroes agrupados por tipo de inteligencia")
    print("0. Salir")


def stark_menu_principal_2(lista_personajes):
    while True:
        limpiar_consola()
        imprimir_menu_2()
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion <= 14:
                if opcion == 1:
                    print("\nSuperhéroes de género M:")
                    stark_imprimir_heroe_genero(lista_personajes, 'M')
                elif opcion == 2:
                    print("\nSuperhéroes de género F:")
                    stark_imprimir_heroe_genero(lista_personajes, 'F')
                elif opcion == 3:
                    print("\nSuperhéroe más alto de género M:")
                    stark_calcular_imprimir_heroe_genero(
                        lista_personajes, "maximo", "altura", "M")
                elif opcion == 4:
                    print("\nSuperhéroe más alto de género F:")
                    stark_calcular_imprimir_heroe_genero(
                        lista_personajes, "maximo", "altura", "F")
                elif opcion == 5:
                    print("\nSuperhéroe más bajo de género M:")
                    stark_calcular_imprimir_heroe_genero(
                        lista_personajes, "minimo", "altura", "M")
                elif opcion == 6:
                    print("\nSuperhéroe más bajo de género F:")
                    stark_calcular_imprimir_heroe_genero(
                        lista_personajes, "minimo", "altura", "F")
                elif opcion == 7:
                    print("\nAltura promedio de superhéroes de género M:")
                    stark_calcular_imprimir_promedio_altura_genero(
                        lista_personajes, "altura", "M")
                elif opcion == 8:
                    print("\nAltura promedio de superhéroes de género F:")
                    stark_calcular_imprimir_promedio_altura_genero(
                        lista_personajes, "altura", "F")
                elif opcion == 9:
                    print("\nCantidad de superhéroes por color de ojos:")
                    stark_calcular_cantidad_por_tipo(
                        lista_personajes, 'color_ojos')
                elif opcion == 10:
                    print("\nCantidad de superhéroes por color de pelo:")
                    stark_calcular_cantidad_por_tipo(
                        lista_personajes, 'color_pelo')
                elif opcion == 11:
                    print("\nCantidad de superhéroes por tipo de inteligencia:")
                    stark_calcular_cantidad_por_tipo(
                        lista_personajes, 'tipo_inteligencia')
                elif opcion == 12:
                    print("\nListar superhéroes agrupados por color de ojos:")
                    tipos_variedades = obtener_lista_de_tipos(
                        lista_personajes, 'color_ojos')
                    resultados = obtener_heroes_por_tipo(
                        lista_personajes, tipos_variedades, 'color_ojos')
                    imprimir_heroes_por_tipo(resultados, 'color_ojos')
                elif opcion == 13:
                    print("\nListar superhéroes agrupados por color de pelo:")
                    tipos_variedades = obtener_lista_de_tipos(
                        lista_personajes, 'color_pelo')
                    resultados = obtener_heroes_por_tipo(
                        lista_personajes, tipos_variedades, 'color_pelo')
                    imprimir_heroes_por_tipo(resultados, 'color_pelo')
                elif opcion == 14:
                    print("\nListar superhéroes agrupados por tipo de inteligencia:")
                    tipos_variedades = obtener_lista_de_tipos(
                        lista_personajes, 'tipo_inteligencia')
                    resultados = obtener_heroes_por_tipo(
                        lista_personajes, tipos_variedades, 'tipo_inteligencia')
                    imprimir_heroes_por_tipo(
                        resultados, 'tipo_inteligencia')
                elif opcion == 0:
                    imprimir_dato("Saliendo del programa.")
                    break
            else:
                imprimir_dato("Opción no válida. Intente nuevamente.")
        else:
            imprimir_dato("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    limpiar_consola()
    stark_menu_principal_2(lista_personajes)
