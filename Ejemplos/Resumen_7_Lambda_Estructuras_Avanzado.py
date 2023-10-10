'''
Una función lambda en Python es una función anónima y pequeña que se define usando la palabra clave lambda. 
Estas funciones son útiles cuando necesitas una función temporal para realizar una operación simple o para pasar una función como argumento a otra función, como en el caso de las funciones map(), filter(), y sorted().

La sintaxis general de una función lambda es la siguiente:
lambda argumentos: expresion
'''

'''
lambda: Esta palabra clave indica que estás creando una función lambda.

argumentos: Aquí debes especificar los argumentos que la función tomará. 
Puedes tener cero o más argumentos, separados por comas.

expresión: Esta es la expresión que define lo que hará la función. 
La expresión se evalúa y su resultado se devuelve automáticamente como el resultado de la función.
'''

# Una función lambda que suma dos números:
suma = lambda x, y: x + y
resultado = suma(3, 4)
print(resultado)  # Salida: 7


# Una función lambda que verifica si un número es par:
es_par = lambda x: x % 2 == 0
print(es_par(4))  # Salida: True
print(es_par(5))  # Salida: False


# Utilizando funciones lambda con map() para aplicar una operación a cada elemento de una lista:
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]


# Utilizando funciones lambda con filter() para filtrar elementos de una lista:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6, 8, 10]


'''
Las funciones lambda son útiles cuando necesitas una función simple sin tener que definirla por completo utilizando la sintaxis de def. Sin embargo, su uso debe ser moderado, ya que las funciones nombradas definidas con def son más legibles y versátiles para funciones más complejas.
'''

# ---------------------------------------------------------------
# OPERADORES TERNARIOS
# ---------------------------------------------------------------

'''
Los operadores ternarios, también conocidos como operadores condicionales, son una característica en muchos lenguajes de programación que te permiten escribir expresiones condicionales de manera más concisa. En Python, el operador ternario se expresa utilizando la siguiente sintaxis:

valor_si_verdadero if condicion else valor_si_falso
'''

'''
condicion: Una expresión booleana que se evalúa como True o False.

valor_si_verdadero: El valor que se asignará si la condición es True.

valor_si_falso: El valor que se asignará si la condición es False.
'''

'''
El operador ternario evalúa la condición. Si la condición es True, se devuelve valor_si_verdadero; de lo contrario, se devuelve valor_si_falso.
'''

# Asignar un valor a una variable basado en una condición:
edad = 25
estatus = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(estatus)  # Salida: "Mayor de edad"


# Usar el operador ternario en una expresión:
x = 5
y = 10
resultado = x if x > y else y
print(resultado)  # Salida: 10


# Utilizar el operador ternario en una lista por comprensión:
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 if x % 2 == 0 else x for x in numeros]
print(cuadrados)  # Salida: [1, 4, 3, 16, 5]


'''
Los operadores ternarios son útiles para simplificar el código en situaciones en las que deseas realizar una operación basada en una condición, y se utilizan comúnmente en lugar de estructuras if-else cuando la lógica es simple y solo se necesita una asignación rápida y concisa.
'''

# ---------------------------------------------------------------
# LISTAS ANIDADAS
# ---------------------------------------------------------------

'''
Una lista anidada en Python es una lista que contiene una o más listas como sus elementos. Esto significa que puedes tener listas dentro de listas, creando así una estructura de datos multidimensional. Estas listas anidadas pueden ser útiles para representar estructuras de datos más complejas, como matrices, tablas o árboles.
'''

# Crear una lista anidada:
# En este ejemplo, lista_anidada es una lista que contiene tres listas internas.
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Acceder a elementos en una lista anidada:
elemento = lista_anidada[1][1]  # Obtiene el elemento en la segunda lista interna (índice 1) y en la segunda posición (índice 1).
print(elemento)  # Salida: 5


# Modificar elementos en una lista anidada:
lista_anidada[0][0] = 10
print(lista_anidada)  # Salida: [[10, 2, 3], [4, 5, 6], [7, 8, 9]]


# Iterar a través de una lista anidada:
for lista_interna in lista_anidada:
    for elemento in lista_interna:
        print(elemento)


# Agregar elementos a una lista anidada:
nueva_lista = [10, 11, 12]
lista_anidada.append(nueva_lista)
print(lista_anidada)  # Ahora `nueva_lista` se encuentra al final de `lista_anidada`.


'''
Las listas anidadas te permiten crear estructuras de datos más complejas y representar datos multidimensionales de manera efectiva en Python. Puedes anidar listas tanto como sea necesario para adaptarse a tus necesidades específicas.
'''

# ---------------------------------------------------------------
# DICCIONARIOS ANIDADOS
# ---------------------------------------------------------------

'''
Los diccionarios anidados en Python son estructuras de datos en las que un diccionario contiene otro diccionario (u otros tipos de datos) como valores asociados a claves específicas. 
Esto permite representar estructuras de datos más complejas y anidadas en Python.
'''

# Crear un diccionario anidado:
diccionario_anidado = {
    'persona1': {
        'nombre': 'Juan',
        'edad': 30,
        'ciudad': 'Bogotá'
    },
    'persona2': {
        'nombre': 'María',
        'edad': 25,
        'ciudad': 'Medellín'
    }
}

# Acceder a elementos en un diccionario anidado:
nombre_persona1 = diccionario_anidado['persona1']['nombre']
print(nombre_persona1)  # Salida: 'Juan'


# Modificar elementos en un diccionario anidado:
diccionario_anidado['persona2']['edad'] = 26
print(diccionario_anidado)


# Iterar a través de un diccionario anidado:
for persona, detalles in diccionario_anidado.items():
    print(f'Persona: {persona}')
    for clave, valor in detalles.items():
        print(f'{clave}: {valor}')


# Agregar elementos a un diccionario anidado:
diccionario_anidado['persona3'] = {
    'nombre': 'Carlos',
    'edad': 35,
    'ciudad': 'Cali'
}

'''
Los diccionarios anidados son especialmente útiles cuando necesitas representar datos estructurados y relacionados entre sí. 
Puedes anidar diccionarios tanto como sea necesario para organizar y manipular datos de manera efectiva en Python.
'''

# ---------------------------------------------------------------
# ZIP()
# ---------------------------------------------------------------

'''
La función zip() en Python es una función incorporada que se utiliza para combinar dos o más iterables, como listas, tuplas o rangos, elemento a elemento, creando así un nuevo iterable que contiene tuplas con elementos emparejados. 
Esta función es útil cuando deseas agrupar datos relacionados de diferentes secuencias.

La sintaxis de zip() es la siguiente:

zip(iterable1, iterable2, ...)

iterable1, iterable2, ...: Los iterables que deseas combinar. 
Puedes proporcionar múltiples iterables separados por comas, y zip() los combinará elemento a elemento.

El resultado de zip() es un objeto zip, que es un iterable. 
Puedes convertir este objeto zip en una lista, tupla u otro iterable según tus necesidades.
'''

# Combinar dos listas en una lista de tuplas:
nombres = ['Juan', 'María', 'Carlos']
edades = [30, 25, 35]

combinados = list(zip(nombres, edades))
print(combinados)  # Salida: [('Juan', 30), ('María', 25), ('Carlos', 35)]


# Recorrer elementos de varias listas al mismo tiempo:
nombres = ['Juan', 'María', 'Carlos']
edades = [30, 25, 35]

for nombre, edad in zip(nombres, edades):
    print(f'{nombre} tiene {edad} años')


# Desempaquetar elementos de una lista de tuplas:
pares = [(1, 'uno'), (2, 'dos'), (3, 'tres')]
numeros, palabras = zip(*pares)

print(numeros)  # Salida: (1, 2, 3)
print(palabras)  # Salida: ('uno', 'dos', 'tres')

'''
Es importante tener en cuenta que zip() se detendrá cuando el iterable más corto se agote.
'''

# ---------------------------------------------------------------
# MAP()
# ---------------------------------------------------------------

'''
La función map() en Python es una función incorporada que se utiliza para aplicar una función a cada elemento de un iterable (como una lista, tupla o rango) y devuelve un objeto map que es un iterable. 

La función map() toma dos argumentos principales: la función que deseas aplicar y el iterable sobre el cual deseas aplicar esa función.

La sintaxis general de map() es la siguiente:

map(función, iterable)
'''

'''
función: La función que deseas aplicar a cada elemento del iterable. 
Puede ser una función definida por el usuario o una función lambda.

iterable: El iterable (lista, tupla, rango, etc.) sobre el cual deseas aplicar la función.
'''

'''
La función map() devuelve un objeto map, que es un iterable. 
Para obtener los resultados en forma de una lista u otro iterable, generalmente lo convertimos a un tipo de dato iterable específico (por ejemplo, una lista) utilizando list(), tuple(), o set().
'''

# Aplicar una función a cada elemento de una lista:
def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]


# Utilizar map() con una función lambda:
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]


# Aplicar una función a cada elemento de una tupla:
def duplicar(x):
    return x * 2

tupla = (1, 2, 3, 4, 5)
resultado = tuple(map(duplicar, tupla))
print(resultado)  # Salida: (2, 4, 6, 8, 10)


# Utilizar map() con múltiples iterables:
lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
resultado = list(map(lambda x, y: x + y, lista1, lista2))
print(resultado)  # Salida: [11, 22, 33]

'''
La función map() es útil cuando deseas aplicar una función a cada elemento de una secuencia y obtener una nueva secuencia con los resultados de esas aplicaciones.
'''

# ---------------------------------------------------------------
# FILTER()
# ---------------------------------------------------------------

'''
La función filter() en Python es una función incorporada que se utiliza para filtrar elementos de un iterable (como una lista, tupla, u otro iterable) en función de una función de prueba (predicado). 
La función de prueba es una función que toma un elemento del iterable como argumento y devuelve True o False. 
Los elementos que cumplen con la condición (aquellos para los cuales la función de prueba devuelve True) se incluyen en el resultado.

La sintaxis general de filter() es la siguiente:

filter(función_de_prueba, iterable)

'''

'''
función_de_prueba: La función que toma un elemento del iterable como argumento y devuelve True o False según una condición específica.

iterable: El iterable (lista, tupla, rango, etc.) del cual deseas filtrar los elementos.
'''

'''
La función filter() devuelve un objeto filter, que es un iterable. Para obtener los resultados en forma de una lista, tupla u otro iterable, generalmente lo convertimos a un tipo de dato iterable específico (por ejemplo, una lista) utilizando list(), tuple(), o set().
'''

# Filtrar números pares de una lista:
def es_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(es_par, numeros))
print(pares)  # Salida: [2, 4, 6, 8, 10]


# Utilizar filter() con una función lambda para filtrar elementos:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6, 8, 10]


# Filtrar palabras que comienzan con una letra específica de una lista de palabras:
def comienza_con_a(palabra):
    return palabra[0].lower() == 'a'

palabras = ['Manzana', 'Banana', 'Naranja', 'Pera', 'Kiwi', 'Aguacate']
palabras_con_a = list(filter(comienza_con_a, palabras))
print(palabras_con_a)  # Salida: ['Manzana', 'Aguacate']


'''
La función filter() es útil cuando deseas seleccionar elementos de un iterable que cumplan con una condición específica y obtener una nueva secuencia con los elementos filtrados.
'''