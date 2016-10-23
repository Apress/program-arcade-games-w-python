"""
 Simple graphics demo

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653

# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Rotate Text")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

text_rotate_degrees = 0

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Draw some borders
    pygame.draw.line(screen, BLACK, [100,50], [200, 50])
    pygame.draw.line(screen, BLACK, [100,50], [100, 150])

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Sideways text
    text = font.render("Sideways text", True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, [0, 0])

    # Sideways text
    text = font.render("Upside down text", True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, [30, 0])

    # Flipped text
    text = font.render("Flipped text", True, BLACK)
    text = pygame.transform.flip(text, False, True)
    screen.blit(text, [30, 20])

    # Animated rotation
    text = font.render("Rotating text", True, BLACK)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    text_rotate_degrees += 1
    screen.blit(text, [100, 50])

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
