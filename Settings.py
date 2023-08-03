import pygame
import enum
SCALE = 1
WINDOWSIZE = (1024 * SCALE,1024 * SCALE)  # 1:1 RATIO
FPS = 60
WINDOWCENTER = (WINDOWSIZE[0]//2,WINDOWSIZE[1]//2,)

# Key Bindings
class Keys(enum.Enum):
    MOVELEFT = pygame.K_a
    MOVERIGHT = pygame.K_d

    MOVEUP = pygame.K_w
    MOVEDOWN = pygame.K_s
    

    SOFTDROP = pygame.K_s
    HARDDROP = pygame.K_SPACE   # this might be broken on my keyboard idk
    ROTATELEFT = pygame.K_LEFT
    ROTATERIGHT= pygame.K_RIGHT
    HOLD = pygame.K_LSHIFT
    PAUSE = pygame.K_ESCAPE
    C = pygame.K_c
