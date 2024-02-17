# Initialize Pygame
import sys
import pygame
from Field import Field

FPS: int = 120
pygame.init()

# Set up the window
width = 1000
height = 1000
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mini Golf")

# Create the game field
game_field = Field(width, height, 0)

# Run the game loop
while True:
    dt = pygame.time.Clock().tick(FPS) / 100.0  # Calculate delta time (time elapsed between frames in seconds)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
            game_field.drag_start = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left mouse button released
            drag_end = pygame.mouse.get_pos()
            delta_x = drag_end[0] - game_field.drag_start[0]
            delta_y = drag_end[1] - game_field.drag_start[1]

            # Add the delta values to the ball's velocity
            game_field.ball.velocity[0] -= delta_x  # You can adjust the scale factor for sensitivity
            game_field.ball.velocity[1] -= delta_y

            game_field.drag_start = None  # Reset the drag start position

    # Update and draw the game field
    game_field.update(dt)
    game_field.draw(window)

    # Update the display
    pygame.display.flip()
