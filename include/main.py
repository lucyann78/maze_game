import math # Necesario para cálculos con PI y grados/radianes

# --- Dimensiones de la Pantalla ---
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# --- Configuración del Mapa ---
TAMANO_TILE = 64 # Tamaño en píxeles de un solo "cuadrado" o "tile" en el mapa del juego.
                 # Es importante que el mapa esté en múltiplos de este tamaño.

# --- Configuración del Jugador ---
VELOCIDAD_JUGADOR = 0.05 # Velocidad de movimiento del jugador por frame (en unidades del mundo).
VELOCIDAD_ROTACION_JUGADOR = 0.03 # Velocidad de rotación del jugador por frame (en radianes).
FOV_JUGADOR_GRADOS = 60 # Campo de Visión del jugador en grados.
RADIO_JUGADOR = 10 # Radio del jugador, útil para la detección de colisiones (Tarea 4).

# --- Configuración de Raycasting ---
NUM_RAYOS = ANCHO_PANTALLA # Generalmente, lanzamos un rayo por cada columna de píxeles de la pantalla para renderizar.
HALF_FOV_RAD = (FOV_JUGADOR_GRADOS / 2) * (math.pi / 180) # La mitad del FOV, convertido a radianes.
PASO_ANGULO_RAD = (FOV_JUGADOR_GRADOS / NUM_RAYOS) * (math.pi / 180) # La diferencia de ángulo entre cada rayo, en radianes.

# --- Cuadros Por Segundo (FPS) ---
FPS = 60 # Velocidad objetivo de los frames por segundo para un juego fluido.

# --- Rutas de Recursos ---
# Es crucial que estas rutas sean correctas en relación al directorio desde donde se ejecuta `src/main.py`.
DIR_IMAGENES = "resources/images/" # Directorio base para todas tus imágenes.
RUTA_ARMA_FLOR = DIR_IMAGENES + "flower_gun.png" # Ruta para la imagen de tu arma de flores (Tarea 11).
RUTA_TEXTURA_PARED = DIR_IMAGENES + "wall_texture.png" # Ruta para una textura de pared (Tarea 8).
RUTA_IMAGEN_PRUEBA = DIR_IMAGENES + "hello_world.bmp" # Una imagen de prueba simple.
