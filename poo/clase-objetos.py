
# una clase contiene lo que va tener el objeto
class Celular():
    marca = 'Samsung'
    modelo = 's23'
    camara = '48px'


# se instancia la clase para crear el objeto
celular1 = Celular()

# print(celular1.modelo)

# ------------------------------------------------------------------------------------------

# creamos la clase y le pasamos los atributos que recibe con el self


class Celular:
    # constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    # metodos (acciones del objeto) se debe poner el self para autorefenciar el objeto

    def llamar(self):
        print(f'estas haciendo un llamado desde un: {self.modelo}')

    def cortar(self):
        print(f'Cortaste la llamada desde tu : {self.modelo}')


# instanciamos la clase y creamos el objeto y le pasamos los valores
celular1 = Celular('Samsung', 'S23', '48MP')
celular2 = Celular('Apple', 'Iphone 15', '358MP')

# print(celular2.llamar())
