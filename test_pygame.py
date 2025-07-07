import pygame

pygame.init()

screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Test Pygame Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Si presionas una tecla, también cierra
        if event.type == pygame.KEYDOWN:
            running = False

    screen.fill((255, 0, 0)) # Rellena la pantalla de rojo
    pygame.display.flip()

pygame.quit()
print("Ventana de Pygame cerrada.")
