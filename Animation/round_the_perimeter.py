# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    if x+robot.get_width() < 640 and y == 0:
        x += velocity
    if y+robot.get_height() < 480 and x+robot.get_width() >= 640:
        y +=velocity
    if x+robot.get_width() <= 640 and y+robot.get_height() >= 480:
        x -= velocity
    if x ==0 and y+robot.get_height() <= 480:
        y -=velocity

    clock.tick(60)