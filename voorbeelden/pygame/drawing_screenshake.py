import sys, pygame
from random import randint
from pygame.locals import *
from time import sleep

pygame.init()

background = 0, 0, 0
foreground = 255, 255, 255
size = width, height = 640, 480

screen = pygame.display.set_mode(size)
buffer = pygame.Surface(size)
buffer.fill(background)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    (left_button, middle_button, right_button) = pygame.mouse.get_pressed()
    if left_button:
        pygame.draw.circle(buffer, foreground, pygame.mouse.get_pos(), 10)
    if right_button:
        for i in range(1000):
            offset = randint(-10, 10), randint(-10, 10)
            screen.fill(background)
            screen.blit(buffer, offset)
            pygame.display.flip()
        buffer.fill(background)

    screen.fill(background)
    screen.blit(buffer, (0,0))
    pygame.display.flip()