def mix_colors(color1, color2, ratio):
    """
    Mezcla dos colores RGB (tuplas de 3 enteros) basándose en una proporción.
    `ratio` debe ser un valor entre 0.0 y 1.0.
    Un ratio de 0.0 significa 100% color1, 1.0 significa 100% color2.
    """
    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
    return (r, g, b)
