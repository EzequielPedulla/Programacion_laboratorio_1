
class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:

        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f'Hola estoy hablando')

# herencia multiple


class Artista:
    def __init__(self, habilidad):

        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return (f'Mi habilidad es: {self.habilidad}')

# de dos clases diferentes heredamos , diferentes propiedades


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa) -> None:
        super().__init__(nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)

        self.salario = salario
        self.empresa = empresa

    # para clase padre se utiliza super() y para la clase actual self
    def presentarse(self):
        print(
            f'hola soy : {self.nombre}, y mi habilidad es {super().mostrar_habilidad()} y trabajo en {self.empresa}')


EmpleadoArtista = EmpleadoArtista(
    'roberto', 20, 'Argentino', 'Cagar', 20000, 'Hostia')


print(EmpleadoArtista.presentarse())

# la clase empleado hereda todos los atributos y metodos de la clase padre (persona)


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario) -> None:
        # super hereda los atributos de persona a empleado, y agrega nuevos a empleado
        super().__init__(nombre, edad, nacionalidad)

        self.trabajo = trabajo
        self.salario = salario

    # sobrescribe el metodo de persona
    def hablar(self):
        print('no')


class Estudiante(Persona):

    def __init__(self, nombre, edad, nacionalidad, notas, universidad) -> None:
        super().__init__(nombre, edad, nacionalidad)

        self.notas = notas
        self.universidad = universidad


roberto = Empleado('Roberto', 43, 'Argentino', 'programador', 100000)

# print(roberto.hablar())


herencia = issubclass(Artista, Persona)

# pregunta true o false de si es una instancia
instancia = isinstance(roberto, Persona)

print(instancia)
