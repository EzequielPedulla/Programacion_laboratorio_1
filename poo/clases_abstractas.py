from abc import ABC, abstractclassmethod

# la clase abstracta es como un modelo de plantilla


class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad) -> None:

        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Hola , me llamo {self.nombre} y tengo {self.edad}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Estoy estudiando {self.actividad}')


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Estoy trabajando {self.actividad}')


ezequiel = Estudiante('ezequiel', 20, 'M', 'Giku')

pedrito = Trabajador('Pedrito', 25, 'M', 'Tocarse')

ezequiel.hacer_actividad()


pedrito.hacer_actividad()
pedrito.presentarse()
