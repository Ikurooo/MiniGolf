import pygame
from pygame import Surface

from Obstacle import Obstacle


class Ball:
    def __init__(self, x: int, y: int, radius: int, color: list[int], velocity: list[float], friction: float):
        self.x: int = x
        self.y: int = y
        self.radius: int = radius
        self.color: tuple[int, ...] = tuple(color)
        self.velocity: list[float] = velocity  # Convert velocity to a list
        self.friction: float = friction

    def update(self, dt: float):
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt

        # Apply friction to slow down the ball
        self.velocity[0] *= self.friction
        self.velocity[1] *= self.friction

    def check_collision_with_window(self, window_width: int, window_height: int):
        if self.x - self.radius < 0 or self.x + self.radius > window_width:
            self.velocity[0] = -self.velocity[0]  # Reverse horizontal velocity on window edges
        if self.y - self.radius < 0 or self.y + self.radius > window_height:
            self.velocity[1] = -self.velocity[1]  # Reverse vertical velocity on window edges

    def check_collision_with_obstacle(self, obstacle: Obstacle):
        # Check collision between the ball and the obstacle
        ball_left: float = self.x - self.radius
        ball_right: float = self.x + self.radius
        ball_top: float = self.y - self.radius
        ball_bottom: float = self.y + self.radius

        obstacle_left: float = obstacle.rect.left
        obstacle_right: float = obstacle.rect.right
        obstacle_top: float = obstacle.rect.top
        obstacle_bottom: float = obstacle.rect.bottom

        # Check if any side of the ball is outside the obstacle
        if not (ball_right < obstacle_left or ball_left > obstacle_right or
                ball_bottom < obstacle_top or ball_top > obstacle_bottom):
            # Change the direction of the ball upon collision
            if self.x < obstacle_left or self.x > obstacle_right:
                self.velocity[0] = -self.velocity[0]  # Reverse horizontal velocity
            if self.y < obstacle_top or self.y > obstacle_bottom:
                self.velocity[1] = -self.velocity[1]  # Reverse vertical velocity

    def draw(self, window: Surface):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)
