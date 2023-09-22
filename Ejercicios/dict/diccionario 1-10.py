
# 1
dias_semana = {
    'Lunes': 1,
    'Martes': 2,
    'Miercoles': 3,
    'Juevees': 4,
    'Viernes': 5,
}
# print(dias_semana)
# -----------------------------------

# 2
meses_del_año = {
    'Enero': 1,
    'Febrero': 2,
    'Marzo': 3,
    'Abril': 4,
    'Mayo': 5,
    'Junio': 6,
    'Julio': 7,
    'Agosto': 8,
    'Septiembre': 9,
    'Octubre': 10,
    'Noviembre': 11,
    'Diciembre': 12,
}

# print(meses_del_año['Diciembre'])
# --------------------------------------

# 3

informacion_pelicula = {
    'Titulo': 'Shrek',
    'Director': ' Vicky Jenson',
    'Año_estreno': '2001'

}

# print(informacion_pelicula['Titulo'])

# -----------------------------------------

# 4

# Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad, código postal,
# partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.


info_direccion = {
    'nombre calle': 'Calle falsa ',
    'Altura': '123',
    'Localidad': 'Gutierrez',
    'Codigo_postal': '1890',
    'Partido': 'Berazategui',
    'Provincia': 'Buenos Aires',
}
# print(info_direccion['nombre calle'], info_direccion['Altura'])

# -----------------------------------------------------------------------------
# 5


# Crea un diccionario que represente los continentes, donde las claves son los nombres de los continentes y los valores son los números correspondientes
# (por ejemplo, {"América": 1, "Europa": 2, ...}). Imprime el valor correspondiente al continente "África".


continentes = {
    'America': 1,
    'Europa': 2,
    'Africa': 3,
    'Oceania': 4,
    'Asia': 5,
}

# print(continentes['Africa'])

# -----------------------------------------------------------------------------------


# 6

# Crea un diccionario que represente las estaciones del año, donde las claves son los nombres de las estaciones
# y los valores son los números correspondientes (por ejemplo, {"primavera": 1, "verano": 2, ...}). Imprime el valor correspondiente a la estación "invierno".

estaciones_del_año = {
    'Primavera': 1,
    'Verano': 1,
    'Otoño': 1,
    'Invierno': 1,
}

# print(estaciones_del_año['Invierno'])


# --------------------------------------------------------------------


# 7
# Crea un diccionario que contenga la información de una canción: título, artista y duración. Luego, imprime la duración de la canción.

info_cancion = {
    'titulo': 'Satisfaction',
    'Artista': 'Rolling Stones',
    'Duracion': 3.45,
}

# print(info_cancion.get('Duracion'))
# print(info_cancion.get('Duracionad', 'No se encontro')) # para los valores que no se encuentran

# ---------------------------------------------------------------------


# 8 Crea un diccionario que represente las edades de varias personas,
# donde las claves son los nombres de las personas y los valores son sus edades. Imprime la edad de la persona más joven.


personas = {
    'Pepe': 25,
    'Martin': 45,
    'Raul': 48,
    'Moni': 56,
}

# agarra la key con el menor valor
persona_mas_joven = min(personas, key=personas.get)
edad_mas_joven = personas[persona_mas_joven]

# Imprimir la edad de la persona más joven
print(
    f"La persona más joven es {persona_mas_joven} y tiene {edad_mas_joven} años.")


# ------------------------------------------------------------------------------------------

# 9
# Crea un diccionario que contenga las capitales de los países de América del Sur.
# Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.

capitales_paises = {
    'Argentina': 'Buenos Aires',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asuncion',
}

pais_ingresado = input('Ingrese un pais: ')

if pais_ingresado in capitales_paises:
    print(
        f'La capital del pais {pais_ingresado} es {capitales_paises[pais_ingresado]}')
else:
    print(f'El pais ingresado no esta esta')

# -------------------------------------------------------------------------------------

# 10
# Crea un diccionario que represente las notas de un examen de varios estudiantes,
# donde las claves son los nombres de los estudiantes y los valores son sus notas. Imprime el promedio de las notas.


estudiantes = {
    'Pepe': 10,
    'Raul': 5,
    'Marta': 15,
    'Mariano': 10,
}

# suma todos los valores de del dicc estudiantes
suma_notas = sum(estudiantes.values())

cantidad_estudiantes = len(estudiantes)

promedio_notas = suma_notas / cantidad_estudiantes

print(f'La el promedio de las notas es de {promedio_notas}')
