#/_______________________________________________/INPUT HANDLER/_______________________________________________/

# RECORDS INPUT - could be saved for replays?
# 
import pygame
import Settings
from Helpers import Quit
import sys
# TODO: control flow needs figuring out
# TODO: Certian inputs messed up when held - check on another PC if this is still the case

# Control Flow:
# Scene Manager calls scene update with argument (InputManager.getInput)
class InputManager:
    def __init__(self):
        self.SessionKeys = [] # List of keypresses every tick for playback
        self.timeHeld = 0
        pygame.init()
        pygame.key.set_repeat(400,40)   # Key repetition stuff

    def GetSessionKeys(self):
        return self.SessionKeys

    def GetHeldTime(self):
        return self.timeHeld

    def CheckKey(self,KeyCheck):
        '''
        Checks if specified key is pressed

        Parameters:
            KeyCheck (Settings.Key): The key to check for
        '''
        # print(Settings.Keys.HARDDROP.name)
        if self.SessionKeys[-1] == []:
            return False
        if self.SessionKeys[-1] == [KeyCheck.name]:
            return True
        return False



    def GetInput(self):
        inputList = []
        for event in pygame.event.get():
            # if event map key is one of the matching enum values then we have a match
            if pygame.key.get_pressed()[pygame.K_1] or event.type == pygame.QUIT:
                print(self.SessionKeys,f'len: {len(self.SessionKeys)}')
                print(f'Sessions Size: {sys.getsizeof(self.SessionKeys)}')
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.dict['key'] in Settings.Keys._value2member_map_:
                    self.timeHeld +=1
                    print(Settings.Keys(event.dict['key']).name,self.timeHeld)
                    inputList.append(Settings.Keys(event.dict['key']).name)
            else:
                self.timeHeld = 0
        self.SessionKeys.append(inputList)
        
        return inputList
