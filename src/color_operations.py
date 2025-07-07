def apply_shadow(color, distance, max_distance=1000):
    """
    Aplica un efecto de sombra simple a un color RGB basándose en la distancia.
    Cuanto mayor sea la `distance`, más oscuro será el `color`.
    `max_distance` define la distancia a la que el color alcanza su máxima oscuridad (factor 0.2).
    """
    shadow_factor = max(0.2, 1.0 - (distance / max_distance)) # Evita que el color sea completamente negro
    return (int(color[0] * shadow_factor),
            int(color[1] * shadow_factor),
            int(color[2] * shadow_factor))

def adjust_brightness(color, factor):
    """
    Ajusta el brillo de un color RGB por un `factor`.
    `factor` > 1.0 para más brillante, `factor` < 1.0 para más oscuro.
    Los valores de RGB se limitan a 255.
    """
    return (min(255, int(color[0] * factor)),
            min(255, int(color[1] * factor)),
            min(255, int(color[2] * factor)))
