# Initialize Pygame
import sys
import pygame
from Field import Field

FPS: int = 120
pygame.init()

# Set up the window
width = 600
height = 1000
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Window")

# Create the game field
game_field = Field(width, height)

# Run the game loop
while True:
    dt = pygame.time.Clock().tick(FPS) / 100.0  # Calculate delta time (time elapsed between frames in seconds)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update and draw the game field
    game_field.update(dt)
    game_field.draw(window)

    # Update the display
    pygame.display.flip()
