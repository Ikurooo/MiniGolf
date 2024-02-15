import pygame
from Ball import Ball
from Obstacle import Obstacle


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ball = Ball(400, 400, 25, (255, 100, 100), [0, 0], 0.99)
        self.obstacle = Obstacle(300, 700, 100, 100, (255, 0, 255))

    def update(self, dt):
        self.ball.update(dt)
        self.ball.check_collision_with_window(self.width, self.height)
        self.ball.check_collision_with_obstacle(self.obstacle)

    def draw(self, window):
        window.fill((0, 200, 100))  # Fill the window with a white color
        # Draw green checker pattern
        square_size = 50
        for x in range(0, self.width, square_size):
            for y in range(0, self.height, square_size):
                if (x // square_size + y // square_size) % 2 == 0:
                    pygame.draw.rect(window, (0, 250, 100), (x, y, square_size, square_size))
        self.obstacle.draw(window)
        self.ball.draw(window)
