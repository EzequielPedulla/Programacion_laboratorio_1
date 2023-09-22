from datos_stark_02 import lista_personajes

# 1


def stark_normalizar_datos(lista_personajes):
    '''
    la función normaliza los datos numéricos en una lista de héroes, convirtiendo las claves que representan datos numéricos
    (edad, altura, peso) al tipo de dato correcto (entero o flotante) 

    recibe lista_personajes

    devuelve: nada
    '''

    if not lista_personajes:
        print("Error: Lista de héroes vacía")
        return

    for persona in lista_personajes:

        for personaje in lista_personajes:
            for key, value in personaje.items():
                if key in ['altura', 'peso', 'fuerza']:
                    try:
                        personaje[key] = float(value)
                    except ValueError:
                        pass
    print('Datos normalizados')


def obtener_nombre(personaje: dict) -> str:
    return f"Nombre: {personaje['nombre']}"


def imprimir_dato(dato: str) -> None:
    print(dato)


def stark_imprimir_nombres_heroes(lista_personajes):
    if not lista_personajes:
        return -1

    for personaje in lista_personajes:
        imprimir_dato = (obtener_nombre(personaje))
        return 0


# --------------------------------------------------------------------------------------------------

def obtener_nombre_y_dato(personaje: dict, key: str) -> str:
    nombre = personaje.get('nombre', 'Nombre no encontrado')
    dato = personaje.get(key, 'Dato no encontrado')
    return f"Nombre: {nombre} | {key}: {dato}"


dato_fuerza = obtener_nombre_y_dato(lista_personajes, 'fuerza')
print(dato_fuerza)  # Esto imprimirá: "Nombre: Venom | fuerza: 500"


def stark_imprimir_nombres_alturas(lista_personaje: list[dict]) -> int:
    pass
