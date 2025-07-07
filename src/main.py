import pygame
import math
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from include.main import ANCHO_PANTALLA, ALTO_PANTALLA, FPS, TAMANO_TILE, FOV_JUGADOR_GRADOS
from src.SDL_subfunctions import init_pygame, quit_pygame
from src.window import setup_game_window
from src.map import GameMap
from src.player import Player
from src.draw_all_things import draw_game_frame
from src.window_status import handle_input_events, update_player_movement

def main_game_loop():
    init_pygame()
    screen, clock = setup_game_window(ANCHO_PANTALLA, ALTO_PANTALLA, FPS)

    game_map = GameMap()
    player = Player(x=TAMANO_TILE * 1.5, y=TAMANO_TILE * 1.5, angle=math.radians(FOV_JUGADOR_GRADOS / 2))

    running = True
    while running:
        delta_time = clock.tick(FPS) / 1000.0

        if handle_input_events(player):
            running = False

        update_player_movement(player, delta_time, game_map)

        draw_game_frame(screen, player, game_map, clock)

        #time.sleep(1) # Pausa temporal para depuración. Comentar/eliminar después de verificar.

    quit_pygame()

if __name__ == "__main__":
    main_game_loop()
