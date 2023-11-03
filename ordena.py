

def filtrar_y_mostrar_jugadores(self, cantidad):
    """
    Crea un filtro que permite ingresar una cantidad de jugadores y muestra esos jugadores ordenados por la suma de los dos campos.
    """

    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [
                x
                for x in arr[1:]
                if (x.estadisticas.robos_totales + x.estadisticas.bloqueos_totales)
                <= (
                    pivot.estadisticas.robos_totales
                    + pivot.estadisticas.bloqueos_totales
                )
            ]
            greater = [
                x
                for x in arr[1:]
                if (x.estadisticas.robos_totales + x.estadisticas.bloqueos_totales)
                > (
                    pivot.estadisticas.robos_totales
                    + pivot.estadisticas.bloqueos_totales
                )
            ]
            return quicksort(greater) + [pivot] + quicksort(less)

    try:
        cantidad = int(cantidad)
        jugadores_ordenados = quicksort(self.jugadores)
        for i in range(min(cantidad, len(jugadores_ordenados))):
            jugador = jugadores_ordenados[i]
            print(
                f"{jugador.nombre}: {jugador.estadisticas.robos_totales + jugador.estadisticas.bloqueos_totales}"
            )
    except ValueError:
        print("Cantidad inválida. Debe ser un número entero.")
