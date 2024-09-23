import pygame, sys

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HIGH = 800
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))
pygame.display.set_caption("MY first pygame game")
clock = pygame.time.Clock()
#game loop
while True : 
    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()

    #Update position

    #Draw the change
    pygame.draw.circle(window, pygame.Color('white'), (400, 400), 20)


    pygame.display.update()
    clock.tick(60)