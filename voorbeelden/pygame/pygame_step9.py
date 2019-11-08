import sys, pygame
from pygame.locals import *

pygame.init()

background = 0, 0, 0
ball_color = 255, 255, 255
size = width, height = 640, 480
ball_rect = pygame.Rect(320, 240, 50, 50)
ball_speed = 2, 2
player_speed = 5
player_rect = pygame.Rect(width / 2, height - 20, 60, 10)
game_over = False

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
ball = pygame.image.load("intro_ball.gif").convert_alpha()
ball = pygame.transform.smoothscale(ball, ball_rect.size)

font = pygame.font.SysFont("Arial", 50)

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
    player_rect.move_ip(player_speed * direction, 0)

    if ball_rect.colliderect(player_rect):
        ball_speed = (ball_speed[0], -ball_speed[1])
    if ball_rect.left < 0 or ball_rect.right > width:
        ball_speed = (-ball_speed[0], ball_speed[1])
    if ball_rect.top < 0:
        ball_speed = (ball_speed[0], -ball_speed[1])
    if ball_rect.bottom > height:
        ball_speed = (0, 0)
        game_over = True

    ball_rect.move_ip(ball_speed)
    
    screen.fill(background)
    screen.blit(ball, ball_rect)
    pygame.draw.rect(screen, ball_color, player_rect)
    if game_over:
        text = font.render("Game over!", 0, (255, 0, 0), background)
        screen.blit(text, (10, 10))

    pygame.display.flip()