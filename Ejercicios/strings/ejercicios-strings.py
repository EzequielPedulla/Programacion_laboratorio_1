

# 1

def devuelve_mayusculas(palabra: str) -> str.upper:

    palabra_mayuscula = palabra.upper()

    return palabra_mayuscula


# print(devuelve_mayusculas('Hola mundo'))


# 2

def devuelve_minusculas(palabra: str) -> str.lower:

    palabra_mayuscula = palabra.lower()

    return palabra_mayuscula


# print(devuelve_minusculas('Hola mundo'))

# 3

def devuelve_nuevo_str(palabra_1, palabra_2: str) -> str:

    nueva_palabra = f'{palabra_1} {palabra_2}'

    return nueva_palabra


# print(devuelve_nuevo_str('Hola', 'Mundo'))

# 4


def toma_str_devuelve_num_caracteres(palabra: str) -> (str):

    numero_caracteres = len(palabra)

    return numero_caracteres


# print(toma_str_devuelve_num_caracteres('Holaquetal'))

# 5

def toma_str_devuelve_veces_aparece(palabra: str, caracter):

    palabra.count


# 6

def toma_str_devuelve_lista(palabra: str) -> list:

    palabra = palabra.split(',')

    return palabra


# print(toma_str_devuelve_lista('Hola,como,estas '))

# 7


def toma_str_elimina_espacios(palabra: str) -> list:

    palabra = palabra.strip()

    return palabra


# print(toma_str_elimina_espacios('                  Hola,como,estas               '))

# 8


def recibe_nombre_apellido_devuelve_dicc(nombre: str, apellido: str) -> list:

    nombre = nombre.strip()

    apellido = apellido.strip()

    nombre = nombre.capitalize()

    apellido = apellido.capitalize()

    resultado = {
        'nombre': nombre,
        'apellido': apellido,
    }

    return resultado


# print(recibe_nombre_apellido_devuelve_dicc(
#     '             Goku                ', '        KARAto             '))


# 9

def unir_nombres_con_salto_de_linea(nombres: list[str]):

    nombres_unidos = '\n'.join(nombres)

    return nombres_unidos


nombres = ["Juan", "María", "Pedro"]
resultado = unir_nombres_con_salto_de_linea(nombres)

# print(resultado)

# 10


def obtener_mail(nombre: str, apellido: str) -> str:

    inicial = nombre[0]
    dominio = '@utn-fra.com.ar'
    email = f'{inicial}.{apellido}{dominio}'

    return email


# print(obtener_mail('Ezequiel', 'Pedulla'))

# con lambda


def obtener_mail_lambda(
    nombre, apellido): return f'{nombre[0]}.{apellido}@utn-fra.com.ar'


# print(obtener_mail_lambda('Ezequiel', 'Pedulla'))

# 11


def concatenar_palabras(lista_palabras):

    palabras_concatenadas = ', '.join(lista_palabras[:-1])

    resultado = palabras_concatenadas + ' y ' + lista_palabras[-1]

    return resultado


lista_palabras = ["manzanas", "naranjas", "bananas"]
# resultado = concatenar_palabras(lista_palabras)
# print(resultado)


# 12

def ocultar_numero_tarjeta(numero_tarjeta: str):

    if not numero_tarjeta.isdigit():
        return 'el numero de tarjeta no es valido'

    ultimos_cuatro = numero_tarjeta[-4:]

    longitud_oculta = len(numero_tarjeta) - 4

    numeros_ocultos = '*' * longitud_oculta

    resultado = f'{numeros_ocultos} {ultimos_cuatro}'

    return resultado


numero_tarjeta = "1234567890123456"
# resultado = ocultar_numero_tarjeta(numero_tarjeta)
# print(resultado)


# 13

def eliminar_despues_del_arroba(correo):

    partes = correo.split('@')

    nombre_usuario = partes[0]

    return nombre_usuario


correo = "ezequiel@gmail.com"
# resultado = eliminar_despues_del_arroba(correo)
# print(resultado)


# 14

def nombre_dominio(url):

    partes = url.split('.')

    nombre_dominio = partes[1]

    return nombre_dominio


url = 'https://www.ejemplo.com.ar/pagina1'

# print(nombre_dominio(url))

# 15


def filtrar_caracteres_alfabeticos(cadena):

    caracteres_permitidos = ''

    for caracter in cadena:
        if caracter.isalpha() or caracter.isspace():
            caracteres_permitidos += caracter

    return caracteres_permitidos


cadena = "H0l4, m4nd0!"
resultado = filtrar_caracteres_alfabeticos(cadena)
# print(resultado)

# 16


def obtener_acronimo(cadena):

    palabras = cadena.split()

    acronimo = ''

    for palabra in palabras:
        acronimo += palabra[0]

    acronimo = acronimo.upper()

    return acronimo


cadena = "Universidad Tecnológica Nacional Facultad Regional Avellaneda"
resultado = obtener_acronimo(cadena)
# print(resultado)


# 17

def convertir_a_8_bits(numero_binario):

    cadena_8_bits = numero_binario.zfill(8)

    return cadena_8_bits


numero_binario = "101"
resultado = convertir_a_8_bits(numero_binario)
# print(resultado)

# 18


def intercambiar_mayusculas_y_minusculas(cadena):

    cadena = cadena.swapcase()

    return cadena


cadena = "HoLa"
resultado = intercambiar_mayusculas_y_minusculas(cadena)
# print(resultado)


# 19
def contar_digitos(cadena):

    cantidad_digitos = 0

    for caracter in cadena:
        cantidad_digitos += 1

    return cantidad_digitos


cadena = "1234 Hola Mundo"
resultado = contar_digitos(cadena)
# print(f"La cadena '{cadena}' contiene {resultado} dígitos.")


# 20
def unir_direcciones_de_correo(lista_correos):
    # Utilizar el método join para unir las direcciones con punto y coma
    direcciones_unidas = ";".join(lista_correos)

    return direcciones_unidas


# Ejemplo de uso
correos = ["juan@gmail.com",                    "maria@hotmail.com"]
resultado = unir_direcciones_de_correo(correos)
print(resultado)

# 21


def contar_palabras(string):

    palabras = string.split()

    frecuencia_palabras = {}

    for palabra in palabras:

        palabra = palabra.strip()
        palabra = palabra.lower()

        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    return frecuencia_palabras


texto = "Este es un ejemplo. Este es un texto de ejemplo, y este es el final del ejemplo."
resultado = contar_palabras(texto)
print(resultado)
