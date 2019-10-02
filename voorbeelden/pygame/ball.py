import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif").convert_alpha()
ballrect = ball.get_rect()
mask = pygame.Surface(ball.get_size(), pygame.SRCALPHA)

i = 1

clock = pygame.time.Clock()
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)

    mask.blit(ball, (0,0))
    i = i + 1
    r = abs((i % 510) - 255)
    g = abs(((i * 2) % 510) - 255)
    b = abs(((i * 3) % 510) - 255)
    mask.fill((r, g, b, 255), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(mask, ballrect)
    pygame.display.flip()