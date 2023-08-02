import pygame
import time
from math import sin

# TODO Buttons with functions attached

class Helper:
    # Keeps track of mouse stuff
    mouseDelta = [0,0]
    mousePrev = None
    
    def MouseCheck() -> None:
        """
        Records the mouse delta - Movement per frame
        """
        if Helper.mousePrev == None:
            Helper.mousePrev = pygame.mouse.get_pos()
        elif pygame.mouse.get_pos() != Helper.mousePrev:
            Helper.mouseDelta = [pygame.mouse.get_pos()[0] - Helper.mousePrev[0],pygame.mouse.get_pos()[1] - Helper.mousePrev[1]]
            Helper.mousePrev = pygame.mouse.get_pos()
        else:
            Helper.mouseDelta = [0,0]


    @staticmethod
    def DrawText(screen,text,size,position,color,AA=False) -> None:
        """
        Draws text to the screen given

        Keyword arguments:
        screen -- Pygame.surface
        text -- String to write
        size -- Int - text size in .pt (I think)
        position -- (x,y) - Location on screen to be rendered at
        AA -- Anti Aliasing
        """
        font = pygame.font.Font(None,size)
        text = font.render(text,AA,color)
        text_rect = text.get_rect()
        text_rect.center = position
        screen.blit(text,text_rect)

    @staticmethod
    def Ratio(x,y) -> float:
        '''Returns Y/X '''
        return y/x

# Need a button which can be selected
class Button:
    # not interactive yet
    def __init__(self,Text,Position,width,height,function=None,FARGS=None):
        """
        Draws text to the screen given

        Keyword arguments:

        text -- String to write

        position -- (x,y) Location on screen to be rendered at

        width -- Box Width

        height -- Box Height

        DoFunc -- Function Refrence to be called when clicked

        Args  -- Tuple of args to be sent to the DoFunc when clicked

        """

        self.text = Text

        self.position = Position
        self.width = width
        self.height = height

        # Function to be executed on click
        self.function = function
        if FARGS:
            self.Args = [FARGS,]

        self.clicked = False
        self.selected = False
        self.StrobeTime = 4
        self.surface = pygame.Surface((width,height),flags=pygame.SRCALPHA)
        self.Rect = pygame.Rect((Position[0] - width//2,Position[1] - height//2),(width,height))
        # print(self.Rect.center)

    
    # -> Describes the return type, not input parameters
    def Draw(self,Window,BG,Border=3) -> None: 
        # Draw: Border - BG - Text
        self.surface.fill((0,0,0))

        rightSide = self.width - (Border*2)
        BotSide = self.height - (Border*2)
        # bg Fill
        
        drawBG = BG
        if self.selected:
            a,b,c = BG
            sinWave = sin(time.time()) * 50
            drawBG = (a + sinWave,b + sinWave,c + sinWave)

        if self.clicked:
            self.surface.set_alpha(125)
        else:
            self.surface.set_alpha(255)

 
        # Regular
        pygame.draw.rect(self.surface,drawBG,(0+Border,0+Border,rightSide,BotSide))
        Helper.DrawText(self.surface,self.text,20,(self.width//2,self.height//2),(255,255,255))
        Window.blit(self.surface,self.Rect)
    
    # Draws and Logic
    def Update(self,Window,BG) -> None:
        self.CheckCollision()
        self.Draw(Window,BG)
    
    # If mouse is inside the box
    def CheckCollision(self):

        if self.Rect.collidepoint(pygame.mouse.get_pos()):
            self.selected = True

            if pygame.mouse.get_pressed() == (1,0,0) and self.selected:
                self.clicked = True
                
                # self.function(self.Args[0])
                self.selected = False

            if pygame.mouse.get_pressed() == (0,0,0) and self.selected:
                self.clicked = False
        else:
            self.clicked = False
            self.selected = False
        # print(self.selected,self.clicked)
