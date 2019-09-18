import sys, pygame, random
pygame.init()

size = width, height = 640, 480
black = 0, 0, 0
color = 255, 255, 255

screen = pygame.display.set_mode(size)
screen.fill(black)

p = random.randint(0, width), random.randint(0, height)
p1 = 0, height
p2 = width // 2, 0
p3 = width, height

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    target = [p1, p2, p3][random.randint(0, 2)]
    p = (p[0] + target[0]) // 2, (p[1] + target[1]) // 2

    pygame.draw.circle(screen, color, p, 1)

    pygame.display.flip()