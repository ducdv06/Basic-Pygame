import pygame
import sys

pygame.init()
width, height = 400, 600
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 51, 51)

square_x, square_y = 0, 0
square_w, square_h = 56, 56
distance = 1

bird = pygame.image.load("./assests/yellowbird-midflap.png")
bird = pygame.transform.scale(bird, (square_w, square_h))

running = True
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(WHITE, (0,0,width, height))
    screen.fill(RED, (square_x,square_y,square_w,square_h))
    screen.blit(bird, ((square_x,square_y,square_w,square_h)))

    square_x += distance
    if square_x + square_w >= width:
        square_x = width - square_w
        distance = -distance
        bird = pygame.transform.flip(bird, True, False)
    if square_x <= 0:
        square_x = 0
        distance = -distance
        bird = pygame.transform.flip(bird, True, False)
    pygame.display.update()
    clock.tick(60)