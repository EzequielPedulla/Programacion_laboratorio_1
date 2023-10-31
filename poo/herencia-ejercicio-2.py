

class Persona:
    def __init__(self, nombre, edad) -> None:

        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print(f'Mi nombre es {self.nombre} y mi edad {self.edad}')


class Estudiante(Persona):

    def __init__(self, nombre, edad, grado) -> None:
        super().__init__(nombre, edad)

        self.grado = grado

    def imprimir_grado(self):

        print(f'El grado del estudiante es {self.grado}')


estudiante = Estudiante('Ezequiel', 20, 'A')

# estudiante.imprimir()

# estudiante.imprimir_grado()
