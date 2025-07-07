import pygame
# Importamos la función de inicialización de pantalla desde include/renderer para mantener la consistencia.
from include.renderer import init_screen as renderer_init_screen

def setup_game_window(width, height, fps):
    """
    Configura e inicializa la ventana de Pygame y el objeto Clock para controlar el FPS.
    """
    # Llama a la función real de Pygame para establecer el modo de pantalla.
    screen = pygame.display.set_mode((width, height))
    # Crea un objeto Clock para controlar la velocidad de fotogramas del juego.
    clock = pygame.time.Clock()
    # Establece el título de la ventana del juego.
    pygame.display.set_caption("Raycaster ConectaFlores")
    return screen, clock
