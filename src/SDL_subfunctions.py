import pygame

def init_pygame():
    """
    Inicializa todos los módulos de Pygame. Debe llamarse al inicio del juego.
    """
    pygame.init()

def quit_pygame():
    """
    Desinicializa todos los módulos de Pygame. Debe llamarse al final del juego para liberar recursos.
    """
    pygame.quit()
