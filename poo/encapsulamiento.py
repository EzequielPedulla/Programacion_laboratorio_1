
class Miclase:
    def __init__(self) -> None:

        # con un guion bajo es privado
        # self._atributo_privados = 'valor'

        # con dos guiones no se puede acceder
        self.__atributo_privados = 'valor'


objeto = Miclase()


# print(objeto.__atributo_privados)


class Persona:
    def __init__(self, nombre, edad) -> None:

        self.__nombre = nombre
        self.__edad = edad
# para llamar un atributo privado creamos el metodo get

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):

        self.__nombre = nuevo_nombre

        return nuevo_nombre


ezequiel = Persona('Ezequiel', 20)

nombre = ezequiel.get_nombre()

print(nombre)


ezequiel.set_nombre('goku')

nombre = ezequiel.get_nombre()

print(nombre)
