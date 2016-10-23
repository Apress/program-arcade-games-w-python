""" 
 Show how to open a window for OpenGL graphics
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 This program is based off the ideas in the excellent tutorials
 at http://nehe.gamedev.net/
"""

import OpenGL.GL 
import OpenGL.GLU
import pygame

def resize_gl_scene(size):
    height = size[1]
    width = size[0]

    OpenGL.GL.glViewport(0, 0, width, height)
    OpenGL.GL.glMatrixMode(OpenGL.GL.GL_PROJECTION)
    OpenGL.GL.glLoadIdentity()
    OpenGL.GLU.gluPerspective(45, 1.0 * width / height, 0.1, 100.0)
    OpenGL.GL.glMatrixMode(OpenGL.GL.GL_MODELVIEW)
    OpenGL.GL.glLoadIdentity()

def init_gl():
    OpenGL.GL.glShadeModel(OpenGL.GL.GL_SMOOTH)
    OpenGL.GL.glClearColor(0.0, 0.0, 0.0, 0.0)
    OpenGL.GL.glClearDepth(1.0)
    OpenGL.GL.glEnable(OpenGL.GL.GL_DEPTH_TEST)
    OpenGL.GL.glDepthFunc(OpenGL.GL.GL_LEQUAL)
    OpenGL.GL.glHint(OpenGL.GL.GL_PERSPECTIVE_CORRECTION_HINT, OpenGL.GL.GL_NICEST)

def draw_gl_scene():
    OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT | OpenGL.GL.GL_DEPTH_BUFFER_BIT)
    OpenGL.GL.glLoadIdentity()

def main():
    """ Main function for the game. """
    
    # Get Pygame ready
    pygame.init()
    
    # Set the width and height of the screen [width,height]
    size = (640,480)
    video_flags = pygame.OPENGL | pygame.DOUBLEBUF    
    screen = pygame.display.set_mode(size, video_flags)

    # Create an OpenGL viewport
    resize_gl_scene(size)
    init_gl()

    # These are for calculating FPS
    frames = 0
    ticks = pygame.time.get_ticks()
    
    done = False
    
    while not done:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            done = True
        
        draw_gl_scene()
        pygame.display.flip()
        frames = frames + 1
        
    total_ticks = pygame.time.get_ticks() - ticks
    print("Average of {:.1f} fps".format((frames * 1000) / total_ticks))
    
    pygame.quit()

if __name__ == "__main__":
    main()
