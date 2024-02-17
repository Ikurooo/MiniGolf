import pygame


class Hole:
    def __init__(self, x, y):
        self.color = (0, 0, 0)
        self.x = x
        self.y = y
        self.radius = 35

    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)
