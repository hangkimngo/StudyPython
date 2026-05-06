# WRITE YOUR SOLUTION HERE:

import random
import pygame
from pygame import display


pygame.init()

WIDTH = 640
HEIGHT = 480
CENTER = WIDTH // 2

window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill((0, 0, 0))
pygame.display.set_caption("Asteroids")
robot_image = pygame.image.load("robot.png")
rock_image = pygame.image.load("rock.png")
game_font = pygame.font.SysFont("Arial", 24)



class Robot:
    def __init__(self):
        self.x = 0
        self.y = 480-robot_image.get_height()
        self.speed = 5
        self.to_right = False
        self.to_left = False
        self.score = 0
    
    def move(self):
        if self.to_left:
            self.x -= self.speed
        if self.to_right:
            self.x += self.speed

      # keep robot inside window
        if self.x < 0:
            self.x = 0
        if self.x + robot_image.get_width() > WIDTH:
            self.x = WIDTH - robot_image.get_width()

class Rock:
    def __init__(self):
        self.x = random.randint(0, WIDTH - rock_image.get_width())
        self.y = -rock_image.get_height()
        self.speed_x = 0
        self.speed_y = 1
        self.falling = True

    def move(self):
        if self.falling:
            self.y += self.speed_y

    def touches_robot(self, robot: Robot):
        return (
            self.x < robot.x + robot_image.get_width() and
            self.x + rock_image.get_width() > robot.x and
            self.y < robot.y + robot_image.get_height() and
            self.y + rock_image.get_height() > robot.y
        )

def new_game():
    robot = Robot()
    rocks = []
    game_over = False
    return robot, rocks, game_over

robotti, rocks, game_over = new_game()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if game_over:
                robotti, rocks, game_over = new_game()

            if event.key == pygame.K_LEFT:
                robotti.to_left = True
            if event.key == pygame.K_RIGHT:
                robotti.to_right = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                robotti.to_left = False
            if event.key == pygame.K_RIGHT:
                robotti.to_right = False
            
    if not game_over:
        robotti.move()

         # sometimes create a new rock
        if random.randint(1, 60) == 1:
            rocks.append(Rock())

            # move rocks and check for collisions
        for rock in rocks[:]:
            rock.move()
            if rock.touches_robot(robotti):
                robotti.score += 1
                rocks.remove(rock)
            elif rock.y+rock_image.get_height() >= HEIGHT:
                game_over = True
    


    window.fill((0, 0, 0))
    text = game_font.render(f"Points: {robotti.score} ", True, (255, 0, 0))
    window.blit(text, (500, 10))

    for rock in rocks:
        window.blit(rock_image, (rock.x, rock.y))

    window.blit(robot_image, (robotti.x, robotti.y))

    if game_over:
        end_text = game_font.render("Game over! Press any key", True, (255, 0, 0))
        text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(end_text, text_rect)
    
    pygame.display.flip()
    clock.tick(60)

