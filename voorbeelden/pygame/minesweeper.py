import sys, pygame
from random import randint
from pygame.locals import *

pygame.init()

def create_grid():
    result = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    num_mines_placed = 0
    while num_mines_placed < 10:
        x, y = randint(0, 7), randint(0, 7)
        if result[x][y] != 'X':
            result[x][y] = 'X'
            for n_x, n_y in neighbours(x, y):
                if result[n_x][n_y] != 'X':
                    result[n_x][n_y] = result[n_x][n_y] + 1
            num_mines_placed = num_mines_placed + 1
    return result

def neighbours(x, y):
    candidates = [(x+dx, y+dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
    candidates.remove((x, y))
    for (el_x, el_y) in list(candidates):
        if el_x < 0 or el_y < 0 or el_x > 7 or el_y > 7:
            candidates.remove((el_x, el_y))
    return candidates

red = 255, 0, 0
green = 0, 255, 0
background = 0, 0, 0
cell_colors = {
    '?': (127, 127, 127),
    '0': (0, 255, 0),
    '1': (127, 127, 255),
    '2': (0, 255, 255),
    '3': (255, 0, 0),
    '4': (0, 127, 0),
    '5': (127, 0, 255),
    '6': (0, 127, 127),
    '7': (127, 0, 0),
    '8': (255, 255, 255),
    'X': (255, 0, 0),
    'F': (255, 255, 0),
}

size = width, height = 400, 400
grid = create_grid()

state = [
    ['?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?'],
    ['?', '?', '?', '?', '?', '?', '?', '?'],
]

game_lost = False
game_won = False

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 50)
font_game_over = pygame.font.SysFont("Arial", 100)

def check_game_won():
    global game_won
    won = True
    for row in state:
        for cell in row:
            if cell == '?':
                won = False
    game_won = won

def open_cell(x, y):
    global game_lost
    if state[x][y] == 'open':
        return
    state[x][y] = 'open'
    if grid[x][y] == 'X':
        game_lost = True
    if grid[x][y] == 0:
        for (n_x, n_y) in neighbours(x, y):
            open_cell(n_x, n_y)

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP and not (game_lost or game_won):
            x = event.pos[0] // 50
            y = event.pos[1] // 50
            if event.button == 1 and state[x][y] != 'F':
                open_cell(x, y)
            elif event.button == 3:
                if state[x][y] == 'F':
                    state[x][y] = '?'
                elif state[x][y] == '?':
                    state[x][y] = 'F'
            check_game_won()
    
    screen.fill(background)
    for x in range(8):
        for y in range(8):
            if state[x][y] == 'open':
                text = str(grid[x][y])
            else:
                text = state[x][y]
            text_surf = font.render(text, True, cell_colors[text], background)
            screen.blit(text_surf, (x * 50, y * 50))

    if game_lost:
        text_surf = font_game_over.render("BOOM!", True, red, background)
        screen.blit(text_surf, (25, 150))

    if game_won:
        text_surf = font_game_over.render("YOU", True, green, background)
        screen.blit(text_surf, (80, 100))
        text_surf = font_game_over.render("WON!", True, green, background)
        screen.blit(text_surf, (55, 200))

    pygame.display.flip()