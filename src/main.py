import pygame
import math
import sys
import os
import time # Importa el módulo 'time'

# Añade la ruta del directorio raíz del proyecto al PATH de Python.
# Esto es crucial para que Python pueda encontrar los módulos en las carpetas 'include' y 'src'.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa las constantes y funciones necesarias de tus propios módulos.
from include.main import ANCHO_PANTALLA, ALTO_PANTALLA, FPS, TAMANO_TILE, FOV_JUGADOR_GRADOS
from src.SDL_subfunctions import init_pygame, quit_pygame
from src.window import setup_game_window
from src.map import GameMap
from src.player import Player
from src.draw_all_things import draw_game_frame
# Importa las funciones de manejo de entrada y la variable global _keys_pressed.
from src.window_status import handle_input_events, update_player_movement, _keys_pressed

def main_game_loop():
    """
    Función principal del juego. Inicializa Pygame, configura la ventana
    y ejecuta el bucle principal del juego.
    """
    # Inicializa todos los módulos de Pygame.
    init_pygame()
    # Configura la ventana del juego y obtiene el objeto de pantalla y el reloj para controlar el FPS.
    screen, clock = setup_game_window(ANCHO_PANTALLA, ALTO_PANTALLA, FPS)

    # Inicializa el mapa del juego.
    game_map = GameMap()
    # Crea una instancia del jugador en una posición inicial y con un ángulo de visión.
    player = Player(x=TAMANO_TILE * 1.5, y=TAMANO_TILE * 1.5, angle=math.radians(FOV_JUGADOR_GRADOS / 2))

    # Variable que controla si el bucle del juego debe seguir ejecutándose.
    running = True

    # --- Bucle Principal del Juego ---
    while running:
        # Calcula el tiempo transcurrido desde el último frame. Es crucial para un movimiento suave.
        delta_time = clock.tick(FPS) / 1000.0

        # Maneja todos los eventos de entrada (teclado, cerrar ventana).
        # Si la función indica que se debe salir del juego, la bandera 'running' se pone en False.
        if handle_input_events(player):
            running = False

        # --- LÍNEA DE DEPURACIÓN PARA EL ESTADO DE LAS TECLAS ---
        # Se ejecuta en cada frame para mostrar el estado actual de las teclas presionadas.
        print(f"Estado de teclas: {_keys_pressed}")
        # --------------------------------------------------------

        # Actualiza la posición y rotación del jugador basándose en la entrada y las colisiones.
        update_player_movement(player, delta_time, game_map)

        # Dibuja todos los elementos del juego en la pantalla.
        draw_game_frame(screen, player, game_map, clock)

        # La línea `time.sleep(1)` está comentada. Si la descomentas, el juego irá muy lento,
        # lo cual es útil para depuración visual, pero debe estar comentada para juego normal.
        # time.sleep(1)

    # Una vez que el bucle termina, desinicializa Pygame y cierra la ventana.
    quit_pygame()

# Este bloque asegura que main_game_loop() solo se ejecute cuando el script se inicia directamente.
if __name__ == "__main__":
    main_game_loop()
