import pygame
from pygame import Rect, Surface


class Obstacle:
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int, ...]):
        self.rect: Rect = pygame.Rect(x, y, width, height)
        self.color: tuple[int, ...] = color

    def draw(self, window: Surface):
        pygame.draw.rect(window, self.color, self.rect)

