from datos_stark import lista_personajes

# B Recorrer la lista imprimiendo por consola el nombre de cada superhéroe


def recorrer_nombre_superheroe(lista_personajes: list[dict]):
    nombres_personajes = []

    for personaje in lista_personajes:
        nombre = personaje.get('nombre', 'No se encontro nombre')
        nombres_personajes.append(nombre)

    return nombres_personajes

# C Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo


def recorrer_nombre_superheroe_con_altura(lista_personajes: list[dict]):
    for personaje in lista_personajes:
        nombre = personaje.get('nombre', 'No se encontro nombre')
        altura = personaje.get('altura', 'No se encontro altura')
        print(f'Nombre: {nombre} Altura: {altura}')

# D Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)


def determina_superheroe_mas_alto(lista_personajes: list[dict]):
    superheroe_mas_alto = None
    nombre_mas_alto = None

    for personaje in lista_personajes:
        altura = personaje.get('altura', 0)
        altura = float(altura)

        if superheroe_mas_alto is None or altura > superheroe_mas_alto:
            superheroe_mas_alto = altura
            nombre_mas_alto = personaje.get('nombre', 'No se encontro nombre')

    return superheroe_mas_alto, nombre_mas_alto

# E Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)


def determina_superheroe_mas_bajo(lista_personajes: list[dict]):
    superheroe_mas_bajo = None
    nombre_mas_bajo = None

    for personaje in lista_personajes:
        altura = personaje.get('altura', 0)
        altura = float(altura)

        if superheroe_mas_bajo is None or altura < superheroe_mas_bajo:
            superheroe_mas_bajo = altura
            nombre_mas_bajo = personaje.get('nombre', 'No se encontro nombre')

    return superheroe_mas_bajo, nombre_mas_bajo

# F Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)


def determina_altura_promedio(lista_personajes: list[dict]):
    acumulador_altura_personajes = 0
    contador_personajes = 0

    for personaje in lista_personajes:
        altura = personaje.get('altura', 0)
        altura = float(altura)

        acumulador_altura_personajes += altura
        contador_personajes += 1

    promedio_altura_personajes = acumulador_altura_personajes / contador_personajes

    return promedio_altura_personajes

# G Calcular e informar cual es el superhéroe más y menos pesado


def calcular_mas_pesado(lista_personajes: list[dict]):
    personaje_peso_maximo = None
    nombre_personaje_maximo = None

    for personaje in lista_personajes:
        peso_personaje = personaje.get('peso', 0)
        peso_personaje = float(peso_personaje)

        if personaje_peso_maximo is None or peso_personaje > personaje_peso_maximo:
            personaje_peso_maximo = peso_personaje
            nombre_personaje_maximo = personaje.get(
                'nombre', 'No se encontro nombre')

    return personaje_peso_maximo, nombre_personaje_maximo


def calcular_menos_pesado(lista_personajes: list[dict]):
    personaje_peso_minimo = None
    nombre_personaje_minimo = None

    for personaje in lista_personajes:
        peso_personaje = personaje.get('peso', 0)
        peso_personaje = float(peso_personaje)

        if personaje_peso_minimo is None or peso_personaje < personaje_peso_minimo:
            personaje_peso_minimo = peso_personaje
            nombre_personaje_minimo = personaje.get(
                'nombre', 'No se encontro nombre')

    return personaje_peso_minimo, nombre_personaje_minimo


def pedir_opcion_menu() -> str:
    return input("Elija una opcion: ")


def mostrar_menu() -> str:
    menu = """
    1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    2 - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    3 - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    4 - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    5 - Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
    6 - Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    7 - Calcular e informar cual es el superhéroe más y menos pesado.
    8 - Salir
    """
    print(menu)
    return pedir_opcion_menu()


def main_app(lista_heroes: list[dict]):
    while True:
        opcion_elegida = mostrar_menu()

        if opcion_elegida == "1":
            nombres_superheroes = recorrer_nombre_superheroe(lista_personajes)
            for nombre in nombres_superheroes:
                print(nombre)
        elif opcion_elegida == "2":
            recorrer_nombre_superheroe_con_altura(lista_personajes)
        elif opcion_elegida == "3":
            heroe_mas_alto, nombre_mas_alto = determina_superheroe_mas_alto(
                lista_heroes)
            print(
                f"El superhéroe más alto es {nombre_mas_alto} con una altura de {heroe_mas_alto} cm.")
        elif opcion_elegida == "4":
            super_heroe_mas_bajo, nombre_super_heroe_mas_bajo = determina_superheroe_mas_bajo(
                lista_heroes)
            print(
                f"El superhéroe más bajo es {nombre_super_heroe_mas_bajo} con una altura de {super_heroe_mas_bajo} cm.")
        elif opcion_elegida == "5":
            promedio_altura = determina_altura_promedio(lista_personajes)
            print(
                f"La altura promedio de los superhéroes es {promedio_altura} cm.")
        elif opcion_elegida == "6":
            _, nombre_super_heroe_mas_bajo = determina_superheroe_mas_bajo(
                lista_heroes)
            _, nombre_super_heroe_mas_alto = determina_superheroe_mas_alto(
                lista_heroes)
            print(f"El superhéroe más bajo es {nombre_super_heroe_mas_bajo}")
            print(f"El superhéroe más alto es {nombre_super_heroe_mas_alto}")
        elif opcion_elegida == "7":
            mas_pesado, nombre_mas_pesado = calcular_mas_pesado(
                lista_personajes)
            menos_pesado, nombre_menos_pesado = calcular_menos_pesado(
                lista_personajes)
            print(
                f"El superhéroe más pesado es {nombre_mas_pesado} con un peso de {mas_pesado} kg.")
            print(
                f"El superhéroe menos pesado es {nombre_menos_pesado} con un peso de {menos_pesado} kg.")
        elif opcion_elegida == "8":
            break
        else:
            print('Opcion incorrecta, elija entre 1 y 8')


if __name__ == "__main__":
    main_app(lista_personajes)
