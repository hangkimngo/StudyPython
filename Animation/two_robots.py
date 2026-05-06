# # WRITE YOUR SOLUTION HERE:
# import pygame

# pygame.init()
# window = pygame.display.set_mode((640, 480))

# robot = pygame.image.load("robot.png")

# x = 0
# y = 0
# velocity = 1
# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()

#     window.fill((0, 0, 0))
#     window.blit(robot, (x, 40))
#     clock.tick(60)
#     window.blit(robot, (x, 60+robot.get_height()))
#     pygame.display.flip()
    
#     x += velocity
#     if velocity > 0 and x+robot.get_width() >= 640:
#         velocity = -velocity
#     if velocity < 0 and x <= 0:
#         velocity = -velocity

#     clock.tick(40)

import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two robots")

robot = pygame.image.load("robot.png")

x1 = 0
x2 = 0

speed1 = 1
speed2 = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    window.blit(robot, (x1, 100))
    window.blit(robot, (x2, 300))

    x1 += speed1
    x2 += speed2

    if x1 <= 0 or x1 + robot.get_width() >= WIDTH:
        speed1 = -speed1

    if x2 <= 0 or x2 + robot.get_width() >= WIDTH:
        speed2 = -speed2

    pygame.display.flip()
    clock.tick(60)