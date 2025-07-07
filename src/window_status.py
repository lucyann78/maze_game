import pygame
from src.player import Player # Necesitamos el objeto Player para interactuar con él
from src.map import GameMap # Necesitamos el objeto GameMap para las colisiones

# Diccionario global para rastrear el estado de las teclas presionadas.
# Esto es esencial para el manejo de "multitarea" (Tarea 9),
# permitiendo al jugador mover y rotar simultáneamente.
_keys_pressed = {
    pygame.K_w: False,     # Tecla W: Adelante
    pygame.K_s: False,     # Tecla S: Atrás
    pygame.K_a: False,     # Tecla A: Strafe Izquierda
    pygame.K_d: False,     # Tecla D: Strafe Derecha
    pygame.K_LEFT: False,  # Flecha izquierda: Rotar izquierda
    pygame.K_RIGHT: False, # Flecha derecha: Rotar derecha
    pygame.K_m: False,     # Tecla M: Para activar/desactivar el minimapa (Tarea 6)
    # Agrega más teclas aquí a medida que implementes nuevas funcionalidades (disparar, lluvia, etc.)
}

_minimap_enabled = False # Variable global para controlar el estado del minimapa (inicialmente desactivado).

def handle_input_events(player_instance):
    """
    Maneja todos los eventos de Pygame (cerrar ventana, presionar/soltar teclas).
    Actualiza el estado global de las teclas.
    Devuelve True si el evento `pygame.QUIT` (cerrar ventana) ha ocurrido,
    indicando que el bucle principal del juego debe terminar.
    """
    global _minimap_enabled # Declara que vamos a modificar la variable global _minimap_enabled.

    for event in pygame.event.get(): # Itera sobre todos los eventos ocurridos desde el último frame.
        if event.type == pygame.QUIT:
            return True # El usuario ha cerrado la ventana, el juego debe terminar.
        elif event.type == pygame.KEYDOWN: # Si una tecla ha sido presionada...
            if event.key in _keys_pressed: # Verifica si es una de nuestras teclas de movimiento/rotación.
                _keys_pressed[event.key] = True # Marca la tecla como presionada.
            if event.key == pygame.K_m: # Si es la tecla 'M', alterna el estado del minimapa.
                _minimap_enabled = not _minimap_enabled
        elif event.type == pygame.KEYUP: # Si una tecla ha sido soltada...
            if event.key in _keys_pressed: # Verifica si es una de nuestras teclas de movimiento/rotación.
                _keys_pressed[event.key] = False # Marca la tecla como no presionada.
    return False # Si no se ha detectado el evento QUIT, el juego continúa.

def update_player_movement(player, delta_time, game_map_obj):
    """
    Actualiza la posición y rotación del jugador basándose en el estado actual de las teclas.
    Esto permite movimientos y rotaciones simultáneos (Tarea 3: Mover, Tarea 4: ¡Ouch! (Colisión), Tarea 9: ¡Multitarea!).
    """
    # --- Manejo del movimiento combinado (Tarea 9) ---

    # Movimiento Adelante/Atrás: Solo si W está presionada y S no (o viceversa).
    if _keys_pressed[pygame.K_w] and not _keys_pressed[pygame.K_s]:
        player.move(1, delta_time, game_map_obj) # Mueve hacia adelante
    elif _keys_pressed[pygame.K_s] and not _keys_pressed[pygame.K_w]:
        player.move(-1, delta_time, game_map_obj) # Mueve hacia atrás

    # Movimiento Lateral (Strafe) Izquierda/Derecha: Solo si A está presionada y D no (o viceversa).
    if _keys_pressed[pygame.K_a] and not _keys_pressed[pygame.K_d]:
        player.strafe(-1, delta_time, game_map_obj) # Strafe izquierda
    elif _keys_pressed[pygame.K_d] and not _keys_pressed[pygame.K_a]:
        player.strafe(1, delta_time, game_map_obj) # Strafe derecha

    # Rotación: Las flechas izquierda/derecha.
    if _keys_pressed[pygame.K_LEFT]:
        player.rotate(-1) # Rotar a la izquierda
    if _keys_pressed[pygame.K_RIGHT]:
        player.rotate(1) # Rotar a la derecha

def is_minimap_active():
    """
    Devuelve el estado actual de la activación/desactivación del minimapa.
    (Tarea 6: Dibujar el mapa)
    """
    return _minimap_enabled
