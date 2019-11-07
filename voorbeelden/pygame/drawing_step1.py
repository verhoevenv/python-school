import sys, pygame
from pygame.locals import *

pygame.init()

background = 0, 0, 0
foreground = 255, 255, 255
size = width, height = 640, 480

screen = pygame.display.set_mode(size)
screen.fill(background)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    (left_button, middle_button, right_button) = pygame.mouse.get_pressed()
    if left_button:
        pygame.draw.circle(screen, foreground, pygame.mouse.get_pos(), 10)
    if right_button:
        screen.fill(background)

    pygame.display.flip()