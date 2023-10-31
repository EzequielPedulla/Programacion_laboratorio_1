# archivo_de_funciones.py

from datos_stark_03 import lista_personajes
import os


def limpiar_consola():
    _ = input('Presione Enter para continuar...')
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')


def imprimir_dato(dato: list) -> None:
    print(dato)


def obtener_nombre(heroe: dict) -> str:

    nombre = heroe.get('nombre', 'nombre no encontrado')
    return f'Nombre:{nombre}'


def es_genero(heroe: dict, genero_buscado: str) -> bool:

    genero_heroe = heroe.get('genero', 'No se encontro')
    if genero_heroe == genero_buscado:
        return True
    return False


def stark_imprimir_heroe_genero(lista_personajes: list[dict], genero_buscado: str) -> None:
    for heroe in lista_personajes:
        if es_genero(heroe, genero_buscado):
            nombre_heroe = obtener_nombre(heroe)
            imprimir_dato(nombre_heroe)


def calcular_min_genero(lista_personajes: list[dict], dato_buscar: str, genero_buscar):
    min_heroe = None
    for heroe in lista_personajes:
        if heroe.get('genero', 'No se encontro genero') == genero_buscar:
            valor_minimo = float(heroe.get(dato_buscar, 'No se encontro dato'))
            if min_heroe == None or valor_minimo < min_heroe:
                min_heroe = valor_minimo
                nombre_heroe_min = obtener_nombre(heroe)
    return nombre_heroe_min


def calcular_max_genero(lista_personajes: list[dict], dato_buscar: str, genero_buscar):
    max_heroe = None
    for heroe in lista_personajes:
        if heroe.get('genero', 'No se encontro genero') == genero_buscar:
            valor_maximo = (heroe.get(dato_buscar, 'No se encontro dato'))
            if max_heroe == None or valor_maximo > max_heroe:
                max_heroe = valor_maximo
                nombre_heroe_max = obtener_nombre(heroe)
    return nombre_heroe_max


def calcular_max_min_dato_genero(lista_personajes: list[dict], tipo_calculo: str, dato_buscar, genero_buscar):
    if tipo_calculo == 'maximo':
        return calcular_max_genero(lista_personajes, dato_buscar, genero_buscar)
    elif tipo_calculo == 'minimo':
        return calcular_min_genero(lista_personajes, dato_buscar, genero_buscar)
    else:
        return None


def obtener_nombre_y_dato(heroe, key: str) -> dict:
    for heroe in lista_personajes:
        nombre = heroe.get('nombre', 'Nombre no encontrado')
        dato = heroe.get(key, 'Dato no encontrado')
    return {'nombre': nombre, key: dato}


def stark_calcular_imprimir_heroe_genero(lista_personajes: list[dict], tipo_calculo: str, dato_buscar: str, genero_buscar: str):
    if not lista_personajes:
        return -1
    heroe = calcular_max_min_dato_genero(
        lista_personajes, tipo_calculo, dato_buscar, genero_buscar)
    resultado = obtener_nombre_y_dato(heroe, dato_buscar)
    resultado_formateado = f'Nombre: {resultado["nombre"]}, {dato_buscar}: {resultado[dato_buscar]}'
    imprimir_dato(resultado_formateado)


def sumar_dato_heroe_genero(lista_personajes: list[dict], dato_calcular: str, genero_buscar: str):
    suma_total = 0
    for heroe in lista_personajes:
        if isinstance(heroe, dict) and bool(heroe):
            if heroe.get('genero') == genero_buscar:
                valor_dato = heroe.get(dato_calcular, 0)
                valor_dato = float(valor_dato)
                suma_total += valor_dato
    return suma_total


def cantidad_heroes_genero(lista_personajes: list[dict], genero_buscar: str):
    cantidad = 0
    for heroe in lista_personajes:
        if heroe.get('genero') == genero_buscar:
            cantidad += 1
    return cantidad


def dividir(dividendo, divisor):
    if divisor == 0:
        return 0
    return dividendo / divisor


def calcular_promedio_genero(lista_personajes: list[dict], dato_calcular: str, genero: str):
    suma = sumar_dato_heroe_genero(lista_personajes, dato_calcular, genero)
    cantidad = cantidad_heroes_genero(lista_personajes, genero)
    promedio = dividir(suma, cantidad)
    return promedio


def stark_calcular_imprimir_promedio_altura_genero(lista_personajes: list[dict], dato_calcular: str, genero: str):
    if not lista_personajes:
        return 'Error: Lista de héroes vacía'
    promedio = calcular_promedio_genero(
        lista_personajes, dato_calcular, genero)
    imprimir_dato(f'Altura promedio genero {genero}: {promedio:.2f}')


def calcular_cantidad_tipo(lista_personajes: list[dict], dato_buscar: str):
    if not lista_personajes:
        return 'La lista esta vacia'
    valores_unicos = {}
    for heroe in lista_personajes:
        dato = heroe.get(dato_buscar)
        if dato is not None:
            if dato not in valores_unicos:
                valores_unicos[dato] = 1
            else:
                valores_unicos[dato] += 1
    return valores_unicos


def imprimir_cantidad_heroes_tipo(valores_tipo: dict, tipo_dato: str):
    for valor, cantidad in valores_tipo.items():
        mensaje = f'Característica: {valor} - Cantidad de héroes: {cantidad}'
        imprimir_dato(mensaje)


def stark_calcular_cantidad_por_tipo(lista_personajes: list[dict], tipo_dato: str):
    cantidad = calcular_cantidad_tipo(lista_personajes, tipo_dato)
    resultado = imprimir_cantidad_heroes_tipo(cantidad, tipo_dato)
    return resultado


def obtener_lista_de_tipos(lista_personajes: list[dict], tipo_dato: str):
    valores_tipo = []
    for heroe in lista_personajes:
        dato = heroe.get(tipo_dato, 'N/A')
        valores_tipo.append(dato)
    valores_tipo_unicos = []
    for valor in valores_tipo:
        if valor not in valores_tipo_unicos:
            valores_tipo_unicos.append(valor)
    return valores_tipo_unicos


def normalizar_dato(dato_heroe: str, valor_por_defecto):
    if not dato_heroe:
        return valor_por_defecto
    return dato_heroe


def obtener_heroes_por_tipo(lista_personajes: list[dict], tipos_variedades: list, tipo_dato: str):
    heroes_por_variedad = {}
    for variedad in tipos_variedades:
        heroes_por_variedad[variedad] = []
        for heroe in lista_personajes:
            valor_tipo = normalizar_dato(heroe.get(tipo_dato, 'N/A'), 'N/A')
            variedad_normalizada = normalizar_dato(variedad, 'N/A')
            if valor_tipo == variedad_normalizada:
                heroes_por_variedad[variedad].append(
                    heroe.get('nombre', 'No se encontro'))
    return heroes_por_variedad


def imprimir_heroes_por_tipo(heroe_por_variedad: dict[list], tipo_dato: str):
    for key, valor in heroe_por_variedad.items():
        if valor:
            mensaje = f"{tipo_dato} {key}: {' | '.join(valor)}"
        else:
            mensaje = f"{tipo_dato} {key}: No se encontraron heroes"
        imprimir_dato(mensaje)


def stark_listar_heroes_por_dato(lista_personajes: list[dict], tipo_dato: str):
    tipos_variedades = obtener_lista_de_tipos(lista_personajes, tipo_dato)
    heroes_por_variedad = obtener_heroes_por_tipo(
        lista_personajes, tipos_variedades, tipo_dato)
    imprimir_heroes_por_tipo(heroes_por_variedad, tipo_dato)
