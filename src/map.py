# El mapa del juego.
# Los valores representan diferentes tipos de "tiles" o cuadrados en el mapa:
# 0 = espacio vacío (por donde el jugador puede moverse)
# 1 = pared (un obstáculo)
# Más adelante, podrías usar otros números para diferentes tipos de paredes, puertas, etc.

class GameMap:
    def __init__(self):
        # Tarea 0: Mapa codificado directamente en el código.
        # Puedes modificar este array bidimensional para cambiar el diseño del laberinto.
        # Cada sublista es una fila del mapa.
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def get_value(self, x, y):
        """
        Devuelve el valor del mapa en las coordenadas de tile dadas (x, y).
        Se asegura de que las coordenadas estén dentro de los límites del mapa.
        """
        map_x = int(x)
        map_y = int(y)
        # Verifica si las coordenadas están dentro del rango del mapa.
        if 0 <= map_x < len(self.map_data[0]) and 0 <= map_y < len(self.map_data):
            return self.map_data[map_y][map_x]
        return 1 # Si está fuera de los límites, asume que es una pared para evitar errores.
