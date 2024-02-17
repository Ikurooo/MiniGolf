import pygame
from Ball import Ball
from Obstacle import Obstacle


class Field:
    def __init__(self, width, height, level):
        self.width = width
        self.height = height
        self.ball = None
        self.obstacles = []
        self.load_level(level)

    def load_level(self, level):
        with open("levels.txt") as file:
            for number, line in enumerate(file):
                if number == level:
                    params = line.strip().split(";")
                    ball_params = params[0].strip().split(",")
                    self.ball = Ball(
                        x=int(ball_params[0]),
                        y=int(ball_params[1]),
                        radius=25,
                        color=tuple(map(int, ball_params[2].split('.'))),
                        velocity=[0, 0],
                        friction=0.9900
                    )

                    for i in range(1, len(params) - 1):
                        obstacle_params = params[i].strip().split(",")
                        obstacle = Obstacle(
                            x=int(obstacle_params[0]),
                            y=int(obstacle_params[1]),
                            width=int(obstacle_params[2]),
                            height=int(obstacle_params[3]),
                            color=tuple(map(int, obstacle_params[4].strip().split('.')))
                        )
                        self.obstacles.append(obstacle)
                    break

    def update(self, dt):
        self.ball.update(dt)
        self.ball.check_collision_with_window(self.width, self.height)
        # TODO: add spacial hash table
        for obstacle in self.obstacles:
            self.ball.check_collision_with_obstacle(obstacle)

    def draw(self, window):
        window.fill((0, 200, 100))  # Fill the window with a white color
        # Draw green checker pattern
        square_size = 50
        for x in range(0, self.width, square_size):
            for y in range(0, self.height, square_size):
                if (x // square_size + y // square_size) % 2 == 0:
                    pygame.draw.rect(window, (0, 250, 100), (x, y, square_size, square_size))
        for obstacle in self.obstacles:
            obstacle.draw(window)
        self.ball.draw(window)
