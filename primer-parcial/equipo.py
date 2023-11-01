import json
from jugador import *
from estadisticas import *
# definimos la clase Equipo se va a encargar de cargar la informacion de un archivo json
# ademas de crear objetos de la clase jugador con la informacion


class Equipo:

    def __init__(self, archivo_json) -> None:
        # se inicializa una lista de jugadores
        self.jugadores = []
        # llamamos al metodo de la clase para cargar el json
        self.cargar_desde_json(archivo_json)

    def cargar_desde_json(self, archivo_json):

        try:
            # abre el archivo json en modo lectura
            with open(archivo_json, 'r', encoding='utf-8') as archivo:
                # carga el contenido del json en un objeto datos
                datos = json.load(archivo)

            # buscar en el json la clave jugadores si no existen se crea una lista vacia
            jugadores_data = datos.get('jugadores', [])
            # iteramos los jugadores en los datos
            for jugador in jugadores_data:
                # instanciamos el objeto jugador a partir de los datos
                jugador = self.crear_jugador(jugador)
                # agregamos los jugadores a la lista
                self.jugadores.append(jugador)

        except FileNotFoundError:
            print(f'El archivo {archivo_json} no se encontro')

    def crear_jugador(self, jugador_data):
        # extrae los atributos del jugador del diccionario 'jugador_data'
        nombre = jugador_data.get('nombre', 'N/A')
        posicion = jugador_data.get('posicion', 'N/A')
        logros = jugador_data.get('logros', 'N/A')
        estadisticas_data = jugador_data.get('estadisticas', 'N/A')

        # crea el objeto estadisticas para el jugador
        estadisticas = self.crear_estadisticas(estadisticas_data)
        # crea un objeto jugador con los atributos extraidos y el objeto de estadisticas
        jugador = Jugador(nombre, posicion, logros, estadisticas)

        return jugador

    def crear_estadisticas(self, estadisticas_data):
        # creamos un objeto estadisticas y asignamos los valores de los atributos
        estadisticas = Estadisticas()

        estadisticas.temporadas = estadisticas_data.get('temporadas', 0)
        estadisticas.puntos_totales = estadisticas_data.get(
            'puntos_totales', 0)
        estadisticas.promedio_puntos_por_partido = estadisticas_data.get(
            'promedio_puntos_por_partido', 0.0)
        estadisticas.rebotes_totales = estadisticas_data.get(
            'rebotes_totales', 0)
        estadisticas.promedio_rebotes_por_partido = estadisticas_data.get(
            'promedio_rebotes_por_partido', 0.0)
        estadisticas.asistencias_totales = estadisticas_data.get(
            'asistencias_totales', 0)
        estadisticas.promedio_asistencias_por_partido = estadisticas_data.get(
            'promedio_asistencias_por_partido', 0.0)
        estadisticas.robos_totales = estadisticas_data.get('robos_totales', 0)
        estadisticas.bloqueos_totales = estadisticas_data.get(
            'bloqueos_totales', 0)
        estadisticas.porcentaje_tiros_de_campo = estadisticas_data.get(
            'porcentaje_tiros_de_campo', 0.0)
        estadisticas.porcentaje_tiros_libres = estadisticas_data.get(
            'porcentaje_tiros_libres', 0.0)
        estadisticas.porcentaje_tiros_triples = estadisticas_data.get(
            'porcentaje_tiros_triples', 0.0)

        return estadisticas


# ruta del archivo json que continee los datos del equipo
ruta_json = r'primer-parcial\dream_team.json'
# crea el objeto equipo y carga los datos del el archivo json
equipo = Equipo(ruta_json)
