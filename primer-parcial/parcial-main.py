
from biblioteca import *
from jugador import *
from equipo import Equipo


def imprimir_menu_parcial():

    print("\nMenú:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team")
    print("2. Seleccionar un jugador por su índice y mostrar sus estadísticas")
    print("3. Exportar las estadísticas de un jugador a un archivo CSV")
    print("4. Buscar un jugador por su nombre y mostrar sus logros")
    print("5. Calcular y mostrar el promedio de puntos por partido de todo el equipo")
    print("6. Verificar si un jugador es miembro del Salón de la Fama del baloncesto")
    print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales")
    print("8. Ordenar jugadores por promedio de rebotes y exportar a CSV")
    print("9. ordenar los datos por el jugador que sumando los robos totales más los bloqueos totales")
    print("10. Salir")


def menu_parcial():

    while True:
        limpiar_consola()
        imprimir_menu_parcial()
        opcion = input('Ingrese el número de la opción que desea ejecutar: ')

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 10:
                if opcion == 1:
                    print('Mostrar la lista de todos los jugadores del Dream Team')
                    print(mostrar_lista_jugadores(equipo))
                elif opcion == 2:
                    print(
                        'Seleccionar un jugador por su índice y mostrar sus estadísticas')
                    indice = input('ingrese el indice del jugador: ')
                    resultado = mostrar_estadisticas_jugador(
                        equipo, indice)
                    print(resultado)
                elif opcion == 3:
                    print('Exportar las estadisticas de un jugador a un archivo CSV')
                    indice = input('Ingrese el indice del jugador: ')

                    resultado = mostrar_estadisticas_jugador(
                        equipo, indice)

                    jugador_seleccionado = equipo.jugadores[int(
                        indice)]
                    respuesta = input(
                        '¿Desea guardar las estadísticas en un archivo CSV? (S/N): ')

                    if respuesta.lower() == 's':
                        guardar_estadisticas_en_csv(
                            jugador_seleccionado)
                        print('Se guardo el CSV')
                    else:
                        print('No se guardo el CSV')
                elif opcion == 4:

                    print('Buscar un jugador por su nombre y mostrar sus logros')

                    nombre = input('Ingrese el nombre: ')
                    resultado = buscar_jugador_por_nombre(equipo, nombre)
                    print(resultado)
                elif opcion == 5:
                    print(
                        'Calcular y mostrar el promedio de puntos por partido de todo el equipo')
                    promedios_ordenados = calcular_promedio_puntos_equipo(
                        equipo)
                    mostrar_promedios_ordenados(promedios_ordenados)
                elif opcion == 6:
                    print(
                        'Verificar si un jugador es miembro del Salón de la Fama del baloncesto')
                    nombre = input('Ingrese el nombre del jugador: ')
                    resultado = buscar_jugador_salon_fama(equipo, nombre)
                    print(resultado)
                elif opcion == 7:
                    print(
                        'Calcular y mostrar el jugador con la mayor cantidad de rebotes totales')
                    resultado = encontrar_jugador_con_mas_rebotes(equipo)

                    print(resultado)
                elif opcion == 8:
                    print('Opciones disponibles para la opcion 8: ')
                    print(
                        'A) Ordenar jugadores por promedio de rebotes y mostrar el listado.')
                    print(
                        'B) Ordenar jugadores por promedio de rebotes y exportar a CSV.')
                    print(
                        'C) Exportar la lista de jugadores ordenada por rebotes a un archivo JSON')

                    subopcion = input(
                        'Elija una opcion (A/B/C): ').strip().lower()

                    if subopcion == 'a':
                        lista_jugadores_rebotes_ordenada = ordenar_y_guardar_csv(
                            equipo)
                        mostrar_lista_jugadores(
                            lista_jugadores_rebotes_ordenada)
                    elif subopcion == 'b':
                        lista_jugadores_rebotes_ordenada = ordenar_y_guardar_csv(
                            equipo)
                        nombre_archivo = input(
                            'Ingrese el nombre del archivo: ')

                        guardar_jugadores_en_csv(
                            lista_jugadores_rebotes_ordenada, nombre_archivo)
                    elif subopcion == 'c':

                        print(
                            "c. Exportar la lista de jugadores ordenada por rebotes a un archivo JSON")
                        lista_jugadores_rebotes_ordenada = ordenar_y_guardar_csv(
                            equipo)
                        archivo_json = guardar_lista_jugadores_en_json(
                            lista_jugadores_rebotes_ordenada)

                        if archivo_json:
                            print(
                                f'Los datos se han guardado en {archivo_json}')
                    else:
                        print('Opciono no valida seleccione "A" o "B"')
                elif opcion == 9:
                    print(
                        'Ordenar jugadores por la suma de robos totales y bloqueos totales:')
                    print('A) Ordenar los jugadores por el valor sumado.')
                    print(
                        'B) Listar todos los jugadores ordenados y mostrar el porcentaje de este valor.')
                    print(
                        'C) Crear un filtro para mostrar una cantidad específica de jugadores ordenados.')

                    subopcion = input(
                        'Elija una opcion (A/B/C): ').strip().lower()
                    if subopcion == 'a':
                        lista_jugadores_suma_robos_bloqueos = ordenar_y_mostrar_jugadores_valor_sumado(
                            equipo)

                    if subopcion == 'b':
                        mostrar_porcentaje_valor_sumado(
                            lista_jugadores_suma_robos_bloqueos)

                    if subopcion == 'c':

                        cantidad_jugadores_mostrar = int(input(
                            'Ingrese la cantidad de jugadores que quiere mostrar'))
                        ordenar_y_mostrar_jugadores_valor_sumado(
                            equipo, cantidad_jugadores_mostrar)
            elif opcion == 10:
                break
        else:
            print('Opción no válida. Ingrese un número válido.')


if __name__ == '__main__':

    menu_parcial()
