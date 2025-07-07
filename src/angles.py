import math
from include.applied_math import normalize_angle

def calculate_angle_difference(angle1, angle2):
    """
    Calcula la diferencia angular más corta entre dos ángulos (en radianes).
    Útil para corregir el efecto "ojo de pez" en el raycasting o para la IA de enemigos.
    """
    diff = normalize_angle(angle1 - angle2)
    if diff > math.pi:
        diff -= 2 * math.pi
    return diff
