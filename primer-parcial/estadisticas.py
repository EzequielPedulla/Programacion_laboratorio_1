# definimos la clase estadistica para poder almarcenarlas
class Estadisticas:
    def __init__(self) -> None:
        self.temporadas = 0
        self.puntos_totales = 0
        self.promedio_puntos_por_partido = 0
        self.rebotes_totales = 0
        self.promedio_rebotes_por_partido = 0
        self.asistencias_totales = 0
        self.promedio_asistencias_por_partido = 0
        self.robos_totales = 0
        self.bloqueos_totales = 0
        self.porcentaje_tiros_de_campo = 0
        self.porcentaje_tiros_libres = 0
        self.porcentaje_tiros_triples = 0
