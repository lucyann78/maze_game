import pygame
from src.player import Player
from src.map import GameMap

# Diccionario global para rastrear el estado de las teclas presionadas.
# Las claves deben ser los valores numéricos (o las constantes de Pygame) que event.key devuelve.
_keys_pressed = {
    pygame.K_w: False,
    pygame.K_s: False,
    pygame.K_a: False,
    pygame.K_d: False,
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_m: False,
}

_minimap_enabled = False

def handle_input_events(player_instance):
    """
    Maneja todos los eventos de Pygame y actualiza el estado global de las teclas.
    """
    global _minimap_enabled

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            # Aquí es donde se verifica si el 'valor numérico' de la tecla presionada
            # coincide con una de las claves de nuestro diccionario.
            # print(f"DEBUG: Tecla presionada: {event.key}") # Puedes descomentar para depuración

            if event.key in _keys_pressed:
                _keys_pressed[event.key] = True
            if event.key == pygame.K_m:
                _minimap_enabled = not _minimap_enabled

        elif event.type == pygame.KEYUP:
            # print(f"DEBUG: Tecla soltada: {event.key}") # Puedes descomentar para depuración
            if event.key in _keys_pressed:
                _keys_pressed[event.key] = False
    return False

def update_player_movement(player, delta_time, game_map_obj):
    """
    Actualiza la posición y rotación del jugador basándose en el estado de las teclas.
    """
    # Movimiento Adelante/Atrás
    if _keys_pressed[pygame.K_w] and not _keys_pressed[pygame.K_s]:
        player.move(1, delta_time, game_map_obj)
    elif _keys_pressed[pygame.K_s] and not _keys_pressed[pygame.K_w]:
        player.move(-1, delta_time, game_map_obj)

    # Movimiento Lateral (Strafe)
    if _keys_pressed[pygame.K_a] and not _keys_pressed[pygame.K_d]:
        player.strafe(-1, delta_time, game_map_obj)
    elif _keys_pressed[pygame.K_d] and not _keys_pressed[pygame.K_a]:
        player.strafe(1, delta_time, game_map_obj)

    # Rotación
    if _keys_pressed[pygame.K_LEFT]:
        player.rotate(-1)
    if _keys_pressed[pygame.K_RIGHT]:
        player.rotate(1)

def is_minimap_active():
    """Devuelve el estado actual de la activación/desactivación del minimapa."""
    return _minimap_enabled
