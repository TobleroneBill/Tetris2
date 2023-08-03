# Scene Manager
# import Scene.S_Game as S_Game
import Scene.S_Menu as S_Menu
import Scene.S_Game as S_Game
import Scene.S_Debug as S_Debug
import Tetris.Input as Input
import pygame
from Helpers import Quit



# Need some way for the scene to tell the scenemanager to switch scenes 
#   - Scenes all have a refrence to the scene manager # think this is the best idea, its kind of already set up this way

class SceneManager:
    def __init__(self):

        self.InputManager = Input.InputManager()            # Handles input

        # Add all to this dict
        self.SceneList = {
        # Menu Scenes
        'Menu':  S_Menu.MenuScene(self),
        # 'Stats': S_Menu.StatsScene(),
        # 'Modes': S_Menu.ModesScene(),

        # GameMode Scenes
        'Game': S_Game.Gamemode_Original(self),

        # Debug Scenes
        'DebugInput' : S_Debug.InputDebug(self),
        'DebugSnakeTest' : S_Debug.SnakeDebug(self)

    }
        self.activeScene = self.SceneList['DebugSnakeTest']     #
        self.Run()

    
    def SetScene(self,SceneName):
        # Should never happen - take out when stable
        if SceneName not in self.SceneList.keys():
            raise ValueError
        self.activeScene = self.SceneList[SceneName]
        
    
    def Run(self):
        # main game loop here
        while True:

            # send inputmanager keys to current level, which will have more specific instructions
            self.activeScene.Input()
            
            # Update Game Logic
            self.activeScene.Update()
            
            # Draw Game
            self.activeScene.Draw()




