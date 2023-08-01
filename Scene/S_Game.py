#/_______________________________________________/SCENE SETTINGS/_______________________________________________/
import Scene.Scene
import GameFuncs.GameFuncs

import Menu.UI # for debug


#/_______________________________________________/GAME MODES/_______________________________________________/

# Regular Tetris
# When testing transition - set this to black window with center text saying "GAME"
class Gamemode_Original(Scene):
    def __init__(self) -> None:
        pass
    # simple input and then upgrade if I feel necassary
    def Input(self):    # 1
        pass

    def Update(self):   # 2
        pass

    def Draw(self):     # 3
        Menu.UI.Helper.DrawText()

# Could seperate these, but seems unnecessary/needlessly long. organizational purposes :thinking: hmmm
