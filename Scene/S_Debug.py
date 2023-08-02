# Debug levels
from Scene.Scene import SceneTemplate
import Menu.UI as Menu
import Settings
import sys

import copy

class InputDebug(SceneTemplate):
    def __init__(self,Manager):
        super().__init__(Manager)
        self.RenderString = ''
        self.LastInput = ''
        self.rawLast = None
        self.TimeHeld = 0

    def Input(self,input):    # 1
        input.GetInput()
        


    def Update(self):   # 2
        super().Update()
        sessionKeys = self.Manager.InputManager.GetSessionKeys()
        HoldTime = self.Manager.InputManager.GetHeldTime()
        HoldTime *= 3
        if HoldTime >= 255:
            HoldTime = 255

        self.TimeHeld = HoldTime

        TotalInputs = len(sessionKeys)
        SizeInputs = sys.getsizeof(sessionKeys)
        
        if sessionKeys[-1] != []:
            self.LastInput = ','.join(sessionKeys[-1])
            self.rawLast = sessionKeys[-1]

        self.RenderString = f'Total Inputs: {TotalInputs}\nList Size: {SizeInputs}'


    def Draw(self):     # 3
        self.SCREEN.fill((0,0,0))
        Menu.Helper.DrawText(self.SCREEN,self.RenderString,30,Settings.WINDOWCENTER,(255,255,255))
        Menu.Helper.DrawText(self.SCREEN,self.LastInput,30,(Settings.WINDOWCENTER[0],300),(255,self.TimeHeld,self.TimeHeld))

        super().Draw()