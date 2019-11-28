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

# nieuw stuk code om de mijnen te plaatsen:
# (bovenaan is ook 'randint' geimporteerd, om willekeurige getallen te krijgen)
# dit is het moeilijkste stukje code van minesweeper :)

# ik maak gebruik van een hulp-functie. Je kan zelf functies schrijven die je
# vanop andere plaatsen kan oproepen. Dat kan het makkelijker maken om het
# overzicht te bewaren.

# neighbours (= Engels voor 'buren') is een functie die, gegeven x en y, een lijst
# van alle buren teruggeeft, die binnen het spelbord liggen.
# Normaal zijn dit er 8, behalve aan de rand van het bord.
# Bijvoorbeeld:
# neighbours(5, 7) => [(4, 6), (4, 7), (5, 6), (6, 6), (6, 7)]
# want (5,7) zelf is geen buur van (5,7), en (4, 8), (5, 8) en (6, 8)
# liggen buiten het spelbord.
# Er zijn meerdere manieren om deze functie te maken, hier is er eentje:
def neighbours(x, y):
    candidates = []
    # maak een lijst met 9 posities: de middenste en de 8 buren
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            candidates.append((x+dx, y+dy))
    # verwijder de middenste positie opnieuw
    candidates.remove((x, y))
    # en verwijder alle posities die buiten het bord liggen
    for (el_x, el_y) in list(candidates):
        if el_x < 0 or el_y < 0 or el_x > 7 or el_y > 7:
            candidates.remove((el_x, el_y))
    return candidates

# je kan je eigen functies makkelijk uittesten door ze op te roepen:
print("neighbours(5, 7) =>")
print(neighbours(5, 7))
# maar dit stukje code gaan we in de volgende stap terug wegdoen,
# want het is maar een test

# hier gaan we 10 mijnen op willekeurige plaatsen zetten...
num_mines_placed = 0
while num_mines_placed < 10:
    x, y = randint(0, 7), randint(0, 7)
    # ... alleen als er nog geen mijn staat ...
    if minefield[x][y] != "X":
        minefield[x][y] = "X"
        # en voor elke mijn moeten we het getal van de vakjes ernaast verhogen
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

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 50)

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                (cursor_x, cursor_y) = pygame.mouse.get_pos()
                grid_x = cursor_x // 50
                grid_y = cursor_y // 50
                if grid[grid_x][grid_y] == "?":
                    grid[grid_x][grid_y] = "F"
                elif grid[grid_x][grid_y] == "F":
                    grid[grid_x][grid_y] = "?"

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