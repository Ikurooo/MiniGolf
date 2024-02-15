import pygame


class Ball:
    def __init__(self, x, y, radius, color, velocity, friction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = list(velocity)  # Convert velocity to a list
        self.friction = friction

    def update(self, dt):
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt

        # Apply friction to slow down the ball
        self.velocity[0] *= self.friction
        self.velocity[1] *= self.friction

    def check_collision_with_window(self, window_width, window_height):
        if self.x - self.radius < 0 or self.x + self.radius > window_width:
            self.velocity[0] = -self.velocity[0]  # Reverse horizontal velocity on window edges
        if self.y - self.radius < 0 or self.y + self.radius > window_height:
            self.velocity[1] = -self.velocity[1]  # Reverse vertical velocity on window edges

    def check_collision_with_obstacle(self, obstacle):
        # Check collision between the ball and the obstacle
        ball_left = self.x - self.radius
        ball_right = self.x + self.radius
        ball_top = self.y - self.radius
        ball_bottom = self.y + self.radius

        obstacle_left = obstacle.rect.left
        obstacle_right = obstacle.rect.right
        obstacle_top = obstacle.rect.top
        obstacle_bottom = obstacle.rect.bottom

        # Check if any side of the ball is outside the obstacle
        if ball_right < obstacle_left or ball_left > obstacle_right or ball_bottom < obstacle_top or ball_top > obstacle_bottom:
            pass
        else:
            # Change the direction of the ball upon collision
            if self.x < obstacle_left or self.x > obstacle_right:
                self.velocity[0] = -self.velocity[0]  # Reverse horizontal velocity
            if self.y < obstacle_top or self.y > obstacle_bottom:
                self.velocity[1] = -self.velocity[1]  # Reverse vertical velocity

    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)
