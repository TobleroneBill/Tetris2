from Scene.Scene import SceneTemplate
from Helpers import Quit

import Menu.UI
import pygame, sys
from Settings import WINDOWCENTER

# Dont need a quit scene - this will just be button

# Loads game, and has Scenes for:
#   - Play Game
#   - Stats
#       - Blocks Places
#       - Highest Score
#       - Longest Time Survived
#       - Total Playtime
#   - Options
#   - GameModes


# I am genuinely proud of this :)
class MenuScene(SceneTemplate):
    def __init__(self,Manager):
        super().__init__(Manager)
        self.ButtonList = [
            Menu.UI.Button('TEST BUTTON',WINDOWCENTER,100,80,function=print,FARGS=('Clicked')),
            ]
        self.keycount = 0

    def Input(self):
        pass
        # for event in eventList:
            # if event.type == pygame.KEYDOWN:
            #     if pygame.key.get_pressed()[pygame.K_RIGHT]:
            #         self.Manager.SetScene('Game')
            #     self.keycount +=1
            #     print(self.keycount)


    def Update(self):   # 2
        if self.ButtonList[0].clicked:
            self.Manager.SetScene('Game')
        super().Update()

    def Draw(self):     # 3
        self.SCREEN.fill((100,100,100))

        for button in self.ButtonList:
            button.Update(self.SCREEN,(80,80,80))

        Menu.UI.Helper.DrawText(self.SCREEN,f'{int(self.CLOCK.get_fps())}',36,(
        (self.SCREEN.get_width()//2) + Menu.UI.Helper.mouseDelta[0] ,
        36//2),(255,255,255))
        
        super().Draw()


'''
class StatsScene(Scene):
    pass

    
class ModesScene(Scene):
    pass
'''