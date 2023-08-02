#/_______________________________________________/GAME FUNCTIONS/_______________________________________________/
import numpy as np

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