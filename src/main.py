import pygame
import math
from include.main import ANCHO_PANTALLA, ALTO_PANTALLA, FPS, TAMANO_TILE, FOV_JUGADOR_GRADOS
from src.SDL_subfunctions import init_pygame, quit_pygame
from src.window import setup_game_window
from src.map import GameMap
from src.player import Player
from src.draw_all_things import draw_game_frame
from src.window_status import handle_input_events, update_player_movement # Importa funciones de estado

def main_game_loop():
    """
    Función principal que inicializa el juego, configura el bucle principal
    y maneja la lógica de actualización y renderizado de cada frame.
    """
    # 1. Inicialización de Pygame
    init_pygame()
    screen, clock = setup_game_window(ANCHO_PANTALLA, ALTO_PANTALLA, FPS)

    # 2. Inicializar elementos del juego
    game_map = GameMap() # Crea una instancia de tu mapa (inicialmente hardcodeado, Tarea 0)
    # Crea una instancia del jugador. Inícialo en un espacio vacío en el mapa (ej. 1.5, 1.5 en el tile grid)
    # y con un ángulo de visión inicial.
    player = Player(x=TAMANO_TILE * 1.5, y=TAMANO_TILE * 1.5, angle=math.radians(FOV_JUGADOR_GRADOS / 2))

    running = True # Bandera para controlar si el bucle del juego está activo

    # 3. Bucle Principal del Juego
    while running:
        # Calcula el tiempo transcurrido desde el último frame.
        # Esto es crucial para que el movimiento sea consistente en diferentes FPS.
        delta_time = clock.tick(FPS) / 1000.0 # Tiempo en segundos

        # Maneja los eventos de entrada del usuario (teclado, ratón, cerrar ventana).
        # `handle_input_events` también actualiza el estado global de las teclas.
        # Si devuelve True (indicando que el usuario quiere salir), se detiene el bucle.
        if handle_input_events(player): # Le pasamos el objeto player para que pueda interactuar con él directamente
            running = False

        # Actualiza el estado del jugador (movimiento, rotación) basándose en las teclas presionadas.
        # `update_player_movement` también maneja colisiones (Tarea 3, 4, 9).
        update_player_movement(player, delta_time, game_map) # Pasa el objeto GameMap para verificación de colisiones

        # Dibuja todos los elementos del juego para el frame actual.
        # Esta función es el punto de orquestación del renderizado.
        draw_game_frame(screen, player, game_map, clock) # Pasa el objeto GameMap y el reloj para consistencia

    # 4. Finalización de Pygame (cuando el bucle termina)
    quit_pygame()

# Punto de entrada del script. Asegura que `main_game_loop()` se ejecute solo cuando el script se inicie directamente.
if __name__ == "__main__":
    main_game_loop()
