import sys, pygame
from pygame.locals import *

pygame.init()

black = 0, 0, 0
white = 255, 255, 255

size = width, height = 640, 480

ball_rect = pygame.Rect(width / 2, height / 2, 5, 5)
ball_speed = 2, 2
player_speed = 5
p1 = pygame.Rect(width / 2, 10, 40, 10)
p2 = pygame.Rect(width / 2, height - 20, 40, 10)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keystate = pygame.key.get_pressed()

    direction = keystate[K_RIGHT] - keystate[K_LEFT]
    p1.move_ip(player_speed * direction, 0)

    direction = keystate[K_d] - keystate[K_a]
    p2.move_ip(player_speed * direction, 0)

    ball_rect = ball_rect.move(ball_speed)
    
    if ball_rect.colliderect(p1) or ball_rect.colliderect(p2):
        ball_speed = (ball_speed[0], -ball_speed[1])
    if ball_rect.left < 0 or ball_rect.right > width:
        ball_speed = (-ball_speed[0], ball_speed[1])
    if ball_rect.top < 0 or ball_rect.bottom > height:
        ball_speed = (0, 0)

    screen.fill(black)
    pygame.draw.circle(screen, white, ball_rect.center, 5)
    pygame.draw.rect(screen, white, p1)
    pygame.draw.rect(screen, white, p2)
    pygame.display.flip()