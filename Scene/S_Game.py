#/_______________________________________________/SCENE SETTINGS/_______________________________________________/
from Scene.Scene import SceneTemplate, Quit
import GameFuncs.GameFuncs
import pygame

import Menu.UI # for debug
from Settings import WINDOWCENTER

#/_______________________________________________/GAME MODES/_______________________________________________/

# Regular Tetris
# When testing transition - set this to black window with center text saying "GAME"

class Gamemode_Original(SceneTemplate):
    
    def __init__(self,Manager) -> None:
        super().__init__(Manager)
    
    # simple input and then upgrade if I feel necassary
    def Input(self):    # 1
        eventList = super().Input()
        for event in eventList:
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                Quit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    self.Manager.SetScene('Menu')

    def Update(self):   # 2
        super().Update()

    def Draw(self):     # 3
        self.SCREEN.fill((0,0,0))
        Menu.UI.Helper.DrawText(self.SCREEN,'GAMING',100,WINDOWCENTER,(255,255,255))
        super().Draw()
