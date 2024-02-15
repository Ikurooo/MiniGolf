import pygame


class Ball:
    def __init__(self, x, y, width, height, color, velocity):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.velocity = velocity

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def check_collision_with_window(self, window_width, window_height):
        if self.rect.left < 0 or self.rect.right > window_width:
            self.velocity = (-self.velocity[0], self.velocity[1])  # Reverse horizontal velocity on window edges
        if self.rect.top < 0 or self.rect.bottom > window_height:
            self.velocity = (self.velocity[0], -self.velocity[1])  # Reverse vertical velocity on window edges
