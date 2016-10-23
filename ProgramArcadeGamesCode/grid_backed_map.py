"""
Show how to use an array backed grid in a graphics game.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 20
HEIGHT = 20
MARGIN = 5

# --- Create grid of numbers
# Create an empty list
grid = []
# Loop for each row
for row in range(10):
    # For each row, create a list that will
    # represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(10):
        # Add a number to the current row
        grid[row].append(0)

# Set row 1, column 5 to zero
grid[1][5] = 1

pygame.init()

screen_size = [255, 255]
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column_clicked = pos[0] // (WIDTH + MARGIN)
            row_clicked = pos[1] // (HEIGHT + MARGIN)
            print("Row:", row_clicked, "Column:", column_clicked)
            grid[row_clicked][column_clicked] = 1

    # Set the screen background
    screen.fill(BLACK)

    for row in range(10):
        for column in range(10):
            if grid[row][column] == 0:
                color = WHITE
            else:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [MARGIN + (WIDTH + MARGIN) * column,
                              MARGIN + (HEIGHT + MARGIN) * row,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
