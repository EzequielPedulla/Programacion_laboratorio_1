

from funciones import *


if __name__ == "__main__":
    heroes = cargar_datos()
    limpiar_consola()

    while True:
        limpiar_consola()
        print("\nMenu:")
        print("1 - Listar los primeros N héroes")
        print("2 - Ordenar héroes por altura [Ascendente o Descendente]")
        print("3 - Ordenar héroes por fuerza [Ascendente o Descendente]")
        print("4 - Buscar héroes por inteligencia [good, average, high]")
        print("5 - Exportar lista ordenada de héroes a CSV")
        print("7 - Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            numero_a_listar = int(
                input('Ingrese el numero de heroes a listar: '))

            listar_primeros_heroes(heroes, numero_a_listar)

        elif opcion == "2":
            orden_a_listar = input(
                'Ingrese [Ascendente o Descendente]: ').strip().lower()
            while orden_a_listar not in ['ascendente', 'descendente']:
                print("Opción no válida. Intente de nuevo.")
                orden_a_listar = input(
                    'Ingrese [Ascendente o Descendente]: ').strip().lower()
            heroes_ordenados = ordenar_heroes_por_atributo(
                heroes, 'altura', orden_a_listar == 'descendente')
            imprimir_heroes_por_atributo(heroes_ordenados, 'altura')
            limpiar_consola()

        elif opcion == "3":

            orden_a_listar = input(
                'Ingrese [Ascendente o Descendente]: ').strip().lower()
            while orden_a_listar not in ['ascendente', 'descendente']:
                print("Opción no válida. Intente de nuevo.")
                orden_a_listar = input(
                    'Ingrese [Ascendente o Descendente]: ').strip().lower()
            heroes_ordenados = ordenar_heroes_por_atributo(
                heroes, 'fuerza', orden_a_listar == 'descendente')
            imprimir_heroes_por_atributo(heroes_ordenados, 'fuerza')
            limpiar_consola()

        elif opcion == "4":

            inteligencia = input(
                'Ingrese nivel de inteligencia [good, average, high]: ').strip().lower()
            while inteligencia not in ['good', 'average', 'high']:
                print("Opción no válida. Intente de nuevo.")
                inteligencia = input(
                    'Ingrese nivel de inteligencia [good, average, high]: ').strip().lower()

            heroes_inteligentes = buscar_heroe_por_inteligencia(
                heroes, inteligencia)

            if heroes_inteligentes:
                print(f'Héroes con nivel de inteligencia {inteligencia}:')
                imprimir_nombres_de_heroes(heroes_inteligentes)
            else:
                print(
                    f'No se encontraron héroes con nivel de inteligencia {inteligencia}')
        elif opcion == "5":

            nombre_archivo = input(
                "Ingrese el nombre del archivo CSV: ").strip()

            ordenar = input(
                "¿Desea ordenar la lista antes de exportar? (Sí/No): ").strip().lower()
            if ordenar == "sí":

                direccion = input(
                    "Ingrese la dirección de orden (ascendente o descendente): ").strip().lower()
                while direccion not in ['ascendente', 'descendente']:
                    print("Opción no válida. Intente de nuevo.")
                    direccion = input(

                        "Ingrese la dirección de orden (ascendente o descendente): ").strip().lower()

                heroes_ordenados = ordenar_heroes_por_atributo(
                    heroes, 'altura', direccion == 'descendente')
            else:
                heroes_ordenados = heroes  # Utilizar la lista sin ordenar

            crear_csv(nombre_archivo, 'w', heroes_ordenados)

            print(f'Lista de héroes exportada a {nombre_archivo}')

        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            limpiar_consola()
