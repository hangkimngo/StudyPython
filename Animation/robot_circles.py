import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

center_x, center_y = 320-robot.get_width()/2, 240-robot.get_height()/2

radius = 120
angle_offset = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for i in range(10):
        angle = angle_offset+ (2 * math.pi / 10) * i   # split circle into 10

        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        window.blit(robot, (x, y))

    angle_offset += 0.01
    pygame.display.flip()