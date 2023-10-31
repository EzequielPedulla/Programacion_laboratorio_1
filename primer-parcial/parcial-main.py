
from biblioteca import *
from jugador import *


def imprimir_menu_parcial():

    print("\nMenú:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team")
    print("2. Seleccionar un jugador por su índice y mostrar sus estadísticas")
    print("3. Exportar las estadísticas de un jugador a un archivo CSV")
    print("4. Buscar un jugador por su nombre y mostrar sus logros")
    print("5. Calcular y mostrar el promedio de puntos por partido de todo el equipo")
    print("6. Verificar si un jugador es miembro del Salón de la Fama del baloncesto")
    print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales")
    print("8. Salir")


def menu_parcial():
    while True:
        limpiar_consola()
        imprimir_menu_parcial()
        opcion = input('Ingrese el número de la opción que desea ejecutar: ')

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 8:
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
                break
        else:
            print('Opción no válida. Ingrese un número válido.')


menu_parcial()
