
from datos_stark_03 import lista_personajes
import os

'''
def limpiar_consola():
    _ = input('Presione Enter para continuar...')
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')


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

# Función para mostrar el menú principal y validar la entrada del usuario


def stark_menu_principal_2():
    while True:
        limpiar_consola()
        imprimir_menu_2()
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion <= 14:
                return opcion
        print("Opción no válida. Intente nuevamente.")

# Función para imprimir un dato (lista en este caso)


def imprimir_dato(dato: list) -> None:
    print(dato)

# Función principal que ejecuta las opciones seleccionadas por el usuario


def stark_marvel_app_2():
    while True:
        opcion = stark_menu_principal_2()

        if opcion == 1:
            print("\nSuperhéroes de género M:")
            imprimir_dato(mostrar_nombre_genero(lista_personajes, 'M'))
        elif opcion == 2:
            print("\nSuperhéroes de género F:")
            imprimir_dato(mostrar_nombre_genero(lista_personajes, 'F'))
        elif opcion == 3:
            print("\nSuperhéroe más alto de género M:")
            altura, nombre = determina_superheroe_mas_alto_genero(
                lista_personajes, 'M')
            if altura is not None:
                imprimir_dato(
                    f"El superhéroe más alto de género masculino es {nombre} con una altura de {altura} cm.")
            else:
                imprimir_dato(
                    "No se encontraron superhéroes de género masculino en la lista.")
        elif opcion == 4:
            imprimir_dato("\nSuperhéroe más alto de género F:")
            altura, nombre = determina_superheroe_mas_alto_genero(
                lista_personajes, 'F')
            if altura is not None:
                imprimir_dato(
                    f"El superhéroe más alto de género femenino es {nombre} con una altura de {altura} cm.")
            else:
                imprimir_dato(
                    "No se encontraron superhéroes de género femenino en la lista.")
        # Agregar el resto de las opciones aquí...

        elif opcion == 0:
            imprimir_dato("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            imprimir_dato("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    limpiar_consola()
    stark_marvel_app_2()
'''


def imprimir_dato(dato: list) -> None:
    print(dato)


def obtener_nombre(heroe: dict) -> str:

    for heroe in lista_personajes:

        nombre = heroe.get('nombre', 'nombre no encontrado')

    return f'Nombre:{nombre}'


for heroe in lista_personajes:
    nombre_formateado = obtener_nombre(heroe)

# 1.1 Crear la función 'es género' la cual recibirá como parámetros:


def es_genero(heroe: dict, genero_buscado: str) -> bool:

    for heroe in lista_personajes:
        genero_heroe = heroe.get('genero', 'No se encontro')
        if genero_heroe == genero_buscado:
            return True
    return False


# 1.2
'''
Crear la función 'stark_imprimir_heroe_genero' la cual recibirá como parámetros:

La lista de héroes
Un string el cual representará el género a evaluar (el string puede ser M,  F o N ). Deberá imprimir solamente los héroes  que coincidan con el género pasado por parámetro.

Se deberá reutilizar las funciones 'es_genero', 'obtener_nombre' e 'imprimir_dato'.


La función no retorna nada.

'''


def stark_imprimir_heroe_genero(lista_personajes: list[dict], genero_buscado: str) -> None:

    for heroe in lista_personajes:

        if es_genero(heroe, genero_buscado):
            nombre_heroe = obtener_nombre(heroe)
            imprimir_dato(nombre_heroe)


# 2.1
'''
Crear la función 'calcular_min_genero' la cual recibirá como parámetros:


La lista de héroes. 
Un string para representar el dato que deberá ser evaluado a efectos de determinar cuál es el máximo de la lista (por ejemplo: “altura”, “peso”, etc)
Un string para representar el género (el string puede ser M,  F o NB )


La función deberá retornar el héroe que cumpla la condición de tener el mínimo del género especificado

'''


def calcular_min_genero(lista_personajes: list[dict], dato_buscar: str, genero_buscar):

    min_heroe = None

    for heroe in lista_personajes:

        if heroe.get('genero', 'No se encontro genero') == genero_buscar:

            valor_minimo = float(
                heroe.get(dato_buscar, 'No se encontro dato'))

            if min_heroe == None or valor_minimo < min_heroe:

                min_heroe = valor_minimo

                nombre_heroe_min = obtener_nombre(heroe)

    return nombre_heroe_min


# 2.2

def calcular_max_genero(lista_personajes: list[dict], dato_buscar: str, genero_buscar):

    max_heroe = None

    for heroe in lista_personajes:

        if heroe.get('genero', 'No se encontro genero') == genero_buscar:

            valor_maximo = (
                heroe.get(dato_buscar, 'No se encontro dato'))

            if max_heroe == None or valor_maximo > max_heroe:

                max_heroe = valor_maximo

                nombre_heroe_max = obtener_nombre(heroe)

    return nombre_heroe_max


# 2.3

'''
Crear la funcion 'calcular_max_min_dato_genero' la cual recibiá como  parámetros:


La lista de héroes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores maximo o minimo
Un string que representa la key del dato a calcular, por ejemplo: altura, peso, edad, etc.
Un string para representar el género (el string puede ser M,  F o NB )

La función deberá retornar el héroe que cumpla con la condición pedida. Reutilizar las funciones hechas en los puntos 2.0 y 2.1
Ejemplo de llamada:
calcular_max_min_dato(lista,  "maximo", “F” "edad")
'''


def calcular_max_min_dato_genero(lista_personajes: list[dict], tipo_calculo: str, dato_buscar, genero_buscar):

    if tipo_calculo == 'maximo':
        return (calcular_max_genero(lista_personajes, dato_buscar, genero_buscar))

    elif tipo_calculo == 'minimo':
        return (calcular_min_genero(lista_personajes, dato_buscar, genero_buscar))

    else:
        return None


# 2.4

'''
Crear la función 'stark_calcular_imprimir_heroe_genero' la cual recibirá como parámetros: 


La lista de héroes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores maximo o minimo
Un string para representar el género (el string puede ser M,  F o NB )
Un string que representa la key del dato a calcular, por ejemplo: altura, peso, edad, etc.
La función deberá obtener el héroe que cumpla dichas condiciones, imprimir su nombre y el valor calculado. 

Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.

Reutilizar las funciones calcular_max_min_dato_genero,  obtener_nombre_y_dato y imprimir_dato


'''


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

    # imprimir_dato(resultado_formateado)


resultado = stark_calcular_imprimir_heroe_genero(
    lista_personajes, "maximo", "peso", "F")
if resultado == -1:
    print("La lista de héroes está vacía.")


# 3.1
'''
Crear la función sumar_dato_heroe_genero la cual recibirá como parámetros:
La lista de héroes
Un string que representa la key del dato a calcular, por ejemplo: altura, peso, edad, etc.
Un string para representar el género (el string puede ser M,  F o NB )

La función deberá devolver la suma total del dato recibido como parámetro de todos los héroes del género especificado.
Antes de realizar el cálculo se deberá validar:
El tipo de dato del héroe debe ser diccionario.
El héroe actual de la iteración no debe estar vacío (ser diccionario vacío)
 El género del héroe debe coincidir con el pasado por parámetro.
Una vez que cumpla con las condiciones se  podrá realizar la suma.

'''


def sumar_dato_heroe_genero(lista_personajes: list[dict], dato_calcular: str, genero_buscar: str):

    suma_total = 0

    for heroe in lista_personajes:
        # isistance verifica que sea del tipo dict , bool verifica que no este vacio
        if isinstance(heroe, dict) and bool(heroe):

            if heroe.get('genero') == genero_buscar:

                valor_dato = heroe.get(dato_calcular, 0)

                valor_dato = float(valor_dato)
                suma_total += valor_dato

    return suma_total


# print(sumar_dato_heroe_genero(lista_personajes, 'peso', 'M'))

# 3.2
'''
Crear la función 'cantidad_heroes_genero' la cual recibirá como parámetros: 
La lista de héroes 
Un string que representa el género a buscar.
La función deberá iterar y sumar la cantidad de héroes que cumplan con la condición de género pasada por parámetro.

La función deberá retornar la suma de los héroes según el género especificado

'''


def cantidad_heroes_genero(lista_personajes: list[dict], genero_buscar: str):

    cantidad = 0

    for heroe in lista_personajes:

        if heroe.get('genero') == genero_buscar:

            cantidad += 1

    return cantidad


# 3.3
'''
Crear la función 'calcular_promedio_genero' la cual recibirá como parámetros: 
La lista de héroes 
Un string que representa la key del dato a calcular, por ejemplo: altura, peso, edad, etc.
Un string que representa el género a buscar.
Se deberá reutilizar las funciones: 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y 'dividir'

La función deberá retornar el promedio obtenido, según la key y género pasado por parámetro.

'''


def dividir(dividendo, divisor):
    if divisor == 0:
        return 0
    return dividendo / divisor


def calcular_promedio_genero(lista_personajes: list[dict], dato_calcular: str, genero: str):

    suma = sumar_dato_heroe_genero(lista_personajes, dato_calcular, genero)

    cantidad = cantidad_heroes_genero(lista_personajes, genero)

    promedio = dividir(suma, cantidad)

    return promedio


# print(calcular_promedio_genero(lista_personajes, 'altura', 'M'))


# 3.4

'''

Crear la función 'stark_calcular_imprimir_promedio_altura_genero' la cual recibirá como parámetros:

La lista de héroes 
Un string que representa la key del dato a calcular, por ejemplo: altura, peso, edad, etc.
Un string que representa el género a buscar.
Se deberá validar antes de hacer nada que la lista no esté vacía. En caso de estarlo se deberá imprimir el mensaje: "Error: Lista de héroes vacía"
En caso de no estar vacía, calcular el promedio e imprimir formateado al estilo:
"Altura promedio genero F: 178.45"


Reutilizar las funciones: 'calcular_promedio_genero' e 'imprimir_dato'


'''


def stark_calcular_imprimir_promedio_altura_genero(lista_personajes: list[dict], dato_calcular: str, genero: str):

    if not lista_personajes:
        return 'Error: Lista de héroes vacía'

    promedio = calcular_promedio_genero(
        lista_personajes, dato_calcular, genero)

    imprimir_dato(f'Altura promedio genero {genero}: {promedio:.2f}')


# print(stark_calcular_imprimir_promedio_altura_genero(
#     lista_personajes, 'peso', 'M'))


# 4.1
'''
Crear la función 'calcular_cantidad_tipo' la cual recibirá como parámetros:

La lista de héroes
Un string que representa el tipo de dato/key a buscar (color_ojos, color_pelo, etc)

Antes de realizar cualquier cálculo se deberá validar que la lista no esté vacía

La función deberá retornar un diccionario con los distintos valores del tipo de dato recibido por parámetro y la cantidad de cada uno   (crear un diccionario clave valor)

Por ejemplo, si el tipo de dato fuese color_ojos, devolverá un diccionario de la siguiente manera:

'''


def calcular_cantidad_tipo(lista_personajes: list[dict], dato_buscar: str):

    if not lista_personajes:
        return 'La lista esta vacia'

    valores_unicos = {}

    for heroe in lista_personajes:

        dato = heroe.get(dato_buscar)

        if dato is not None:

            if dato not in valores_unicos:
                # si el dato no esta lo agrega al diccionario
                valores_unicos[dato] = 1

            else:
                # si existe le suma una
                valores_unicos[dato] += 1

    return valores_unicos


# print(calcular_cantidad_tipo(lista_personajes, 'color_ojos'))


# 4.2
'''
 Crear la funcion 'imprimir_cantidad_heroes_tipo' la cual solamente recibirá como parámetros:

Un diccionario que representara las distintas variedades del tipo de dato (distintos colores de ojos, pelo, etc) como clave con sus respectivas cantidades como valor.


Un string que representa el tipo de dato (color_pelo, color_ojos, etc): el cual tendrás que  usarlo únicamente en el mensaje final formateado.

La función deberá iterar cada key del diccionario y variabilizar dicha key con su valor para luego formatearlos en un mensaje el cual deberá imprimir.


Por ejemplo:
 "Característica: color_ojos Blue - Cantidad de héroes: 9"

Reutilizar la función 'imprimir_dato'

'''


def imprimir_cantidad_heroes_tipo(valores_tipo: dict, tipo_dato: str):

    for valor, cantidad in valores_tipo.items():

        mensaje = f'Característica: {valor} - Cantidad de héroes: {cantidad}'
        imprimir_dato(mensaje)


diccionario_valores = calcular_cantidad_tipo(lista_personajes, 'color_pelo')

(imprimir_cantidad_heroes_tipo(diccionario_valores, 'color_pelo'))
