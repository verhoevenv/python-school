import sys, pygame
from pygame.locals import *

pygame.init()

background = 0, 0, 0
size = width, height = 400, 400

minefield = [
    ["1", "0", "0", "0", "0", "0", "0", "0"],
    ["1", "X", "0", "0", "0", "0", "0", "0"],
    ["1", "1", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "2", "X", "0", "0", "0", "0", "0"],
    ["0", "X", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
]

grid = [
    ["?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?"],
]

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 50)

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        (cursor_x, cursor_y) = pygame.mouse.get_pos()
        grid_x = cursor_x // 50
        grid_y = cursor_y // 50
        grid[grid_x][grid_y] = minefield[grid_x][grid_y]
    
    screen.fill(background)

    for x in range(8):
        for y in range(8):
            cell = font.render(grid[x][y], True, (255, 255, 255))
            screen.blit(cell, (x * 50, y * 50))
    pygame.display.flip()