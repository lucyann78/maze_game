import pygame
from include.main import ANCHO_PANTALLA, ALTO_PANTALLA, TAMANO_TILE
from include.colors import VERDE_MENTA_TECHO, VERDE_MENTA_SUELO # Para limpiar la pantalla
from src.raycaster import cast_rays_and_get_data # Importa la implementación real del raycasting

# Estas funciones ya no son placeholders; aquí están sus implementaciones reales.
def clear_screen(screen):
    """
    Rellena la pantalla con el color del techo en la mitad superior y el color del suelo en la mitad inferior.
    (Tarea 0: ¡Paredes!)
    """
    screen.fill(VERDE_MENTA_TECHO) # Rellena la parte superior (techo)
    pygame.draw.rect(screen, VERDE_MENTA_SUELO, (0, ALTO_PANTALLA // 2, ANCHO_PANTALLA, ALTO_PANTALLA // 2)) # Rellena la parte inferior (suelo)

def draw_wall_column(screen, x, wall_height, wall_color):
    """
    Dibuja una única columna vertical en la pantalla que representa una porción de pared.
    (Tarea 0: ¡Paredes!)
    """
    # Calcula las coordenadas Y para el inicio y fin de la columna de la pared.
    # El centro de la pantalla es el punto medio del muro.
    y_start = (ALTO_PANTALLA / 2) - (wall_height / 2)
    y_end = (ALTO_PANTALLA / 2) + (wall_height / 2)
    pygame.draw.line(screen, wall_color, (x, y_start), (x, y_end), 1)


def draw_game_frame(screen, player, game_map_obj, clock):
    """
    Esta es la función principal de dibujo por frame. Orquesta todas las llamadas de renderizado.
    (Tareas 0, 1, y marcadores de posición para futuras tareas como minimapa, armas, etc.)
    """
    clear_screen(screen) # Primero, limpia la pantalla y dibuja el suelo/techo.

    # Realiza el raycasting para obtener los datos de las paredes y luego dibújalas.
    wall_render_data = cast_rays_and_get_data(player, game_map_obj)
    for i, data in enumerate(wall_render_data):
        if data: # Asegúrate de que el rayo haya impactado en algo antes de intentar dibujarlo.
            draw_wall_column(screen, i, data['wall_height'], data['color'])

    # --- Marcadores de posición para futuras llamadas de dibujo ---
    # A medida que implementes más tareas, añadirás las llamadas a funciones aquí.

    # Tarea 6: Dibujar Minimapa (cuando esté implementado y activado)
    # from src.minimap import draw_minimap
    # from src.window_status import is_minimap_active
    # if is_minimap_active():
    #     draw_minimap(screen, player, game_map_obj)

    # Tarea 11: Dibujar Arma (cuando esté implementado)
    # from src.weapon import draw_weapon
    # draw_weapon(screen, player.get_current_weapon_state()) # Asumiendo que el jugador tiene un estado de arma

    # Tarea 12: Dibujar Enemigos (cuando estén implementados)
    # from src.enemy import get_all_enemies, draw_enemy_sprite
    # for enemy in get_all_enemies():
    #    draw_enemy_sprite(screen, player, enemy, clock.get_time())

    # Tarea 13: Dibujar Lluvia (cuando esté implementado)
    # from src.weather import draw_rain
    # draw_rain(screen, clock.get_time()) # Pasa el delta time para la animación de la lluvia

    # Finalmente, actualiza la pantalla para mostrar todo lo dibujado.
    from src.draw_to_screen import refresh_screen
    refresh_screen()
