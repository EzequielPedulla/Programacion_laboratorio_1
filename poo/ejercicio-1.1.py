

class estudiante:
    def __init__(self, nombre, edad, genero) -> None:

        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def estudiar(self):

        print(f'El estudiante {self.nombre} esta estudiando')


ezequiel = estudiante('Ezequiel', 20, 'M')

print(ezequiel.estudiar())
