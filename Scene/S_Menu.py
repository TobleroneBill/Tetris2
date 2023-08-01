from Scene.Scene import SceneTemplate, Quit
import Menu.UI
import pygame, sys

# Dont need a quit scene - this will just be button

# I am genuinely proud of this :)
class MenuScene(SceneTemplate):
    def __init__(self):
        super().__init__() # try this
        self.ButtonList = [
            Menu.UI.Button('TEST BUTTON',(self.SCREEN.get_width()//2,self.SCREEN.get_height()//2),100,80,function=print,FARGS=('Clicked')),
            ]
        self.keycount = 0


    def Input(self):
        eventList = super().Input()
        for event in eventList:
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                Quit()
            if event.type == pygame.KEYDOWN:
                self.keycount +=1
                print(self.keycount)

    def Update(self):   # 2
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