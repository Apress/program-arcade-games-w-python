"""
Use sprites to pick up blocks

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Explanation video: http://youtu.be/iwLj7iJCFQM
"""
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Block(pygame.sprite.Sprite):
    """
    This class represents the block to be picked up.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


class Player(Block):
    """ This class represents the player. It derives from block and thus gets
    the same ___init___ method we defined above. """

    # List of all the blocks we are carrying
    carry_block_list = []

    def update(self):
        """ Method called when updating a sprite. """

        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Now see how the mouse position is different from the current
        # player position. (How far did we move?)
        diff_x = self.rect.x - pos[0]
        diff_y = self.rect.y - pos[1]

        # Loop through each block that we are carrying and adjust
        # it by the amount we moved.
        for block in self.carry_block_list:
            block.rect.x -= diff_x
            block.rect.y -= diff_y

        # Now wet the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Player(RED, 20, 15)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # When the mouse button is pressed, see if we are in contact with
            # other sprites:
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)

            # Set the list of blocks we are in contact with as the list of
            # blocks being carried.
            player.carry_block_list = blocks_hit_list

        elif event.type == pygame.MOUSEBUTTONUP:
            # When we let up on the mouse, set the list of blocks we are
            # carrying as empty.
            player.carry_block_list = []

    all_sprites_list.update()

    # Clear the screen
    screen.fill(WHITE)

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
