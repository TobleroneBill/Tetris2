#/_______________________________________________/SCENE SETTINGS/_______________________________________________/
from Scene.Scene import SceneTemplate
import pygame
import Tetris.Tetris as Game

import Menu.UI # for debug
from Settings import WINDOWCENTER

#/_______________________________________________/GAME MODES/_______________________________________________/

# Regular Tetris
# When testing transition - set this to black window with center text saying "GAME"

# I could copy paste the old tetris code and put it here just to try stuff

class Gamemode_Original(SceneTemplate):
    
    def __init__(self,Manager) -> None:
        super().__init__(Manager)   # inherits stuff
        # self.game = Game.TetrisDefault()
        self.game = Game.DebugRoomInput()
    
    # simple input and then upgrade if I feel necassary
    def Input(self,input):    # 1
        pass

    def Update(self):   # 2
        super().Update()

    def Draw(self):     # 3
        self.SCREEN.fill((0,0,0))
        Menu.UI.Helper.DrawText(self.SCREEN,'GAMING',100,WINDOWCENTER,(255,255,255))
        super().Draw()
