from random import random
import pygame, sys
from pygame.locals import *

pygame.init()

size = width, height = 1000, 1000
black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("Arial", 30)

simulation = pygame.Surface(size)

attempts = 0
hits = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    attempts = attempts + 1
    x = random()
    y = random()
    color = red
    if x*x + y*y < 1:
        hits = hits + 1
        color = green
    
    pygame.draw.circle(simulation, color, (int(x * height), int(y*width)), 1)

    screen.fill(black)
    screen.blit(simulation, (0, 0))

    ren = font.render(f"{hits} / {attempts} => pi ~ {4 * hits / attempts}", 0, white, black)
    screen.blit(ren, (10, 10))

    pygame.display.flip()
