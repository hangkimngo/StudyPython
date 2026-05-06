# WRITE YOUR SOLUTION HERE:
import pygame
from datetime import datetime
import math

pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock() 

center = (320, 240)
radius = 200


def hand_end_position(length, angle):
    x = center[0] + math.cos(angle) * length
    y = center[1] + math.sin(angle) * length
    return (x, y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    now = datetime.now()
    pygame.display.set_caption(now.strftime("%H:%M:%S"))

    seconds = now.second
    minutes = now.minute
    hours = now.hour % 12

    second_angle = math.radians(seconds * 6 - 90)
    minute_angle = math.radians(minutes * 6 - 90)
    hour_angle = math.radians(hours * 30 - 90)

    display.fill((0, 0, 0))

    pygame.draw.circle(display, (255,0,0), center, radius, 4)
    pygame.draw.circle(display, (255,0,0), center, 10, 10)
    pygame.draw.line(display, (0,0,255), center, hand_end_position(180, second_angle), 1)
    pygame.draw.line(display, (0,0,255), center, hand_end_position(170, minute_angle), 3)
    pygame.draw.line(display, (0,0,255), center, hand_end_position(140, hour_angle), 5)


    pygame.display.flip()
    clock.tick(60)
