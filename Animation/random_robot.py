# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

window.fill((0,0,0))
width = robot.get_width()
height = robot.get_height()

indent_w=0
indent_h=0
for i in range(1000):
    window.blit(robot, (random.randint(0,640-width),random.randint(0,480-height)) )


pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()