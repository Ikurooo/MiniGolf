import pygame


class Ball:
    def __init__(self, x, y, radius, color, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = list(velocity)  # Convert velocity to a list

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def check_collision_with_window(self, window_width, window_height):
        if self.x - self.radius < 0 or self.x + self.radius > window_width:
            self.velocity[0] = -self.velocity[0]  # Reverse horizontal velocity on window edges
        if self.y - self.radius < 0 or self.y + self.radius > window_height:
            self.velocity[1] = -self.velocity[1]  # Reverse vertical velocity on window edges

    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)
