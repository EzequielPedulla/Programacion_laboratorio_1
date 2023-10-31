
class Gato():
    def sonido(self):
        return 'Miau'


class Perro():
    def sonido(self):
        return 'Guau'


def hacer_sonido(animal):
    print(animal.sonido())


# en lenguajes de tipado dinamico hay polimorfismo aunque no hereden de una misma clase
gato = Gato()
perro = Perro()


hacer_sonido(perro)
