
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

window.fill((0,0,0))
window.blit(robot, (0,0))
window.blit(robot, (640-robot.get_width(),0))
window.blit(robot, (0,480-robot.get_height()))
window.blit(robot, (640-robot.get_width(),480-robot.get_height()))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
