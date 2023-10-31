class Persona:
    # constructor
    def __init__(self, nombre, edad) -> None:

        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f'persona(nombre={self.nombre},{self.edad})'


goku = Persona('Lucas', 21)


print(goku)
