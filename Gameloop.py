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
ball = Ball(100, 100, 25, (255, 100, 100), [10, 10])

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
    window.fill((0, 200, 100))  # Fill the window with a white color
    # Draw green checker pattern
    square_size = 50
    for x in range(0, width, square_size):
        for y in range(0, height, square_size):
            if (x // square_size + y // square_size) % 2 == 0:
                pygame.draw.rect(window, (0, 250, 100), (x, y, square_size, square_size))
    ball.draw(window)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(120)
