import pygame
from src.player import Player
from src.map import GameMap

# ... (el resto del código incluyendo _keys_pressed) ...

def handle_input_events(player_instance):
    global _minimap_enabled

    for event in pygame.event.get(): # Itera sobre todos los eventos
        print(f"DEBUG: Evento detectado: {event.type}") # <--- AÑADE ESTA LÍNEA
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            print(f"DEBUG: Tecla presionada (código): {event.key}") # <--- AÑADE ESTA LÍNEA
            if event.key in _keys_pressed:
                _keys_pressed[event.key] = True
            if event.key == pygame.K_m:
                _minimap_enabled = not _minimap_enabled
        elif event.type == pygame.KEYUP:
            print(f"DEBUG: Tecla soltada (código): {event.key}") # <--- AÑADE ESTA LÍNEA
            if event.key in _keys_pressed:
                _keys_pressed[event.key] = False
    return False
