import pygame
from src.player import Player # Needs Player class for type hinting
from src.map import GameMap # Needs GameMap for type hinting

# Diccionario global para rastrear el estado de las teclas presionadas.
# Sus claves son las constantes de Pygame para las teclas.
_keys_pressed = {
    pygame.K_w: False,
    pygame.K_s: False,
    pygame.K_a: False,
    pygame.K_d: False,
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_m: False,
}

# Variable global para el estado del minimapa
_minimap_enabled = False

def handle_input_events(player_instance):
    """
    Maneja todos los eventos de Pygame (QUIT, KEYDOWN, KEYUP) y
    actualiza el estado global del diccionario _keys_pressed.
    """
    global _minimap_enabled

    for event in pygame.event.get():
        # Debugging: Print all detected events (you can comment this out later)
        print(f"DEBUG: Evento detectado: {event.type}")

        if event.type == pygame.QUIT:
            return True # Signal to quit the game
        elif event.type == pygame.KEYDOWN:
            # Debugging: Print the key code when a key is pressed
            print(f"DEBUG: Tecla presionada (código): {event.key}")

            if event.key in _keys_pressed:
                _keys_pressed[event.key] = True
            if event.key == pygame.K_m:
                _minimap_enabled = not _minimap_enabled
        elif event.type == pygame.KEYUP:
            # Debugging: Print the key code when a key is released
            print(f"DEBUG: Tecla soltada (código): {event.key}")

            if event.key in _keys_pressed:
                _keys_pressed[event.key] = False
    return False # Game should continue

def is_minimap_active():
    """Returns the current state of the minimap toggle."""
    return _minimap_enabled

# NOTE: The update_player_movement function was removed from here in a previous step,
# and its logic was integrated directly into src/main.py.
