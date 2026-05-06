# WRITE YOUR SOLUTION HERE:# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")


x = random.randint(0, 640-robot.get_width())
y = random.randint(0, 480-robot.get_height())
clicked = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] >= x and event.pos[0] <= x + robot.get_width():
                clicked = True
                if event.pos[1] >= y and event.pos[1] <= y + robot.get_height():
                    clicked = True
                else:   
                    clicked = False
            else:
                clicked = False


        if event.type == pygame.QUIT:
            exit(0)

    if clicked:
        x = random.randint(0, 640-robot.get_width())
        y = random.randint(0, 480-robot.get_height())
        clicked = False

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
