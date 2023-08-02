# Generic Scene
import Settings
import pygame


'''
**Scene Methods copypasta**

class ClassName(SceneTemplate):
    def __init__(self,Manager):
        super().__init__(Manager)

        
    def Input(self):    # 1
        super().Input()


    def Update(self):   # 2
        super().Update()        


    def Draw(self):     # 3
        super().Draw()
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
        return pygame.event.get()


    def Update(self):   # 2
        self.CLOCK.tick(Settings.FPS)


    def Draw(self):     # 3
        pygame.display.update()

