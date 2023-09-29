import re

textos = ['NATHY PELUSO//BZRP Music Sessions #36',
          'NATHY PELUSO//BZRP Music Sessions #38',
          'NATHY PELUSO//BZRP Music Sessions #335',
          'NATHY PELUSO//BZRP Music Sessions #35',
          'NATHY PELUSO//BZRP Music Sessions #36',
          'NATHY PELUSO//BZRP Music Sessions #36',
          'NATHY PELUSO//BZRP Music Sessions #36',
          'NATHY PELUSO//BZRP Music Sessions #36551',
          ]


patron_de_busqueda = '^[a-zA-Z ]+\|\|[a-zA-Z ]+#[0-9]{1,2}$'

# nombre = ''

# while not re.match(patron_de_busqueda, nombre):
#     nombre = input('Escriba un nombre valido solo letras y espacios')

# print(nombre)

for texto in textos:

    if re.match(patron_de_busqueda, texto):

        print(texto)


fechas = [
    '2023/09/28 10:00:00 PM'
    '2023/09/30 20:30:15'
]

patron_de_busqueda_fecha = '(
)'


for fecha in fechas:

    if re.match(patron_de_busqueda_fecha, fecha):
        print(fecha)
