import pygame

#initialize all imported pygame modules
pygame.init()

WINDOW_WIDTH = 720
PIXEL_WIDTH = WINDOW_WIDTH // 3

#Initialize a window or screen for display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))

#create an object to help track time
clock = pygame.time.Clock()


running = True


#Definimos una función para cargar un ícono y ajustarlo a una determinada resolución
def load_icon(path, resolution):
    icon = pygame.image.load(path)
    #resize to new resolution
    return pygame.transform.scale(icon, resolution)

#Ejecutamos la función load_icon
GRID = load_icon('grid.png', [WINDOW_WIDTH, WINDOW_WIDTH])




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    pygame.display.flip()
    screen.fill("white")
    #screen.blit(GRID, (0, 0))

pygame.quit()
