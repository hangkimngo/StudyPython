import random
import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
CENTER = WIDTH // 2

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot invasion")
robot_image = pygame.image.load("robot.png")


class Robot:
    def __init__(self):
        self.x = random.randint(0, WIDTH - robot_image.get_width())
        self.y = -robot_image.get_height()
        self.speed_x = 0
        self.speed_y = random.randint(1, 5)
        self.falling = True

    def move(self):
        if self.falling:
            self.y += self.speed_y

            if self.y + robot_image.get_height() >= HEIGHT:
                self.y = HEIGHT - robot_image.get_height()
                if self.x + robot_image.get_width() >= CENTER:
                    self.speed_x = random.randint(1, 3)
                else:
                    self.speed_x = -random.randint(1, 3)
                self.speed_y = 0
                self.falling = False
        else:
            self.x += self.speed_x

    def outside_window(self):
        return self.x < -robot_image.get_width() or self.x > WIDTH


robots = []
for i in range( random.randint(5, 15)):
    robots.append(Robot())

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    

    window.fill((0, 0, 0))

    for robot in robots[:]:
        robot.move()
        window.blit(robot_image, (robot.x, robot.y))

        if robot.outside_window():
            robots.remove(robot)

    pygame.display.flip()
    clock.tick(60)
