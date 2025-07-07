import pygame
import math
from include.main import (
    ANCHO_PANTALLA, ALTO_PANTALLA, TAMANO_TILE, NUM_RAYOS,
    HALF_FOV_RAD, PASO_ANGULO_RAD
)
from include.colors import (
    COLOR_PARED_NORTE, COLOR_PARED_SUR, COLOR_PARED_ESTE, COLOR_PARED_OESTE
)
from include.applied_math import normalize_angle # Para asegurar ángulos correctos
# from src.map import GameMap # No es necesario importar la clase aquí, se pasa como argumento

def cast_rays_and_get_data(player, game_map_obj):
    """
    Esta es la función central del raycasting. Lanza un rayo por cada columna de píxeles
    de la pantalla, calcula dónde impacta en una pared, y determina qué dibujar.
    (Tareas 0: ¡Paredes!, Tarea 1: Orientación)

    Args:
        player (Player): Objeto Player con posición y ángulo actuales.
        game_map_obj (GameMap): Objeto GameMap que contiene los datos del mapa.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario contiene los datos
              necesarios para renderizar una columna de pared (altura, color, etc.).
    """
    render_data = [] # Aquí almacenaremos la información para cada columna de la pantalla.
    start_angle = player.angle - HALF_FOV_RAD # Ángulo del primer rayo (el de la izquierda del FOV).

    for ray_num in range(NUM_RAYOS): # Iteramos por cada "rayo" o columna de píxeles en la pantalla.
        ray_angle = start_angle + (ray_num * PASO_ANGULO_RAD) # Calcula el ángulo del rayo actual.
        ray_angle = normalize_angle(ray_angle) # Normaliza el ángulo para que siempre esté en el rango [0, 2*PI).

        # --- DDA (Digital Differential Analyzer) Algorithm ---
        # Este algoritmo encuentra rápidamente qué celdas del mapa intercepta un rayo.

        # Coordenadas de la celda del mapa donde el jugador se encuentra.
        map_x = int(player.x / TAMANO_TILE)
        map_y = int(player.y / TAMANO_TILE)

        # Vector de dirección del rayo.
        ray_dir_x = math.cos(ray_angle)
        ray_dir_y = math.sin(ray_angle)

        # Longitud del rayo desde la posición actual hasta el siguiente lado X o Y del grid del mapa.
        side_dist_x = 0
        side_dist_y = 0

        # Longitud del rayo para recorrer una unidad completa en X o Y en el grid del mapa.
        # Se calcula con la inversa del componente de dirección para evitar división por cero.
        delta_dist_x = abs(1 / ray_dir_x) if ray_dir_x != 0 else float('inf')
        delta_dist_y = abs(1 / ray_dir_y) if ray_dir_y != 0 else float('inf')

        step_x = 0 # Dirección para moverse en el eje X (+1 o -1).
        step_y = 0 # Dirección para moverse en el eje Y (+1 o -1).

        hit = False # Bandera que indica si el rayo ha impactado una pared.
        side = 0    # Indica qué tipo de pared se golpeó: 0 = Este/Oeste, 1 = Norte/Sur.

        # Calcula 'step' y las 'side_dist' iniciales.
        # Esto determina si el rayo va hacia un X menor o mayor, y dónde está la primera línea del grid.
        if ray_dir_x < 0:
            step_x = -1
            side_dist_x = (player.x / TAMANO_TILE - map_x) * delta_dist_x
        else:
            step_x = 1
            side_dist_x = (map_x + 1.0 - player.x / TAMANO_TILE) * delta_dist_x

        if ray_dir_y < 0:
            step_y = -1
            side_dist_y = (player.y / TAMANO_TILE - map_y) * delta_dist_y
        else:
            step_y = 1
            side_dist_y = (map_y + 1.0 - player.y / TAMANO_TILE) * delta_dist_y

        # Realiza el DDA: avanza el rayo hasta que golpee una pared.
        while not hit:
            # Decide si avanza en el eje X o Y basándose en qué 'side_dist' es menor.
            if side_dist_x < side_dist_y:
                side_dist_x += delta_dist_x
                map_x += step_x
                side = 0 # Se golpeó una pared Este/Oeste
            else:
                side_dist_y += delta_dist_y
                map_y += step_y
                side = 1 # Se golpeó una pared Norte/Sur

            # Verifica si la celda actual del mapa es una pared.
            if game_map_obj.get_value(map_x, map_y) != 0:
                hit = True

        # Calcula la distancia real a la pared y corrige el efecto "ojo de pez".
        # El efecto ojo de pez ocurre si la distancia no se proyecta correctamente en el plano de la cámara.
        perp_wall_dist = 0
        if side == 0: # Si se golpeó una pared Este/Oeste
            perp_wall_dist = (map_x - player.x / TAMANO_TILE + (1 - step_x) / 2) / ray_dir_x
        else: # Si se golpeó una pared Norte/Sur
            perp_wall_dist = (map_y - player.y / TAMANO_TILE + (1 - step_y) / 2) / ray_dir_y

        # Corrección del efecto ojo de pez (Tarea 0).
        corrected_distance = perp_wall_dist * math.cos(ray_angle - player.angle)
        # Evita la división por cero si la distancia es muy pequeña.
        if corrected_distance < 0.001:
            corrected_distance = 0.001

        # Calcula la altura que la pared debe tener en la pantalla.
        wall_height = (TAMANO_TILE * ALTO_PANTALLA) / corrected_distance

        # Determina el color de la pared según su orientación (Tarea 1).
        wall_color = (0, 0, 0) # Color por defecto (negro)
        if side == 0: # Pared Este-Oeste
            if ray_dir_x > 0: # El rayo fue hacia el Este (golpeó el lado Oeste de la pared)
                wall_color = COLOR_PARED_ESTE
            else: # El rayo fue hacia el Oeste (golpeó el lado Este de la pared)
                wall_color = COLOR_PARED_OESTE
        else: # Pared Norte-Sur
            if ray_dir_y > 0: # El rayo fue hacia el Sur (golpeó el lado Norte de la pared)
                wall_color = COLOR_PARED_SUR
            else: # El rayo fue hacia el Norte (golpeó el lado Sur de la pared)
                wall_color = COLOR_PARED_NORTE

        # Almacena los datos de renderizado para esta columna.
        render_data.append({
            'wall_height': wall_height,
            'color': wall_color,
            'distance': corrected_distance,
            'map_x': map_x,
            'map_y': map_y,
            'side': side # Guarda el lado golpeado, útil para texturas más adelante (Tarea 8).
        })
    return render_data
