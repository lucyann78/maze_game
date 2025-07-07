import math

def normalize_angle(angle):
    """
    Normaliza un ángulo para que siempre esté dentro del rango [0, 2*PI).
    Esto es crucial para evitar problemas con ángulos que crecen indefinidamente.
    """
    return angle % (2 * math.pi)

def distance_between_points(x1, y1, x2, y2):
    """
    Calcula la distancia Euclidiana entre dos puntos (x1, y1) y (x2, y2).
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
