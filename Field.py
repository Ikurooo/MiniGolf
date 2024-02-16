import pygame
from Ball import Ball
from Obstacle import Obstacle


class Field:
    def __init__(self, width, height, level):
        self.width = width
        self.height = height
        self.ball = None
        self.obstacle = None
        self.load_level(level)

    def load_level(self, level):
        with open("levels.txt") as file:
            for number, line in enumerate(file):
                if number == level:
                    params = line.strip().split(";")
                    self.ball = Ball(
                        int(params[0]),
                        int(params[1]),
                        int(params[2]),
                        tuple(map(int, params[3].split(','))),
                        [0, 0],
                        float(params[4])
                    )

                    self.obstacle = Obstacle(
                        int(params[5]),
                        int(params[6]),
                        int(params[7]),
                        int(params[8]),
                        tuple(map(int, params[9].strip().split(',')))
                    )
                    print(self.obstacle.color)
                    break

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
