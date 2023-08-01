# Generic Scene
import Settings
import pygame, sys

def Quit():
    pygame.quit()
    sys.exit()

'''
Scene Methods copypasta:

    def __init__(self) -> None:
        pass
        
    def Input(self):    # 1
        pass


    def Update(self):   # 2
        pass


    def Draw(self):     # 3
        pass
'''

class SceneTemplate:
    def __init__(self,Manager) -> None:
        print('Making Default stuff')
        self.Manager = Manager
        pygame.init()
        self.SCREEN = pygame.display.set_mode(Settings.WINDOWSIZE)
        pygame.display.set_caption('Screen')
        self.CLOCK = pygame.time.Clock()

    # simple input and then upgrade if I feel necassary
    def Input(self):    # 1
        return [event for event in pygame.event.get()]


    def Update(self):   # 2
        self.CLOCK.tick(Settings.FPS)


    def Draw(self):     # 3
        pygame.display.flip()

