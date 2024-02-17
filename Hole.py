import pygame
from pygame import Surface


class Hole:
    def __init__(self, x: int, y: int):
        self.color: tuple[int, ...] = (0, 0, 0)
        self.x: int = x
        self.y: int = y
        self.radius: int = 35

    def draw(self, window: Surface):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)
