import pygame

class Helper:

    # Keeps track of mouse stuff
    mouseDelta = [0,0]
    mousePrev = None
    def MouseCheck():
        # Update MouseDelta
        if Helper.mousePrev == None:
            Helper.mousePrev = pygame.mouse.get_pos()
        elif pygame.mouse.get_pos() != Helper.mousePrev:
            Helper.mouseDelta = [pygame.mouse.get_pos()[0] - Helper.mousePrev[0],pygame.mouse.get_pos()[1] - Helper.mousePrev[1]]
            Helper.mousePrev = pygame.mouse.get_pos()
        else:
            Helper.mouseDelta = [0,0]


    @staticmethod
    def DrawText(screen,text,size,position,color,AA=False):
        font = pygame.font.Font(None,size)
        text = font.render(text,AA,color)
        text_rect = text.get_rect()
        text_rect.center = position
        screen.blit(text,text_rect)

# Need a button which can be selected
class Button:
    # not interactive yet
    def __init__(self,Text,Position,width,height):
        self.text = Text

        self.position = Position
        self.width = width
        self.height = height

        self.surface = pygame.Surface(Position,flags=pygame.SRCALPHA)
        self.Rect = pygame.Rect(Position,(width,height))
    
    # -> Describes the return type, not input parameters
    def Draw(self,Window,BG,Border=True): 

        # Draw: Border - BG - Text
        if not Border:
            self.surface.fill(BG)
        
        Helper.DrawText(self.surface,self.text,20,(self.width//2,self.height//2),(255,255,255))
        
        Window.blit(self.surface,self.Rect)
        

