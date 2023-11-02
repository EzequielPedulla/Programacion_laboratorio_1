import json
import re
import os
from equipo import *
import csv
# Primer parte


def limpiar_consola():
    _ = input('Presione Enter para continuar...')
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')


def mostrar_lista_jugadores(lista_jugadores):
    # iniciamos la lista vacia de jugadores
    lista_jugadores = []
    # iteramos la lista que contiene los jugadores
    for jugador in equipo.jugadores:
        lista_jugadores.append(f'{jugador.nombre} - {jugador.posicion}')

    return lista_jugadores


def mostrar_estadisticas_jugador(equipo, indice):

    # validamos mediente la funcion re.match validamos que sea una cadena de digitos enteros
    if not re.match(r"^\d+$", indice):
        # si no coincide se devuelve none
        print("Índice no válido. Debe ser un número entero.")
        return None

    indice = int(indice)
    # si indice es mayor o igual a 0, y si esta dentro del rango de jugadores
    if 0 <= indice < len(equipo.jugadores):
        # acedemos a los jugadores mediente el indice
        jugador = equipo.jugadores[indice]
        # accedemos a las estadisticas de ese jugador mediante sus atributos
        estadisticas = jugador.estadisticas

        print(f"Estadísticas de {jugador.nombre} - {jugador.posicion}:")
        print(f"Temporadas jugadas: {estadisticas.temporadas}")
        print(f"Puntos totales: {estadisticas.puntos_totales}")
        print(
            f"Promedio de puntos por partido: {estadisticas.promedio_puntos_por_partido}")
        print(f"Rebotes totales: {estadisticas.rebotes_totales}")
        print(
            f"Promedio de rebotes por partido: {estadisticas.promedio_rebotes_por_partido}")
        print(f"Asistencias totales: {estadisticas.asistencias_totales}")
        print(
            f"Promedio de asistencias por partido: {estadisticas.promedio_asistencias_por_partido}")
        print(f"Robos totales: {estadisticas.robos_totales}")
        print(f"Bloqueos totales: {estadisticas.bloqueos_totales}")
        print(
            f"Porcentaje de tiros de campo: {estadisticas.porcentaje_tiros_de_campo}")
        print(
            f"Porcentaje de tiros libres: {estadisticas.porcentaje_tiros_libres}")
        print(
            f"Porcentaje de tiros triples: {estadisticas.porcentaje_tiros_triples}")
    else:
        return "Índice fuera de rango. Debe ser un número válido."


def guardar_estadisticas_en_csv(jugador):

    # construimos el nombre del archivo
    nombre_archivo = f'{jugador.nombre}.csv'
    # abrimos el archivo en modo 'w' modo escritura
    with open(nombre_archivo, mode='w', encoding='utf-8') as archivo_csv:
        # creamos el objeto escritor_csv permite escribir filas en el archivo csv
        # importamos el modulo csv
        escritor_csv = csv.writer(archivo_csv)
        # creamos los encabezados que represetan a las columnas,corresponden a las estadisticas
        encabezados = [
            "nombre", "posición", "temporadas", "puntos totales", "promedio de puntos por partido",
            "rebotes totales", "promedio de rebotes por partido", "asistencias totales", "promedio de asistencias por partido",
            "robos totales", "bloqueos totales", "porcentaje de tiros de campo", "porcentaje de tiros libres", "porcentaje de tiros triples"
        ]
        # mediente el metodo writerow escribimos los encabezados en la primera fila
        escritor_csv.writerow(encabezados)
        # accedemos a las estadisticas mediente el atributo estadisticas
        estadisticas = jugador.estadisticas
        # creamos las filas de datos con las estadisticas del jugador
        fila_datos = [
            jugador.nombre, jugador.posicion, estadisticas.temporadas, estadisticas.puntos_totales, estadisticas.promedio_puntos_por_partido,
            estadisticas.rebotes_totales, estadisticas.promedio_rebotes_por_partido, estadisticas.asistencias_totales, estadisticas.promedio_asistencias_por_partido,
            estadisticas.robos_totales, estadisticas.bloqueos_totales, estadisticas.porcentaje_tiros_de_campo, estadisticas.porcentaje_tiros_libres, estadisticas.porcentaje_tiros_triples
        ]

        escritor_csv.writerow(fila_datos)


def buscar_jugador_por_nombre(equipo, nombre):

    # validamos mediente regex que la cadena ingresada contenga letras ,espacios en blanco y nada mas

    if not re.match(r"^[A-Za-z\s]+$", nombre):
        # si no coincide terminamos
        return 'Nombre no valido. Debe contener solo letras y espacios'

    resultados = []

    for jugador in equipo.jugadores:
        # si el nombre esta en el nombre del jugador accedemos a los logros
        if nombre.lower() in jugador.nombre.lower():

            logros = jugador.logros
            resultados.append((jugador.nombre, logros))
            # guardamos el nombre del jugador en una lista en tuplas con sus logros
    return resultados


def calcular_promedio_puntos_equipo(equipo):

    promedios = []
    # recorremos cada jugador
    for jugador in equipo.jugadores:
        nombre = jugador.nombre
        promedio = jugador.estadisticas.promedio_puntos_por_partido
        # agregamos nombre y promedio a lista promedios
        promedios.append([nombre, promedio])

    # mediante funcion sorted y lambda , ordenamos de forma ascendente por el promedio
    promedios_ordenados = sorted(promedios, key=lambda x: x[1])

    return promedios_ordenados


def mostrar_promedios_ordenados(promedios_ordenados: list):

    print("Promedio de puntos por partido del equipo (ordenados por nombre):")
    for nombre, promedio in promedios_ordenados:
        print(f"{nombre}: {promedio}")


def buscar_jugador_salon_fama(equipo, nombre):

    # mediante regex validamos que sea caracteres validos
    if not re.match(r"^[A-Za-z\s]+$", nombre):
        return 'Nombre no valido. Debe contener solo letras y espacios'

    resultados = []
    # iteramos los jugadores
    for jugador in equipo.jugadores:
        # si el nombre coincide con el de jugador accedemos  los logros
        if nombre.lower() in jugador.nombre.lower():
            logros = jugador.logros

            # si dentro de la lista logros se encuentra miembro de la fama
            if "Miembro del Salon de la Fama del Baloncesto" in logros:
                # agregamos a la lista el nombre
                resultados.append(
                    (jugador.nombre, "Miembro del Salón de la Fama del Baloncesto"))
            else:
                resultados.append((jugador.nombre, 'No es miembro'))

    return resultados


def encontrar_jugador_con_mas_rebotes(equipo):
    # iniciamos la variable en none
    jugador_con_mas_rebotes = None
    maximo_rebotes = 0
    # iteramos los jugadores
    for jugador in equipo.jugadores:
        # guardamos la estadistica de rebotes en la variable
        rebotes = jugador.estadisticas.rebotes_totales
        # si rebotes es mayor a maximo_rebotes , se remplaza el valor
        if rebotes > maximo_rebotes:
            maximo_rebotes = rebotes  # al iniciarla en none el primer iteracion entra al if
            jugador_con_mas_rebotes = jugador.nombre  # guardamos el nombre

    if jugador_con_mas_rebotes:
        print(
            f"El jugador con más rebotes totales es: {jugador_con_mas_rebotes} con {maximo_rebotes} rebotes.")
    else:
        print("No se encontraron datos de rebotes en el equipo.")


def ordenar_y_guardar_csv(equipo):
    lista_jugadores_rebotes = []

    for jugador in equipo.jugadores:
        nombre = jugador.nombre
        promedio_rebotes = jugador.estadisticas.promedio_rebotes_por_partido
        lista_jugadores_rebotes.append((nombre, promedio_rebotes))

    lista_jugadores_rebotes_ordenada = sorted(
        lista_jugadores_rebotes, key=lambda x: x[1], reverse=True)

    for nombre, promedio_rebotes in lista_jugadores_rebotes_ordenada:
        print(f'{nombre}: {promedio_rebotes}')

    return lista_jugadores_rebotes_ordenada


def guardar_jugadores_en_csv(jugadores, nombre_archivo):
    try:
        with open(nombre_archivo, mode='w', encoding='utf-8') as archivo_csv:
            encabezado = ['nombre', 'rebotes totales']
            archivo_csv.write(','.join(encabezado) + '\n')

            for jugador in jugadores:
                nombre = jugador[0]
                rebotes_totales = jugador[1]
                linea = f'{nombre},{rebotes_totales}\n'
                archivo_csv.write(linea)

        print(f'Los datos se guardaron en {nombre_archivo}')
    except Exception as e:
        print(f'Error al guardar datos: {e}')


def guardar_lista_jugadores_en_json(lista_jugadores_rebotes_ordenada):
    nombre_archivo = input(
        'Ingrese el nombre del archivo JSON para guardar los datos: ')

    patron = r'^[a-zA-Z0-9_]+\.json$'

    if re.match(patron, nombre_archivo):
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo_json:
                json.dump(lista_jugadores_rebotes_ordenada, archivo_json)
                print(f'Los datos se han guardado en {nombre_archivo}')
            return nombre_archivo  # Retorna el nombre del archivo
        except Exception:
            print('Error al guardar el archivo')
    else:
        print('Nombre de archivo no válido')


def calcular_suma_robos_y_bloqueos(jugador):
    estadisticas = jugador.estadisticas

    return estadisticas.robos_totales + estadisticas.bloqueos_totales


def ordenar_y_mostrar_jugadores_valor_sumado(equipo, cantidad_jugadores=None):

    lista_jugadores_suma_robos_bloqueos = []

    for jugador in equipo.jugadores:

        nombre = jugador.nombre
        suma_robos_bloqueos = calcular_suma_robos_y_bloqueos(jugador)
        lista_jugadores_suma_robos_bloqueos.append(
            (nombre, suma_robos_bloqueos))

    lista_jugadores_ordenada = sorted(
        lista_jugadores_suma_robos_bloqueos, key=lambda x: x[1], reverse=True)

    if cantidad_jugadores:
        lista_jugadores_ordenada = lista_jugadores_ordenada[:cantidad_jugadores]

    for nombre, suma_robos_bloqueos in lista_jugadores_ordenada:
        print(f'{nombre} : {suma_robos_bloqueos}')

    return lista_jugadores_suma_robos_bloqueos


def calcular_max_valor(jugadores_suma_robos_bloqueos):

    if jugadores_suma_robos_bloqueos:

        # suponemos que el maximo es el primero
        max_valor = jugadores_suma_robos_bloqueos[0][1]
        for nombre, valor in jugadores_suma_robos_bloqueos:
            if valor > max_valor:
                max_valor = valor
        return max_valor


def mostrar_porcentaje_valor_sumado(jugadores_suma_robos_bloqueos):

    if jugadores_suma_robos_bloqueos:
        max_valor = calcular_max_valor(jugadores_suma_robos_bloqueos)

        for nombre, valor in jugadores_suma_robos_bloqueos:
            porcentaje = (valor / max_valor) * 100
            print(f'{nombre} : {porcentaje:.2f} % del valor maximo ')

    else:
        print('la lista esta vacia')
