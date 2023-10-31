# los decoradores suelen agregar codigo a las funciones funcionalides antes o despues de ejecutarlas


def decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar a la funcion')
        funcion()
        print('Despues de llamar la funcion')

    return funcion_modificada


# def saludo():
#     print('Hola wigetta')


# saludo_modificado = decorador(saludo)

# saludo_modificado()

@decorador
def saludo():
    print('Hola como andas')


saludo()
