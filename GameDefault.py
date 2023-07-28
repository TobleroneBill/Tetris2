import pygame 
import numpy as np
import random
import Settings

# GOALS:
#   - Need a resizable window that scales

#   - All things have to mutate a single board - No making new ones (unless you are screwed)
#       - We need to be able to set the board state on load for custom boards (testing atm)
#           - Do need a puzzle board, but could be a modification of this as long as its solid as rocks

#   - Tetris pieces 1-7 + 1x1 blocks (for testing)
#       - Make test rooms for checking specific scenarios
#           - Side collisions
#           - Block collisions
#           - Wierd Tspin stuff
#           - Any other odd things (make a more detailed list somewhere)

#   - Need better input handling than last time
#       - Think I was trying to amalgam mutliple different styles of input from my own ideas and actual tetris
#       - Make a design Doc for this

#   - A system of showing Active pieces with any possible color

#   - Graphics
#       - CLEAR ART STYLE
#       - Good Tetris pieces
#       - Particles on line clears


# make empty default board
def makeBoard():
    return np.array([[0 for x in range(10)] for y in range(24)])

# Runs game
def Run(board=makeBoard()): 
    # Pygame settings
    pygame.init()
    SCREEN = pygame.display.set_mode(Settings.WINDOWSIZE)
    CLOCK = pygame.time.Clock()

    # Main game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        pygame.display.flip()
        CLOCK.tick(Settings.FPS)
    # SICK
    board = np.array(board)
    print(board)

    # Quit the game properly
    pygame.quit()