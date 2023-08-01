# Scene Manager
# import Scene.S_Game as S_Game
import Scene.S_Menu as S_Menu
import Scene.S_Game as S_Game

import pygame

# Need some way for the scene to tell the scenemanager to switch scenes 
#   - Scenes all have a refrence to the scene manager # think this is the best idea, its kind of already set up this way

class SceneManager:
    def __init__(self):
        # Add all to this dict
        self.SceneList = {
        # Menu Scenes
        'Menu':  S_Menu.MenuScene(self),
        # 'Stats': S_Menu.StatsScene(),
        # 'Modes': S_Menu.ModesScene(),

        # GameMode Scenes
        'Game': S_Game.Gamemode_Original(self)
    }
        self.activeScene = self.SceneList['Menu']
        
        # (delay,interval) in Ms (1000 ms in 1 second)
        pygame.key.set_repeat(700,80)   # Key repetition stuff
        self.Run()

    
    def SetScene(self,SceneName):
        # Should never happen - take out when stable
        if SceneName not in self.SceneList.keys():
            raise ValueError
        self.activeScene = self.SceneList[SceneName]
        
    
    def Run(self):
        # main game loop here
        while True:
            self.activeScene.Input()
            self.activeScene.Update()
            self.activeScene.Draw()




