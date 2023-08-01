# Scene Manager
# import Scene.S_Game as S_Game
import Scene.S_Menu as S_Menu
import pygame

class SceneManager:
    def __init__(self):
        # Add all to this dict
        self.SceneList = {
        # Menu Scenes
        'Menu':  S_Menu.MenuScene(),
        # 'Stats': S_Menu.StatsScene(),
        # 'Modes': S_Menu.ModesScene(),

        # GameMode Scenes
        # 'Game': S_Game.Gamemode_Original()
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

    def Update(self):
        # Update each individual aspect of game
        
        # Should I be putting the loop here?
        self.activeScene.Input()
        self.activeScene.Update()
        self.activeScene.Draw()
    
    def Run(self):
        # main game loop here
        while True:
            self.Update()




