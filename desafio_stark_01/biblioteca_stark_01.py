

from datos_stark_01 import lista_personajes
import os

"""
A
Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
"""


def mostrar_nombre_genero(lista_personajes: list[dict], genero) -> list:

    for personaje in lista_personajes:

        if personaje['genero'] == genero:
            print(personaje['nombre'])


# mostrar_nombre_genero(lista_personajes, 'F')
# nombres_genero_masculino = mostrar_nombre_genero(lista_personajes, 'M')


"""
B
Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
"""

# mismo funcionamineto con lambda


def filtrar_nombre_genero(lista_personaje: list, genero: str):

    personajes_filtrados = list(filter(
        lambda x: x['genero'] == genero, lista_personajes))  # filtra los personajes mediante funcion lambda

    for personaje in personajes_filtrados:
        print(personaje['nombre'])


# nombre_generos_fem = filtrar_nombre_genero(lista_personajes, 'F')
# filtrar_nombre_genero(lista_personajes, 'M')


"""
c
Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
"""


def determina_superheroe_mas_alto_genero(lista_personajes, genero):
    superheroe_mas_alto = None

    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            altura_personaje = personaje.get('altura', 'No se encontro')
            altura_personaje = float(altura_personaje)

            if superheroe_mas_alto is None or altura_personaje > superheroe_mas_alto:
                superheroe_mas_alto = altura_personaje
                nombre_mas_alto_genero_M = personaje.get('nombre', '')

    return superheroe_mas_alto, nombre_mas_alto_genero_M


superheroe_mas_alto_genero_M, nombre_mas_alto_genero_M = determina_superheroe_mas_alto_genero(
    lista_personajes, 'M')

if superheroe_mas_alto_genero_M is not None:
    print(
        f"El superhéroe más alto de género masculino es {nombre_mas_alto_genero_M} con una altura de {superheroe_mas_alto_genero_M} cm.")
else:
    print("No se encontraron superhéroes de género masculino en la lista.")

"""
d
Recorrer la lista y determinar cuál es el superhéroe más alto de género F 

"""

superheroe_mas_alto_genero_f, nombre_mas_alto_genero_f = determina_superheroe_mas_alto_genero(
    lista_personajes, 'F')

if superheroe_mas_alto_genero_f is not None:
    print(
        f"El superhéroe más alto de género femenino es {nombre_mas_alto_genero_f} con una altura de {superheroe_mas_alto_genero_f} cm.")
else:
    print("No se encontraron superhéroes de género femenino en la lista.")


"""
E
Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 

"""


def determina_superheroe_mas_bajo_genero(lista_personajes, genero):
    superheroe_mas_bajo = None
    superheroe_mas_bajo_nombre = None

    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            altura_personaje = personaje.get('altura', 'No se encontro')
            altura_personaje = float(altura_personaje)

            if superheroe_mas_bajo is None or altura_personaje < superheroe_mas_bajo:
                superheroe_mas_bajo = altura_personaje
                superheroe_mas_bajo_nombre = personaje.get(
                    'nombre', 'No se encontro')

    return superheroe_mas_bajo, superheroe_mas_bajo_nombre


superheroe_mas_bajo_genero_m, nombre_mas_bajo_genero_m = determina_superheroe_mas_bajo_genero(
    lista_personajes, 'M')

if superheroe_mas_bajo_genero_m is not None:
    print(
        f"El superhéroe más bajo de género masculino es {nombre_mas_bajo_genero_m} con una altura de {superheroe_mas_bajo_genero_m} cm.")
else:
    print("No se encontraron superhéroes de género masculino en la lista.")


"""
F
Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 

"""


superheroe_mas_bajo_genero_f, nombre_mas_bajo_genero_f = determina_superheroe_mas_bajo_genero(
    lista_personajes, 'F')

if superheroe_mas_bajo_genero_f is not None:
    print(
        f"El superhéroe más bajo de género femenino es {nombre_mas_bajo_genero_f} con una altura de {superheroe_mas_bajo_genero_f} cm.")
else:
    print("No se encontraron superhéroes de género femenino en la lista.")


"""
G
Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
"""


def calcula_altura_promedio_genero(lista_personajes, genero):

    acumulador_altura = 0
    contador_personajes_genero = 0

    for personaje in lista_personajes:

        if personaje['genero'] == genero:

            altura_personaje = personaje.get('altura', 'No se encontro')

            altura_personaje = float(altura_personaje)

            acumulador_altura += altura_personaje

            contador_personajes_genero += 1

    if contador_personajes_genero > 0:

        altura_promedio = acumulador_altura / contador_personajes_genero
    else:
        altura_promedio = 0

    return altura_promedio


altura_promedio_genero_m = calcula_altura_promedio_genero(
    lista_personajes, 'M')

if altura_promedio_genero_m > 0:
    print(
        f"La altura promedio de los superhéroes de género masculino es {altura_promedio_genero_m} cm.")
else:
    print("No se encontraron superhéroes de género masculino en la lista.")


"""
H
Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
"""
altura_promedio_genero_f = calcula_altura_promedio_genero(
    lista_personajes, 'F')

if altura_promedio_genero_f > 0:
    print(
        f"La altura promedio de los superhéroes de género femenino es {altura_promedio_genero_f} cm.")
else:
    print("No se encontraron superhéroes de género femenino en la lista.")


"""
J
Determinar cuántos superhéroes tienen cada tipo de color de ojos.
"""


def determina_cuantos_tipos_de_ojos(lista_personajes):
    contador_color_ojos = {}

    for personaje in lista_personajes:
        color_ojos = personaje.get('color_ojos', 'No se encontro')

        if color_ojos in contador_color_ojos:
            contador_color_ojos[color_ojos] += 1
        else:
            contador_color_ojos[color_ojos] = 1

    return contador_color_ojos


contador_color_ojos = determina_cuantos_tipos_de_ojos(lista_personajes)

# for color, valor in contador_color_ojos.items():
#     print(f"Superhéroes con ojos de color '{color}': {valor}")


"""
K
Determinar cuántos superhéroes tienen cada tipo de color de pelo.
"""


def determina_cuantos_tipo_color_pelo(lista_personajes):

    contador_color_pelo = {}

    for personaje in lista_personajes:
        color_pelo = personaje.get('color_pelo', 'No se encontro')

        if color_pelo in contador_color_pelo:
            contador_color_pelo[color_pelo] += 1
        else:
            contador_color_pelo[color_pelo] = 1

    return contador_color_pelo


contador_color_pelo = determina_cuantos_tipo_color_pelo(lista_personajes)

# for color, valor in contador_color_pelo.items():
#     print(f"Superhéroes color de pelo '{color}': {valor}")


"""
L
Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con No Tiene). 
"""


def determina_tipo_inteligencia(lista_personaje):

    contador_tipo_inteligencia = {}

    for personaje in lista_personajes:
        inteligencia = personaje.get('inteligencia', 'No tiene')

        if inteligencia == '':
            inteligencia = 'no tiene'

        if inteligencia in contador_tipo_inteligencia:
            contador_tipo_inteligencia[inteligencia] += 1
        else:
            contador_tipo_inteligencia[inteligencia] = 1

    return contador_tipo_inteligencia


contador_tipo_inteligencia = determina_tipo_inteligencia(lista_personajes)

for inteligencia, valor in contador_tipo_inteligencia.items():
    print(f"Superhéroes con tipo de inteligencia '{inteligencia}': {valor}")

"""
M
Listar todos los superhéroes agrupados por color de ojos.
"""


def agrupar_superheroes_por_color_ojos(lista_personajes):
    superheroes_por_color_ojos = {}

    for personaje in lista_personajes:
        color_ojos = personaje.get('color_ojos', 'no tiene').capitalize()

        if color_ojos not in superheroes_por_color_ojos:
            superheroes_por_color_ojos[color_ojos] = []

        superheroes_por_color_ojos[color_ojos].append(personaje)

    return superheroes_por_color_ojos


superheroes_por_color_ojos = agrupar_superheroes_por_color_ojos(
    lista_personajes)


for color_ojos, lista_superheroes in superheroes_por_color_ojos.items():
    print(f"Superheroes con color de ojos '{color_ojos}':")
    for heroe in lista_superheroes:
        print(f"- {heroe['nombre']}")
    print()


"""
N
Listar todos los superhéroes agrupados por color de pelo.
"""


def agrupar_superheroes_por_color_pelo(lista_personajes):
    superheroes_por_color_pelo = {}

    for personaje in lista_personajes:
        color_pelo = personaje.get('color_pelo', 'no tiene')

        if color_pelo not in superheroes_por_color_pelo:
            superheroes_por_color_pelo[color_pelo] = []

        superheroes_por_color_pelo[color_pelo].append(personaje)

    return superheroes_por_color_pelo


superheroes_por_color_pelo = agrupar_superheroes_por_color_pelo(
    lista_personajes)


for color_pelo, lista_superheroes in superheroes_por_color_pelo.items():
    print(f"Superheroes con color de pelo '{color_pelo}':")
    for heroe in lista_superheroes:
        print(f"- {heroe['nombre']}")
    print()


"""
O
Listar todos los superhéroes agrupados por tipo de inteligencia
"""


def agrupar_superheroes_por_inteligencia(lista_personajes):
    superheroes_por_inteligencia = {}

    for personaje in lista_personajes:
        inteligencia = personaje.get('inteligencia', 'no tiene')

        if inteligencia not in superheroes_por_inteligencia:
            superheroes_por_inteligencia[inteligencia] = []

        superheroes_por_inteligencia[inteligencia].append(personaje)

    return superheroes_por_inteligencia


superheroes_por_inteligencia = agrupar_superheroes_por_inteligencia(
    lista_personajes)


for inteligencia, lista_superheroes in superheroes_por_inteligencia.items():
    print(f"Superheroes con inteligencia '{inteligencia}':")
    for heroe in lista_superheroes:
        print(f"- {heroe['nombre']}")
    print()


def limpiar_consola():
    '''
    Limpia la consola al presionar la tecla enter.
    '''
    _ = input('Presione Enter para continuar...')
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')


def mostrar_menu():
    while True:
        limpiar_consola()
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

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            print("\nSuperhéroes de género M:")
            mostrar_nombre_genero(lista_personajes, 'M')
        elif opcion == "2":
            print("\nSuperhéroes de género F:")
            mostrar_nombre_genero(lista_personajes, 'F')
        elif opcion == "3":
            print("\nSuperhéroe más alto de género M:")
            altura, nombre = determina_superheroe_mas_alto_genero(
                lista_personajes, 'M')
            if altura is not None:
                print(
                    f"El superhéroe más alto de género masculino es {nombre} con una altura de {altura} cm.")
            else:
                print("No se encontraron superhéroes de género masculino en la lista.")
        elif opcion == "4":
            print("\nSuperhéroe más alto de género F:")
            altura, nombre = determina_superheroe_mas_alto_genero(
                lista_personajes, 'F')
            if altura is not None:
                print(
                    f"El superhéroe más alto de género femenino es {nombre} con una altura de {altura} cm.")
            else:
                print("No se encontraron superhéroes de género femenino en la lista.")
        elif opcion == "5":
            print("\nSuperhéroe más bajo de género M:")
            altura, nombre = determina_superheroe_mas_bajo_genero(
                lista_personajes, 'M')
            if altura is not None:
                print(
                    f"El superhéroe más bajo de género masculino es {nombre} con una altura de {altura} cm.")
            else:
                print("No se encontraron superhéroes de género masculino en la lista.")
        elif opcion == "6":
            print("\nSuperhéroe más bajo de género F:")
            altura, nombre = determina_superheroe_mas_bajo_genero(
                lista_personajes, 'F')
            if altura is not None:
                print(
                    f"El superhéroe más bajo de género femenino es {nombre} con una altura de {altura} cm.")
            else:
                print("No se encontraron superhéroes de género femenino en la lista.")
        elif opcion == "7":
            print("\nAltura promedio de superhéroes de género M:")
            altura_promedio = calcula_altura_promedio_genero(
                lista_personajes, 'M')
            if altura_promedio > 0:
                print(
                    f"La altura promedio de los superhéroes de género masculino es {altura_promedio} cm.")
            else:
                print("No se encontraron superhéroes de género masculino en la lista.")
        elif opcion == "8":
            print("\nAltura promedio de superhéroes de género F:")
            altura_promedio = calcula_altura_promedio_genero(
                lista_personajes, 'F')
            if altura_promedio > 0:
                print(
                    f"La altura promedio de los superhéroes de género femenino es {altura_promedio} cm.")
            else:
                print("No se encontraron superhéroes de género femenino en la lista.")
        elif opcion == "9":
            print("\nCantidad de superhéroes por color de ojos:")
            contador_color_ojos = determina_cuantos_tipos_de_ojos(
                lista_personajes)
            for color, valor in contador_color_ojos.items():
                print(f"Superhéroes con ojos de color '{color}': {valor}")
        elif opcion == "10":
            print("\nCantidad de superhéroes por color de pelo:")
            contador_color_pelo = determina_cuantos_tipo_color_pelo(
                lista_personajes)
            for color, valor in contador_color_pelo.items():
                print(f"Superhéroes con color de pelo '{color}': {valor}")
        elif opcion == "11":
            print("\nCantidad de superhéroes por tipo de inteligencia:")
            contador_inteligencia = determina_tipo_inteligencia(
                lista_personajes)
            for inteligencia, valor in contador_inteligencia.items():
                print(
                    f"Superhéroes con tipo de inteligencia '{inteligencia}': {valor}")
        elif opcion == "12":
            print("\nSuperhéroes agrupados por color de ojos:")
            superheroes_por_color_ojos = agrupar_superheroes_por_color_ojos(
                lista_personajes)
            for color_ojos, lista_superheroes in superheroes_por_color_ojos.items():
                print(f"Superhéroes con color de ojos '{color_ojos}':")
                for heroe in lista_superheroes:
                    print(f"- {heroe['nombre']}")
                print()
        elif opcion == "13":
            print("\nSuperhéroes agrupados por color de pelo:")
            superheroes_por_color_pelo = agrupar_superheroes_por_color_pelo(
                lista_personajes)
            for color_pelo, lista_superheroes in superheroes_por_color_pelo.items():
                print(f"Superhéroes con color de pelo '{color_pelo}':")
                for heroe in lista_superheroes:
                    print(f"- {heroe['nombre']}")
                print()
        elif opcion == "14":
            print("\nSuperhéroes agrupados por tipo de inteligencia:")
            superheroes_por_inteligencia = agrupar_superheroes_por_inteligencia(
                lista_personajes)
            for inteligencia, lista_superheroes in superheroes_por_inteligencia.items():
                print(
                    f"Superhéroes con tipo de inteligencia '{inteligencia}':")
                for heroe in lista_superheroes:
                    print(f"- {heroe['nombre']}")
                print()
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    limpiar_consola()

    mostrar_menu()
