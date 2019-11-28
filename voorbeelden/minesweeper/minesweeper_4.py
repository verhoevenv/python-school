import sys, pygame
from random import randint
from pygame.locals import *

pygame.init()

background = 0, 0, 0
size = width, height = 400, 400

minefield = [
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
]

def neighbours(x, y):
    candidates = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            candidates.append((x+dx, y+dy))
    candidates.remove((x, y))
    for (el_x, el_y) in list(candidates):
        if el_x < 0 or el_y < 0 or el_x > 7 or el_y > 7:
            candidates.remove((el_x, el_y))
    return candidates

num_mines_placed = 0
while num_mines_placed < 10:
    x, y = randint(0, 7), randint(0, 7)
    if minefield[x][y] != "X":
        minefield[x][y] = "X"
        for n_x, n_y in neighbours(x, y):
            if minefield[n_x][n_y] != "X":
                minefield[n_x][n_y] = str(int(minefield[n_x][n_y]) + 1)
        num_mines_placed = num_mines_placed + 1

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

# nieuwe variabele
game_lost = False

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 50)

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # kleine aanpassing hier:
        # we willen geen interactie meer als het spel gedaan is
        if event.type == pygame.MOUSEBUTTONUP and not game_lost:
            if event.button == 3:
                (cursor_x, cursor_y) = pygame.mouse.get_pos()
                grid_x = cursor_x // 50
                grid_y = cursor_y // 50
                if grid[grid_x][grid_y] == "?":
                    grid[grid_x][grid_y] = "F"
                elif grid[grid_x][grid_y] == "F":
                    grid[grid_x][grid_y] = "?"

    mouse = pygame.mouse.get_pressed()
    # ook hier willen we geen interactie meer als het spel gedaan is
    if mouse[0] and not game_lost:
        (cursor_x, cursor_y) = pygame.mouse.get_pos()
        grid_x = cursor_x // 50
        grid_y = cursor_y // 50
        grid[grid_x][grid_y] = minefield[grid_x][grid_y]
        # belangrijkste nieuwe stukje code voor game over:
        if minefield[grid_x][grid_y] == "X":
            game_lost = True

    
    screen.fill(background)

    for x in range(8):
        for y in range(8):
            cell = font.render(grid[x][y], True, (255, 255, 255))
            screen.blit(cell, (x * 50, y * 50))

    # we willen ook duidelijk maken dat het game over is
    if game_lost:
        text_surf = font.render("BOOM!", True, (255, 0, 0), background)
        screen.blit(text_surf, (110, 175))

    pygame.display.flip()