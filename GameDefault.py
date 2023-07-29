import pygame 
import numpy as np
import random
import Settings

# GOALS:
#   - Need a resizable window that scales

#   - All things have to mutate a single board - No making new ones (unless you are screwed)
#       - We need to be able to set the board state on load for custom boards (testing atm)
#           - Do need a puzzle board, but could be a modification of this as long as its solid as rocks

TEST ADDITION

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

# Makes the pieces, but how do I keep colors ....
def MakePiece(typenum):
    # I coords
    if typenum == 1:
        return ((0, 1), (0, 0), (0, -1), (0, -2))
    # T coords
    if typenum == 2:
        return ((-1, 0), (0, 0), (1, 0), (0, -1))
    # O coords
    if typenum == 3:
        return ((0, 0), (0, 1), (1, 0), (1, 1))
    # L piece
    if typenum == 4:
        return ((-1, 1), (-1, 0), (0, 0), (1, 0))
    # J piece
    if typenum == 5:
        return ((1, 1), (-1, 0), (0, 0), (1, 0))
    # s piece
    if typenum == 6:
        return ((-1, 0), (0, 0), (0, 1), (1, 1))
    # z piece
    if typenum == 7:
        return ((1, 0), (0, 0), (0, 1), (-1, 1))
    # 1x1 block for testing
    if typenum == 8:
        return ((0, 0))

# make empty default board
def makeBoard():
    return np.array([[0 for x in range(10)] for y in range(24)])

# Runs game
def Run(board=makeBoard(),Level = 1): 
    # Pygame settings
    pygame.init()
    SCREEN = pygame.display.set_mode(Settings.WINDOWSIZE)
    CLOCK = pygame.time.Clock()
    # Game settings
    board = np.array(board)
    print(board)

    # Main game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        pygame.display.flip()
        CLOCK.tick(Settings.FPS)
        
    # Quit the game properly
    pygame.quit()