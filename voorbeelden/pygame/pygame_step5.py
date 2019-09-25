import sys, pygame
from pygame.locals import *

pygame.init()

background = 0, 0, 0
ball_color = 255, 255, 255
size = width, height = 640, 480
ball_position = 320, 240
ball_speed = 2, 2
player_speed = 5
player_position = width / 2, height - 20

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    keystate = pygame.key.get_pressed()
    direction = 0
    if keystate[K_RIGHT]:
        direction = 1
    elif keystate[K_LEFT]:
        direction = -1
    player_position = player_position[0] + player_speed * direction, player_position[1]

    if ball_position[0] < 0 or ball_position[0] > width:
        ball_speed = (-ball_speed[0], ball_speed[1])
    if ball_position[1] < 0 or ball_position[1] > height:
        ball_speed = (ball_speed[0], -ball_speed[1])
    ball_position = ball_position[0] + ball_speed[0], ball_position[1] + ball_speed[1]
    
    screen.fill(background)
    pygame.draw.circle(screen, ball_color, ball_position, 10)
    paddle = pygame.Rect(player_position[0], player_position[1], 60, 10)
    pygame.draw.rect(screen, ball_color, paddle)
    pygame.display.flip()