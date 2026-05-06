(# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((680, 560))
robot = pygame.image.load("robot.png")

window.fill((0,0,0))
width = robot.get_width()
height = robot.get_height()

indent_w=0
indent_h=0
for row in range(1,11):
    for i in range(1,11):
        window.blit(robot, (indent_w+(width*i),indent_h+(height*1))) 
    indent_w +=width/5
    indent_h += height/5

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()