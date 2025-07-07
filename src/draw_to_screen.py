import pygame

def refresh_screen():
    """
    Actualiza la visualización completa de Pygame.
    Esto toma todo lo que se ha dibujado en el "back buffer" y lo muestra en pantalla.
    """
    pygame.display.flip()
