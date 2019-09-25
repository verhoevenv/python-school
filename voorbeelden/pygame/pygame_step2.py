import sys, pygame
from pygame.locals import *

pygame.init()

background = 0, 0, 0
ball_color = 255, 255, 255
size = width, height = 640, 480
ball_position = 320, 240

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ball_position = ball_position[0] + 2, ball_position[1] + 2
    screen.fill(background)
    pygame.draw.circle(screen, ball_color, ball_position, 10)
    pygame.display.flip()