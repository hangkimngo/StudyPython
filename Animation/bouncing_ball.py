# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x=0
y=0

speed_x=3
speed_y=3

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x,y))
    x += speed_x
    y += speed_y
    pygame.display.flip()
    if x <= 0 or x + ball.get_width() >= 640:
        speed_x = -speed_x

    if y <= 0 or y + ball.get_height() >= 480:
        speed_y = -speed_y



    clock.tick(60)