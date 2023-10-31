import json

lista_personas = [
    {
        'nombre': 'luis',
        'edad': 25,
        'altura': 1.75,

    },
    {
        'nombre': 'pepe',
        'edad': 27,
        'altura': 1.80,
    },
    {
        'nombre': 'raul',
        'edad': 35,
        'altura': 1.90,
    }
]

base_datos = []

for i in range(3):
    persona = {}
    edad = input('Ingrese la edad :')
    nombre = input('Ingrese el nombre :')

    edad = int(edad)

    persona['nombre'] = nombre
    persona['edad'] = edad
    base_datos.append(persona)


# archivo json

# with open('base_de_datos.json', 'w') as archivo:
#     # se guarda el archivo
#     json.dump(base_datos, archivo)
#     print('Archivo exportado')


# lee la base de datos
with open('base_de_datos.json', 'r') as archivo:

    base_datos = json.load(archivo)

    print('Archivo obtenido con exito')
print(base_datos)
