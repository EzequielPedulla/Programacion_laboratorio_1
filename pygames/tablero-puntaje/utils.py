from data_puntajes import lista_puntajes


def formatear_puntaje(puntaje: str) -> str:

    puntaje_ceros = puntaje.zfill(4)
    return puntaje_ceros


def formatear_nombre_jugador(nombre: str) -> str:

    nombre_formateado = nombre.upper().strip()

    palabras = nombre_formateado.split()

    primer_nombre = palabras[0]

    return primer_nombre


def ordenar_puntajes(lista_puntajes: list[dict]):

    lista_puntajes_ordenada = sorted(
        lista_puntajes, key=lambda puntaje: puntaje['puntaje'], reverse=True)

    return lista_puntajes_ordenada
