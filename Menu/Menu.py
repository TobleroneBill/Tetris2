# Loads game, and has screens for:
#   - Stats
#       - Blocks Places
#       - Highest Score
#       - Longest Time Survived
#       - Total Playtime
#   - Options
#   - GameModes

import Settings
import pygame
import math
from Menu.Helpers import Helper, Button

# Make a loop for each screen and swap between them
# Going to use an int, and then a match case block to change between different levels
ScreenNum = 0

Selection = 0

pygame.init()

SCREEN = pygame.display.set_mode(Settings.WINDOWSIZE)
pygame.display.set_caption('Tetris 2')
CLOCK = pygame.time.Clock()

# Holds variables for menu stuff
# class Menu:

def SceneSelect(Scene=0):

    # print(Scene)
    running = True
    while running:
        Helper.MouseCheck() # Mouse Movement for use whenever needed
        # print(Helper.mouseDelta)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
            
        match Scene:
            case 0:
                M_Main()
            case 1:
                M_Settings()
            case 2:
                M_Stats()
            case 3:
                M_GameModes()
            case 4:
                M_Quit()
            case _:
                M_Main()
        

        pygame.display.flip()
        CLOCK.tick(Settings.FPS)


def M_Main():
    SCREEN.fill((100,100,100))
    
    ButtonList = [
        Button('TEST BUTTON',(100,50),100,50,'hi',print,('hi'))
    ]

    for button in ButtonList:
        button.Update(SCREEN,(0,0,0))

    # Helper.DrawText(SCREEN,'Testing',36,(100,100),(255,255,255))
    
    # funny mouse movement
    Helper.DrawText(SCREEN,f'{CLOCK.get_fps() // 1}',36,(
        (SCREEN.get_width()//2) + Helper.mouseDelta[0] ,
        36//2),(255,255,255))

    pass

def M_Settings():
    pass

def M_Stats():
    pass

def M_GameModes():
    pass

def M_Quit():
    pass