# Debug levels
from Scene.Scene import SceneTemplate
import Menu.UI as Menu
import Settings
from Settings import Keys
import sys
import Helpers

# Snake imports
import random
import numpy as np
import pygame

class InputDebug(SceneTemplate):
    def __init__(self,Manager):
        super().__init__(Manager)
        self.RenderString = ''
        self.LastInput = ''
        self.rawLast = None
        self.TimeHeld = 0

    def Input(self):    # 1
        # self.Manager.InputManager.GetInput()
        pass
        


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

# Basic Snake game for Input Testing
# Gonna try putting it inside a board too

class SnakeDebug(SceneTemplate):
    # THIS IS AN ABOMINATION
    # They look like ants :)
    # and it runs super slow - 

    ColorPallete = [
        0xf72585,   # Purple
        0xb5179e,
        0x7209b7,
        0x560bad,
        0x480ca8,
        0x3a0ca3,
        0x3f37c9,
        0x4361ee,
        0x4895ef,
        0x4cc9f0    # Cyan
    ]

    BoardSize = (25,25) # X,Y

    def __init__(self,Manager):
        super().__init__(Manager)
        pygame.display.set_caption('Snake')
        pygame.mouse.set_visible(False)
        # This isnt streamed well
        # TODO: test fullscreen on end of session
        # self.SCREEN = pygame.display.set_mode(Settings.WINDOWSIZE,pygame.FULLSCREEN)
        
        self.C_Player = (random.choice(SnakeDebug.ColorPallete[2:-1]))
        self.C_BG = SnakeDebug.ColorPallete[0]
        self.C_Apple = SnakeDebug.ColorPallete[-1]

        self.C_Grid = (80,80,80)

        self.length = 1
        self.Score = 0
        self.time = 0

        self.Direction = 0
        self.PlayerPos = [[SnakeDebug.BoardSize[0]//2,SnakeDebug.BoardSize[1]//2]]

        self.Speed = 1
        
        self.Tickrate = 6
        self.time = 0

        self.ApplePos = [random.randint(0,SnakeDebug.BoardSize[0]),random.randint(0,SnakeDebug.BoardSize[1])]

        self.Paused = False
        self.Grid = np.array([[0 for x in range(SnakeDebug.BoardSize[0])] for y in range(SnakeDebug.BoardSize[1])])
        # how do we dynamically calculate this...

        # I cant really explain this, but this is just how it works
        self.RatioX = Helpers.Ratio(SnakeDebug.BoardSize[1],SnakeDebug.BoardSize[0]) # = .5
        self.RatioY = Helpers.Ratio(SnakeDebug.BoardSize[0],SnakeDebug.BoardSize[1]) # = 2.0

        self.GridW = Settings.WINDOWSIZE[0] * (Helpers.Ratio(SnakeDebug.BoardSize[0],self.RatioX) * self.RatioY)
        self.GridH = Settings.WINDOWSIZE[1] * (Helpers.Ratio(SnakeDebug.BoardSize[1],self.RatioY) * self.RatioX)

        print(self.RatioX,self.RatioY)
        print(self.GridW,self.GridH)


    def Collision(self):
        # Apple
        if self.PlayerPos[0] == self.ApplePos:
            self.Score += (len(self.PlayerPos) * self.Speed)
            
            # dumb way:
            if self.Direction == 0: # Left
                self.PlayerPos.append([self.PlayerPos[0][0] - self.Speed,self.PlayerPos[0][1]])
            if self.Direction == 1: # Right
                self.PlayerPos.append([self.PlayerPos[0][0] + self.Speed,self.PlayerPos[0][1]])
            if self.Direction == 2: # Up
                self.PlayerPos.append([self.PlayerPos[0][0],self.PlayerPos[0][1] - self.Speed])
            if self.Direction == 3: # Down
                self.PlayerPos.append([self.PlayerPos[0][0],self.PlayerPos[0][1] + self.Speed])
            self.AddMove(-self.Speed)
            self.MakeApple()

    def AddMove(self,speed):
        # Thier method just has a list that pops when its lifetime has exceeded the length kind of -
        # Stuff at the back of the list gets popped, and a new player position is added to the end keeping length and board positions
        if self.Direction == 0: # Left
            self.PlayerPos.append([self.PlayerPos[0][0] - speed,self.PlayerPos[0][1]])
        if self.Direction == 1: # Right
            self.PlayerPos.append([self.PlayerPos[0][0] + speed,self.PlayerPos[0][1]])
        if self.Direction == 2: # Up
            self.PlayerPos.append([self.PlayerPos[0][0],self.PlayerPos[0][1] - speed])
        if self.Direction == 3: # Down
            self.PlayerPos.append([self.PlayerPos[0][0],self.PlayerPos[0][1] + speed])
        del self.PlayerPos[0]
                
    # Move player        
    def Input(self):    # 1
        super().Input()
        if self.INPUT.CheckKey(Keys.PAUSE):
            Helpers.Quit()
                
        if self.INPUT.CheckKey(Keys.MOVELEFT):
            self.Direction = 0
        if self.INPUT.CheckKey(Keys.MOVERIGHT):
            self.Direction = 1
        if self.INPUT.CheckKey(Keys.MOVEUP):
            self.Direction = 2
        if self.INPUT.CheckKey(Keys.MOVEDOWN):
            self.Direction = 3
        
        # print(self.Direction)
        
        
    def OOBCheck(self):
        for segment in (self.PlayerPos):
            # X positions
            if segment[0] == SnakeDebug.BoardSize[0]:
                segment[0] = 0
            if segment[0] < 0:
                segment[0] = SnakeDebug.BoardSize[0]-1

            if segment[1] == SnakeDebug.BoardSize[1]:
                segment[1] = 0
            if segment[1] < 0:
                segment[1] = SnakeDebug.BoardSize[1]-1
            

    def Update(self):   # Game Logic
        if self.time % self.Tickrate == 0:
            self.AddMove(self.Speed)
            self.OOBCheck()
            self.Collision()
            self.time = 0
        self.time+=1
        super().Update()
    
    def DrawGrid(self):
        for x in range(SnakeDebug.BoardSize[0]):
            for y in range(SnakeDebug.BoardSize[1]):
                Cell = pygame.Rect(x*self.GridW*1.1,y*self.GridH*1.1,self.GridW*0.9,self.GridH*0.9)
                Cell = pygame.Rect(x*self.GridW,y*self.GridH,self.GridW,self.GridH)

                
                if (x,y) == tuple(self.ApplePos):
                    pygame.draw.rect(self.SCREEN,self.C_Apple,Cell)
        
    def DrawBoard(self):
        for segment in self.PlayerPos:
            BorderCell = pygame.Rect(segment[0]*self.GridW,segment[1]*self.GridH,self.GridW,self.GridH)
            Cell = pygame.Rect(segment[0]*self.GridW*1.1,segment[1]*self.GridH*1.1,self.GridW*0.9,self.GridH*0.9)

            pygame.draw.rect(self.SCREEN,self.C_Grid,BorderCell)
            pygame.draw.rect(self.SCREEN,self.C_Player,Cell)

        Apple = pygame.Rect(self.ApplePos[0]*self.GridW,self.ApplePos[1]*self.GridH,self.GridW,self.GridH)
        pygame.draw.rect(self.SCREEN,self.C_Apple,Apple)


    def MakeApple(self):
        self.ApplePos = [random.randint(2,SnakeDebug.BoardSize[0]-2),random.randint(2,SnakeDebug.BoardSize[1]-2)]

    def Draw(self):     # Drawing 
        # Draw board
        self.SCREEN.fill((0,0,0))
        Menu.Helper.DrawText(self.SCREEN,f'{self.Score}',100,Settings.WINDOWCENTER,(255,255,255),opacity=100)
        self.DrawBoard()
        super().Draw()