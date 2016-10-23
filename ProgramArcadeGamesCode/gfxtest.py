# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

# http://cprogramtutorials.blogspot.com/2011/09/bresenhams-ellipse-drawing-algorithm-c.html
# http://www.gamedev.sk/files/programming/bresenham/ellipse.as
import pygame
import pygame.gfxdraw

def drawEllipse(surface, x0, y0, a, b, color, width=1):
    if (a == 0 or b == 0):
        return;
    a = abs(a);
    b = abs(b);
    a2 = 2*a * a;
    b2 = 2*b * b;
    error = a*a*b;
    x = 0;
    y = b;
    stopy = 0;
    stopx = a2 * b ;
    while (stopy <= stopx):
        if width > 1:
            pygame.gfxdraw.filled_circle(surface,x0 + x, y0 + y,width,color);
            pygame.gfxdraw.filled_circle(surface,x0 - x, y0 + y,width,color);
            pygame.gfxdraw.filled_circle(surface,x0 - x, y0 - y,width,color);
            pygame.gfxdraw.filled_circle(surface,x0 + x, y0 - y,width,color);
        else:
            pygame.gfxdraw.pixel(surface,x0 + x, y0 + y,color);
            pygame.gfxdraw.pixel(surface,x0 - x, y0 + y,color);
            pygame.gfxdraw.pixel(surface,x0 - x, y0 - y,color);
            pygame.gfxdraw.pixel(surface,x0 + x, y0 - y,color);

        x += 1
        error -= b2 * (x - 1);
        stopy += b2;
        if (error <= 0):
            error += a2 * (y - 1);
            y -= 1
            stopx -= a2;
    
    error = b*b*a;
    x = a;
    y = 0;
    stopy = b2*a;
    stopx = 0;
    while (stopy >= stopx):
        if width > 1:
            pygame.gfxdraw.filled_circle(surface,x0 + x, y0 + y,width,color)
            pygame.gfxdraw.filled_circle(surface,x0 - x, y0 + y,width,color)
            pygame.gfxdraw.filled_circle(surface,x0 - x, y0 - y,width,color)
            pygame.gfxdraw.filled_circle(surface,x0 + x, y0 - y,width,color)
        else:
            pygame.gfxdraw.pixel(surface,x0 + x, y0 + y,color)
            pygame.gfxdraw.pixel(surface,x0 - x, y0 + y,color)
            pygame.gfxdraw.pixel(surface,x0 - x, y0 - y,color)
            pygame.gfxdraw.pixel(surface,x0 + x, y0 - y,color)
            
        y += 1;
        error -= a2 * (y - 1);
        stopx += a2;
        if (error < 0):
            error += b2 * (x - 1);
            x -= 1
            stopy -= b2;
        
   
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width,height]
size=[700,500]
screen=pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
 
# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  
  
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
     
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
     
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(white)
    alpha=0
    for x in range(75,401,10):
        alpha +=2
        pygame.gfxdraw.filled_circle(screen,x,100,50,(255,0,0,alpha))
    
    y=50
    alpha=0
    for x in range(75,401,5):
        y+=2
        alpha +=1
        pygame.gfxdraw.box(screen,(x,y,50,50),(0,0,255,alpha))
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    drawEllipse(screen,200,200,130,130,(0,64,64),20)
    #drawEllipse(screen,60,60,50,50,(0,64,64))
    
    x_radius=5
    for x in range(100,700,50):
        
        #drawEllipse(screen,x,400,x_radius,30,(0,64,64))
        x_radius += 2
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(20)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()