class Persona:
    def __init__(self, nombre, edad) -> None:

        self.__nombre = nombre
        self.__edad = edad
# para llamar un atributo privado creamos el metodo get

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):

        self.__nombre = nuevo_nombre


ezequiel = Persona('Ezequiel', 20)

nombre = ezequiel.nombre
print(nombre)

ezequiel.nombre = 'Gasdasds'

nombre = ezequiel.nombre
print(nombre)
