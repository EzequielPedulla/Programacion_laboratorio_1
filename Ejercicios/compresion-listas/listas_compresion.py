
import random

'''
Dada una lista de números: 

Crear una nueva lista donde cada número se duplique.
'''


lista_numeros = [10, 2, -5, 30, 50]


lista_duplicados = [numero * 2 for numero in lista_numeros]


'''
Dada una lista de números: 
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Crea una lista que contenga solo los números pares
'''

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


lista_pares = [numero for numero in lista_numeros if numero % 2 == 0]


'''
Dada una lista de nombres:
Crea una lista de las iniciales de cada nombre

'''

lista_nombres = ["Ana", "Juan", "María", "Carlos",
                 "Luisa", "Pedro", "Sofía", "Pablo", "Laura", "Diego"]

lista_iniciales = [nombre[0] for nombre in lista_nombres]


'''
Dada una lista de frutas:

Crea una lista que contenga sólo las palabras que tienen más de 5 letras '''


lista_frutas = ["manzana", "plátano", "naranja", "uva",
                "sandía", "fresa", "kiwi", "pera", "mango", "papaya"]


lista_mas_cinco_letras = [frutas for frutas in lista_frutas if len(frutas) > 5]


'''
Dada una lista de números, 

Crea una lista donde los números impares se elevan al cuadrado y los números pares permanecen sin cambios.'''


lista_numeros = [8, 17, 33, 41, 59, 22, 14, 6, 49, 10]


lista_numeros_impares_al_cuadrado = [
    numero ** 2 if numero % 2 == 1 else numero for numero in lista_numeros]

'''
Dada esta lista:
Crea una lista que contenga solo los valores únicos 
'''
lista_numeros = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]

# count devuelve las veces que se encontro el valor
lista_valores_unicos = [
    numero for numero in lista_numeros if lista_numeros.count(numero) == 1]


'''
Crea una lista que contenga los números del 1 al 1000.'''


lista_numeros = [numero for numero in range(1, 1001)]


'''
Genera una lista que contenga 10 números enteros aleatorios en un rango del 1 al 1000'''

lista_numeros_aleatorios = [random.randint(1, 1000) for numero in range(10)]


'''
Dada una lista de nombres:

Crea una lista que contenga sólo los nombres que comienzan con una consonante

'''
lista_nombres = ["Lourdes", "Ignacio", "Adela", "Roberto",
                 "Marina", "Ramón", "Ezequiel", "Rodrigo", "Beatriz", "Miguel"]


listas_nombres_consonantes = [
    nombre for nombre in lista_nombres if nombre[0].upper() not in 'AEIOUÁÉÍÓÚ']


'''
Dada una lista de nombres:
Crea una lista que contenga sólo las primeras tres letras de los nombres que comienzan con una vocal 
'''
lista_nombres = ["Lourdes", "Ignacio", "Adela", "Roberto",
                 "Marina", "Ramón", "Ezequiel", "Rodrigo", "Beatriz", "Miguel"]


listas_nombre_modificada = [
    nombre[:3] for nombre in lista_nombres if nombre[0].upper() in 'AEIOUÁÉÍÓÚ']
