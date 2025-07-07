import pygame
import math
import sys
import os

# Añadir la ruta del directorio raíz del proyecto al PATH de Python
# Esto permite importar módulos de 'include' y 'src' directamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# El resto de tus importaciones
from include.main import ANCHO_PANTALLA, ALTO_PANTALLA, FPS, TAMANO_TILE, FOV_JUGADOR_GRADOS
from src.SDL_subfunctions import init_pygame, quit_pygame
from src.window import setup_game_window
from src.map import GameMap
from src.player import Player
from src.draw_all_things import draw_game_frame
from src.window_status import handle_input_events, update_player_movement # Importa funciones de estado

# ... el resto de tu código main_game_loop()
