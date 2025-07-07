import math
from include.main import VELOCIDAD_JUGADOR, VELOCIDAD_ROTACION_JUGADOR, TAMANO_TILE, RADIO_JUGADOR
from src.map import GameMap # Importa la clase GameMap para usar sus datos
from include.applied_math import normalize_angle # Para mantener los ángulos en un rango manejable

class Player:
    def __init__(self, x, y, angle):
        self.x = x  # Posición X del jugador en unidades del mundo.
        self.y = y  # Posición Y del jugador en unidades del mundo.
        self.angle = angle # Ángulo de visión actual del jugador en radianes.

    def rotate(self, direction):
        """
        Rota el ángulo de visión del jugador.
        `direction`: 1 para rotar a la derecha (sentido horario), -1 para rotar a la izquierda (sentido antihorario).
        (Tarea 2: Rotación)
        """
        self.angle += direction * VELOCIDAD_ROTACION_JUGADOR
        self.angle = normalize_angle(self.angle) # Normaliza el ángulo para que siempre esté entre 0 y 2*PI.

    def _is_colliding(self, proposed_x, proposed_y, game_map_obj):
        """
        Función auxiliar privada para verificar si una posición propuesta colisionaría con una pared.
        (Tarea 4: ¡Ouch! - Colisiones)
        """
        # Obtenemos las coordenadas de la celda del mapa donde estaría el centro del jugador.
        tile_x = int(proposed_x / TAMANO_TILE)
        tile_y = int(proposed_y / TAMANO_TILE)

        # Verificamos si la celda del mapa a la que nos movemos es una pared.
        # Esta es una verificación simplificada: solo mira la celda central.
        # Para colisiones más precisas (y deslizamiento), idealmente verificaríamos
        # las 4 esquinas del jugador o un círculo alrededor de él.
        if game_map_obj.get_value(tile_x, tile_y) != 0:
            return True
        return False

    def move(self, direction_scalar, delta_time, game_map_obj):
        """
        Mueve al jugador hacia adelante o hacia atrás con detección de colisiones.
        `direction_scalar`: 1 para moverse hacia adelante, -1 para moverse hacia atrás.
        `delta_time`: Tiempo transcurrido desde el último frame, para un movimiento suave.
        (Tarea 3: Mover, Tarea 4: ¡Ouch! (Colisiones), Tarea 9: ¡Multitarea!)
        """
        move_amount = direction_scalar * VELOCIDAD_JUGADOR * delta_time

        # Calcula las nuevas posiciones propuestas (sin considerar colisiones aún)
        new_x = self.x + math.cos(self.angle) * move_amount
        new_y = self.y + math.sin(self.angle) * move_amount

        # Detección de colisiones: primero intenta mover en X, luego en Y.
        # Esto permite un "deslizamiento" básico sobre las paredes (Tarea 4).
        if not self._is_colliding(new_x, self.y, game_map_obj):
            self.x = new_x
        # Después de intentar mover en X, intenta mover en Y.
        if not self._is_colliding(self.x, new_y, game_map_obj):
            self.y = new_y

    def strafe(self, direction_scalar, delta_time, game_map_obj):
        """
        Mueve al jugador lateralmente (strafing) con detección de colisiones.
        `direction_scalar`: 1 para deslizarse a la derecha, -1 para deslizarse a la izquierda.
        `delta_time`: Tiempo transcurrido desde el último frame.
        (Tarea 9: ¡Multitarea!)
        """
        move_amount = direction_scalar * VELOCIDAD_JUGADOR * delta_time

        # Para deslizarse, el movimiento es perpendicular al ángulo de visión.
        # Sumamos/restamos pi/2 (90 grados) al ángulo actual.
        strafe_angle = self.angle + (math.pi / 2) # Para strafe derecho
        if direction_scalar < 0: # Para strafe izquierdo
            strafe_angle = self.angle - (math.pi / 2)

        # Calcula las nuevas posiciones propuestas
        new_x = self.x + math.cos(strafe_angle) * move_amount
        new_y = self.y + math.sin(strafe_angle) * move_amount

        # Detección de colisiones para strafing (similar al movimiento adelante/atrás)
        if not self._is_colliding(new_x, self.y, game_map_obj):
            self.x = new_x
        if not self._is_colliding(self.x, new_y, game_map_obj):
            self.y = new_y

    def get_current_weapon_state(self):
        """
        (Marcador de posición para la Tarea 11: Armas)
        En futuras tareas, esta función devolvería información sobre el arma
        actual del jugador (ej. tipo de arma, estado de animación) para ser dibujada.
        """
        return {} # Devuelve un diccionario vacío por ahora.
