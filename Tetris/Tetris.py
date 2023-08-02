# import BoardList
from Tetris import GameFuncs, BoardList
import random

#/_______________________________________________/Tests/_______________________________________________/

# Needs to check for input
# idk how i want the input to be....

# need to make input class
# Basically i need a room with width of the board
# Make a 1x1 block, which will be center of influence
# 

class DebugRoomInput:
    def __init__(self):
        pass

# shouldnt have any draw calls, just general game logic
# A rendering class is gonna be made for that, so we can apply effects without worring for the game logic
class TetrisDefault:

    def __init__(self):
        self.board = BoardList.DefaultBoard # holds board
        
        self.line_clears = 0
        self.score = 0
        self.Level = 0
        self.pieceList = [random.randint(0,7) for x in range(8)]
        print(self.pieceList)

