'''

11

Crea un diccionario que represente una lista de tareas por hacer. 
Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado 
(los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado


tareas_por_hacer = {
    'limpiar': 'pendiente',
    'dormir': 'completada',
    'comer': 'proceso'
}



for tarea, estado in tareas_por_hacer.items():
    # print(f'Tarea: {tarea}, Estado: {estado}')
    
    
'''
'''
    # 12

    # Crea un diccionario que represente una lista de las compras. Cada clave del diccionario debe ser el nombre de un producto
    # y cada valor debe ser su cantidad. Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad

    compras_dict = {
        'pan': 2,
        'banana': 5,
        'leche': 7,
    }

    producto_verificar = input('Ingrese el nombre del producto')

    if producto_verificar in compras_dict:
        cantidad = compras_dict[producto_verificar]
        # print(f'la cantidad de {producto_verificar} es {cantidad}')
    else:
        print(f'El producto no se encontro')
'''

'''
    # 13
    # Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa.
    # Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres

    juegos_de_mesa = {
        'monopoly': 'facil',
        'crisis': 'medio',
        'ajedrez': 'dificil',
        'ludo': 'facil',
        'poker': 'medio',
    }

    dificultad_ingresado = input(
        'Ingrese la dificultad (facil),(medio),(dificil)')

    juegos_coincidentes = []

    for juego, dificultad in juegos_de_mesa.items():

        if dificultad_ingresado == dificultad:

            juegos_coincidentes.append(juego)

    if juegos_coincidentes:
        print(f'Juegos de nivel {dificultad_ingresado}')

        for juego in juegos_coincidentes:

            print(juego)
'''

'''
# 14
# Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego.
# Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.

nombres = {
    'pepe': 1000,
    'dardo': 500,
    'moni': 100,
}

nombre_ingresado = input('Ingrese el nombre del jugador')

puntaje_ingresado = input('Ingrese el puntaje')

for nombre in nombres:

    if nombre_ingresado in nombres:
        nombres[nombre_ingresado] = puntaje_ingresado
    else:
        print(f'El jugador no existe en la lista')


for clave, valor in nombres.items():

    print(f'El jugador {clave} tiene el puntaje {valor}')


'''
# 15
# Crea un diccionario que contenga el nombre y el sueldo de varios empleados.
# Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el valor correspondiente en el diccionario.

'''
nombre_sueldo_dicc = {
    'pepe': 1000,
    'dardo': 10000,
    'moni': 100,
}

nombre_ingresado = input('Ingrese el nombre del empleado')

sueldo_ingresado = input('Ingrese el sueldo del empleado')

for nombre in nombre_sueldo_dicc:

    if nombre_ingresado in nombre_sueldo_dicc:
        nombre_sueldo_dicc[nombre_ingresado] = sueldo_ingresado
    else:
        print(f'No se encontro el empleado')


for nombre, sueldo in nombre_sueldo_dicc.items():

    print(f'El empleado es {nombre} y su sueldo es {sueldo}')
    
'''


# 16
# Crea un diccionario que represente una lista de tareas pendientes, donde las claves son las tareas
# y los valores son "True" si están completadas y "False" si no lo están. Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada.
# Imprimir el listado de tareas pendientes

'''
tareas_pendientes = {
    'dormir': False,
    'comer': True,
    'limpiar': True,

}


for tarea, completada in tareas_pendientes.items():

    if completada:
        estado = 'completada'
    else:
        estado = 'pendiente'

tarea_ingresada = input('Ingrese el nombre de la tarea que se completo...')

if tarea_ingresada in tareas_pendientes:
    tareas_pendientes[tarea_ingresada] = True
else:
    print(f'La tarea no se encuentra en la lista ')


for tarea, completada in tareas_pendientes.items():

    if completada:
        estado = 'completada'
    else:
        estado = 'pendiente'

    print(estado)
'''


# 17
# Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas y los valores son los horarios correspondientes.
# Modifica el horario de la película "Avengers: Endgame" a las 19:30.
'''

peliculas_cine = {
    "Shrek": "15:00",
    "busqueda implacable": "17:30",
    "goku": "20:00",

}

cambiar_horario = '00:05'

peliculas_cine["goku"] = cambiar_horario

print(peliculas_cine)
'''

# 18
# Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y los valores son las puntuaciones correspondientes.
# Solicita al usuario el nombre de un juego y luego su puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación

'''
juegos_consola = {
    "mortal kombat": 90,
    "god of war": 95,
    "pes": 88,
    "lego": 92,
}

juego_ingresado = input('Ingrese el juego')
puntaje_ingresado = input('Ingrese el puntaje')


if juego_ingresado in juegos_consola:

    juegos_consola[juego_ingresado] = puntaje_ingresado
else:
    juegos_consola[juego_ingresado] = puntaje_ingresado


for juego, puntaje in juegos_consola.items():

    print(f'El juego es {juego} y el puntaje es {puntaje}')
'''


# 19
# Crea un diccionario que represente las temperaturas de una ciudad durante una semana, donde las claves son los días de la semana y
# los valores son las temperaturas correspondientes. Calcula la temperatura promedio de la semana.

'''
temperaturas_semana = {
    "Lunes": 25,
    "Martes": 28,
    "Miércoles": 27,
    "Jueves": 30,
    "Viernes": 29,
    "Sábado": 31,
    "Domingo": 26,
}

sum_temperatura = 0

for temperatura in temperaturas_semana.values():

    sum_temperatura += temperatura


promedio = sum_temperatura / 7

print(promedio)
'''

# 20

# Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos
# y los valores son "True" si están ocupados y "False" si no lo están. Solicita al usuario un número de asiento y modifica su valor para marcarlo como ocupado.
# Luego imprimí la lista de asientos libres

'''
asientos_avion = {
    "1A": False,
    "1B": False,
    "2A": False,
    "2B": False,
    "3A": False,
    "3B": False,
    "4A": False,
    "4B": False,
    "5A": False,
    "5B": False,
}


numero_asiento_ingresado = input('ingrese su numero de asiento')

if numero_asiento_ingresado in asientos_avion:
    asientos_avion[numero_asiento_ingresado] = True
    print(f'se reservo tu asiento')
else:
    print('El numero de asiento no existe')
'''


# 21


# Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías
# y los valores son los gastos correspondientes. Calcula el total de gastos de la persona.
'''
gastos_persona = {
    "Comida": 200,
    "Transporte": 100,
    "Entretenimiento": 50,
    "Compras": 300,
    "Facturas": 150,
}

total_gastos = 0

for articulos in gastos_persona.values():
    total_gastos += articulos


print(total_gastos)
'''
# 22
# Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y los valores son los gastos correspondientes.
# Calcula el total de gastos de la persona en el mes.


'''
gastos_persona = {
    "Comida": 200,
    "Transporte": 100,
    "Entretenimiento": 50,
    "Compras": 300,
    "Facturas": 150,
}

total_gastos = 0

for articulos in gastos_persona.values():
    total_gastos += articulos

total_mes = total_gastos * 31

print(total_gastos)

'''

# 23
# Crea un diccionario que represente los contactos de un teléfono, donde las claves son los nombres de las personas
# y los valores son los números de teléfono correspondientes. Solicitar al usuario el nombre de un contacto: agregarlo al diccionario en caso de que no exista.
# En caso de que exista modificar el número de teléfono del contacto.

'''

contactos = {"Juan": "123-456-7890",
             "María": "987-654-3210",
             "Pedro": "555-555-5555"}


nombre_ingresado = input('Ingrese el nombre del contacto...')

numero_ingresado = input('Ingrese el numero')

if nombre_ingresado in contactos:
    contactos[nombre_ingresado] = numero_ingresado
else:
    contactos[nombre_ingresado] = numero_ingresado

for nombre, telefono in contactos.items():

    print(f'{nombre} {telefono}')

'''
