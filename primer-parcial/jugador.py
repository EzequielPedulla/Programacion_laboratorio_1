# definimos la clase jugador con sus atributos
class Jugador:
    def __init__(self, nombre, posicion, logros, estadisticas) -> None:

        self.nombre = nombre
        self.posicion = posicion
        self.logros = logros
        self.estadisticas = estadisticas
