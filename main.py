import pygame, sys

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HIGH = 800
GREEN = (20, 160, 133)
BACKGROUND_COLOR = GREEN

ball_raduis = 10
ball_x = 400
ball_y = 400
ball_speed_x = 0
ball_speed_y = 0
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))
pygame.display.set_caption("MY first pygame game")
clock = pygame.time.Clock()
#game loop
while True : 
    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ball_speed_x = 3
            elif event.key == pygame.K_LEFT:
                ball_speed_x = -3
            elif event.key == pygame.K_UP:
                ball_speed_y = -3
            elif event.key == pygame.K_DOWN:
                ball_speed_y = 3

    #Update position
    if ball_x  >= SCREEN_HIGH + ball_raduis :
        ball_x = 0
    if ball_x  < 0:
        ball_x = SCREEN_HIGH
    if ball_y < 0:
        ball_y = SCREEN_WIDTH
    if ball_y > SCREEN_WIDTH:
        ball_y = 0
    else:
        ball_x += ball_speed_x
        ball_y += ball_speed_y




    #Draw the change
    window.fill(BACKGROUND_COLOR)
    pygame.draw.circle(window, pygame.Color('white'), (ball_x, ball_y), ball_raduis)


    pygame.display.update()
    clock.tick(60)