import sys, pygame
from pygame.locals import *

pygame.init()

background = 0, 0, 0
ball_color = 255, 255, 255
size = width, height = 640, 480

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(background)
    pygame.draw.circle(screen, ball_color, (320, 240), 10)
    pygame.display.flip()