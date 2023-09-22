

# 1
# Crear una función que convierta grados Celsius a grados Fahrenheit. Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.


# se crea la funcion recibe como parametro grados celsius
def grados_celsius_a_farenheit(grados_celsius):
    # Fórmula de conversión de Celsius a Fahrenheit: F = (C * 9/5) + 32

    grados_fahrenheit = (grados_celsius * 9/5) + 32

    return grados_fahrenheit


grados_celsius = 24
grados_fahrenheit = grados_celsius_a_farenheit(grados_celsius)

# print(
#     f'El equivalente a {grados_celsius} en fahrenheit es {grados_fahrenheit}')

# ------------------------------------------------------------------------------------

# 2
# Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.


def calcular_area_circulo(radio_circulo):

    area_del_circulo = 3.14 * radio_circulo ** 2

    return area_del_circulo


radio_circulo = 10

area_del_circulo = calcular_area_circulo(radio_circulo)

# print(
#     f'El area del circulo con un radio de {radio_circulo} es de {area_del_circulo}')


# -----------------------------------------------------------------------------------------

# 3
# Crear una función que calcule el descuento aplicado a un producto.
# Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.

def calcular_porcentaje_descuento(precio_original, precio_con_descuento):

    descuento_aplicado = precio_original - precio_con_descuento

    porcentaje_descuento = precio_original * precio_con_descuento / 100

    return porcentaje_descuento


precio_original = 100
precio_descuento = 80

porcentaje_descuento = calcular_porcentaje_descuento(
    precio_original, precio_descuento)

# print(f'el porcentaje de descuento aplicado es {porcentaje_descuento}')


# ----------------------------------------------------------------------------------

# 4
# Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.


def calcular_promedio_edades(lista_edades):

    suma_edades = sum(lista_edades)

    promedio_edades = suma_edades / len(lista_edades)

    return promedio_edades


lista_edades = [10, 50, 60, 30, 10, 50]

promedio_edades = calcular_promedio_edades(lista_edades)


# print(f'El promedio de las edades es de {promedio_edades}')

# ---------------------------------------------------------------------------------------

# 5
# Crear una función que determine si un número es primo o no.
# Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.

# Crear una función que determine si un número es primo o no. Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.


def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Comprobar si el número es divisible por cualquier número en el rango de 2 a la raíz cuadrada del número + 1
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False  # El número es divisible, por lo que no es primo

        return True  # Si no se encontraron divisores, el número es primo

    numero = 7
    resultado = es_primo(numero)

    if resultado:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")


# -----------------------------------------------------------------------

# 6
# Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.

def area_de_triangulo(base_triangulo, altura_triangulo):

    area_de_triangulo = (base * altura) / 2

    return area_de_triangulo


base = 10
altura = 20
resultado = area_de_triangulo(base, altura)

# print(f'el area de una base es {resultado}')

# --------------------------------------------------------------------------------

# 7
# Crear una función que calcule el máximo común divisor de dos números.
# Recibe dos parámetros (números) y devuelve el máximo común divisor.


def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a


numero1 = 48
numero2 = 18
# mcd = calcular_mcd(numero1, numero2)
# print(f"El máximo común divisor de {numero1} y {numero2} es {mcd}.")

# -----------------------------------------------------------------------------------------

# 8
# Crear una función que verifique si un número es par o impar.
# Recibe un número como parámetro y devuelve True si es par o False si es impar.


def es_par_o_impar(numero):

    if numero % 2 == 0:
        return True
    else:
        return False


numero = 10
# if es_par_o_impar(numero):
#     print(f'{numero} es un numero par ')
# else:
#     print(f'El {numero} es impar')

# ---------------------------------------------------------------------------------------------------------

# 9
# Crear una función que cuente la cantidad de veces que aparece un elemento en una lista.
# Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.

lista_nombres = ['pepe', 'moni', 'coqui', 'dardo', 'pepe', 'pepe', 'dardo']


def contador_elemento(lista_nombres, elemento_a_contar):

    contador = 0
    for nombre in lista_nombres:

        if nombre == elemento_a_contar:
            contador += 1

    return contador


elemento_a_contar = 'dardo'
cantidad = contador_elemento(lista_nombres, elemento_a_contar)

# print(f'El nombre {elemento_a_contar} se repite {cantidad} en la lista ')

# ------------------------------------------------------------------------------------------------------------------
