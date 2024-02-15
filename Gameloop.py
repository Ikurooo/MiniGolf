import pygame
import sys
from Ball import Ball


# Initialize Pygame
pygame.init()

# Set up the window
width, height = 600, 1000
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Window")

# Create a ball object
ball = Ball(100, 100, 50, 50, (0, 0, 255), (5, 2))

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the ball position
    ball.update()

    # Check for collisions with window boundaries
    ball.check_collision_with_window(width, height)

    # Draw something on the window
    window.fill((255, 255, 255))  # Fill the window with a white color
    pygame.draw.rect(window, ball.color, ball.rect)  # Draw the ball

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
