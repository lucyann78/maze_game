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
# MODIFICADO: Solo importamos handle_input_events y _keys_pressed de window_status
from src.window_status import handle_input_events, _keys_pressed

def main_game_loop():
    init_pygame()
    screen, clock = setup_game_window(ANCHO_PANTALLA, ALTO_PANTALLA, FPS)

    game_map = GameMap()
    player = Player(x=TAMANO_TILE * 1.5, y=TAMANO_TILE * 1.5, angle=math.radians(FOV_JUGADOR_GRADOS / 2))

    running = True
    while running:
        delta_time = clock.tick(FPS) / 1000.0

        if handle_input_events(player): # Esta función actualiza _keys_pressed
            running = False

        # --- LÍNEAS DE DEPURACIÓN DE ESTADO DE TECLAS ---
        print(f"Estado de teclas: {_keys_pressed}")
        # ------------------------------------------------

        # --- NUEVA LÓGICA DE MOVIMIENTO DEL JUGADOR (MÁS DIRECTA) ---
        # Reemplaza la llamada a update_player_movement
        # Movimiento Adelante/Atrás
        if _keys_pressed[pygame.K_w] and not _keys_pressed[pygame.K_s]:
            player.move(1, delta_time, game_map)
        elif _keys_pressed[pygame.K_s] and not _keys_pressed[pygame.K_w]:
            player.move(-1, delta_time, game_map)

        # Movimiento Lateral (Strafe)
        if _keys_pressed[pygame.K_a] and not _keys_pressed[pygame.K_d]:
            player.strafe(-1, delta_time, game_map)
        elif _keys_pressed[pygame.K_d] and not _keys_pressed[pygame.K_a]:
            player.strafe(1, delta_time, game_map)

        # Rotación
        if _keys_pressed[pygame.K_LEFT]:
            player.rotate(-1)
        if _keys_pressed[pygame.K_RIGHT]:
            player.rotate(1)
        # -------------------------------------------------------------

        draw_game_frame(screen, player, game_map, clock)

        # time.sleep(1) # Pausa temporal para depuración. Comentar/eliminar después de verificar.

    quit_pygame()

if __name__ == "__main__":
    main_game_loop()
