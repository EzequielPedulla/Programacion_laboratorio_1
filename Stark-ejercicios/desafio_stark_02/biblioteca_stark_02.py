from datos_stark_02 import lista_personajes
import os


def stark_normalizar_datos(lista_heroes: list[dict]) -> None:
    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        return

    for heroe in lista_heroes:
        for key, value in heroe.items():
            if key in ["altura", "peso", "fuerza"]:
                try:
                    heroe[key] = float(value)
                except ValueError:
                    pass
    print("Datos normalizados")


# 1.1
def obtener_nombre(heroe: dict) -> str:

    nombre = heroe.get('nombre', 'nombre no encontrado')

    return f'Nombre:{nombre}'


for heroe in lista_personajes:
    nombre_formateado = obtener_nombre(heroe)


# 1.2

def imprimir_dato(dato: list) -> None:
    print(dato)


1.3


def stark_imprimir_nombres_heroes(lista_personajes: list[dict]) -> int:

    if not lista_personajes:

        return -1

    for heroe in lista_personajes:
        nombre_formateado = obtener_nombre(heroe)
        imprimir_dato(nombre_formateado)

    return 0


# 2

def obtener_nombre_y_dato(heroe: dict, key: str) -> str:

    nombre = heroe.get('nombre', 'Nombre no encontrado')

    dato = heroe.get(key, 'Dato no encontrado')

    return f'Nombre: {nombre}: {dato}'


# print(obtener_nombre_y_dato(heroe, 'fuerza'))


# 3

def stark_imprimir_nombres_alturas(lista_personajes: list[dict]) -> int:

    if not lista_personajes:
        return -1

    for heroe in lista_personajes:

        resultado = obtener_nombre_y_dato(heroe, 'altura')

        # print(resultado)

    return 0


# 4.1

def calcular_max(lista_heroes: list[dict], key: str) -> dict:
    if not lista_heroes:
        return {}

    max_hero = max(lista_heroes, key=lambda x: x.get(key, 0))
    return max_hero


# 4.2


def stark_imprimir_nombres_alturas(lista_personajes: list[dict]) -> int:

    if not lista_personajes:
        return -1

    for heroe in lista_personajes:

        resultado = obtener_nombre_y_dato(heroe, 'altura')

        print(resultado)

    return resultado


# 4.1


def calcular_min(lista_heroes: list[dict], key: str) -> dict:
    if not lista_heroes:
        return {}

    min_hero = min(lista_heroes, key=lambda x: x.get(key, 0))
    return min_hero


# 4.3

def calcular_max_min_dato(lista_personajes: list[dict], tipo_calculo: str, key: str):

    if tipo_calculo == 'maximo':
        return calcular_max(lista_personajes, key)

    elif tipo_calculo == 'minimo':
        return calcular_min(lista_personajes, key)
    else:
        return {}


# 4.4


def stark_calcular_imprimir_heroe(
    lista_heroes: list[dict], tipo_calculo: str, key: str
) -> int:
    if not lista_heroes:
        return -1

    heroe = calcular_max_min_dato(lista_heroes, tipo_calculo, key)
    if heroe:
        dato = heroe.get(key, "Dato no encontrado")
        imprimir_dato(
            f"{tipo_calculo.capitalize()} {key}: {obtener_nombre_y_dato(heroe, key)}"
        )
    return 0


print(stark_calcular_imprimir_heroe(lista_personajes, 'maximo', 'peso'))

# 5.1


def sumar_dato_heroe(lista_personajes: list[dict], key: str) -> float:
    suma = 0.0

    for heroe in lista_personajes:
        # Verificamos que el héroe sea un diccionario y tenga la clave key
        if isinstance(heroe, dict) and key in heroe:
            try:
                valor = float(heroe[key])
                suma += valor  # Sumamos el valor al acumulador
            except ValueError:
                pass  # Ignoramos los valores no numéricos

    return suma

# 5.2


def dividir(dividendo, divisor):
    if divisor == 0:
        return 0
    else:
        return dividendo / divisor


# 5.3

def calcular_promedio(lista_personajes, key):

    suma = sumar_dato_heroe(lista_personajes, 'altura')
    cantidad_heroes = len(lista_personajes)

    if cantidad_heroes == 0:
        return 0

    promedio = suma/cantidad_heroes

    return promedio


def stark_calcular_imprimir_promedio_altura(lista_personajes: list[dict]):

    if not lista_personajes:
        return -1

    altura_promedio = calcular_promedio(lista_personajes, 'altura')

    print(f"Altura promedio de los héroes: {altura_promedio:.2f}")


stark_calcular_imprimir_promedio_altura(lista_personajes)


def limpiar_consola():
    '''
    Limpia la consola al presionar la tecla enter.
    '''
    _ = input('Presione Enter para continuar...')
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')


def imprimir_menu() -> None:
    menu = """
    Menú:
    1. Imprimir nombres de héroes
    2. Imprimir nombres y alturas
    3. Calcular e imprimir el héroe con el máximo dato
    4. Calcular e imprimir el héroe con el mínimo dato
    5. Calcular e imprimir el promedio de alturas
    6. Salir
    """
    imprimir_dato(menu)


def validar_entero(numero: str) -> bool:
    return numero.isdigit()


def stark_menu_principal(lista_heroes: list[dict]) -> int:
    while True:
        limpiar_consola()
        imprimir_menu()
        opcion = input("Ingrese el número de la opción deseada: ")
        if validar_entero(opcion):
            opcion = int(opcion)
            if opcion == 1:
                stark_imprimir_nombres_heroes(lista_personajes)
            elif opcion == 2:
                stark_imprimir_nombres_alturas(lista_personajes)
            if opcion == 3:
                stark_calcular_imprimir_heroe(
                    lista_personajes, "maximo", "altura")
            elif opcion == 4:
                stark_calcular_imprimir_heroe(
                    lista_personajes, "minimo", "altura")
            elif opcion == 5:
                stark_calcular_imprimir_promedio_altura(lista_personajes)
            elif opcion == 6:
                print("FIN")
                return 0
            else:
                print("Opción no válida. Intente nuevamente.")
        else:
            print("Opción no válida. Intente nuevamente.")


def stark_marvel_app(lista_personajes: list[dict]) -> None:
    print("Bienvenido a Stark Marvel App")
    stark_menu_principal(lista_personajes)


# Uso de las funciones
if __name__ == "__main__":
    limpiar_consola()
    from datos_stark_02 import lista_personajes

    stark_normalizar_datos(lista_personajes)
    stark_marvel_app(lista_personajes)
