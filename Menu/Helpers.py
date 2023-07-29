import pygame

class Helper:
    # Keeps track of mouse stuff
    mouseDelta = [0,0]
    mousePrev = None
    
    
    def MouseCheck() -> None:
        """
        Records the mouse delta - Movement per frame
        """

        if Helper.mousePrev == None:
            Helper.mousePrev = pygame.mouse.get_pos()
        elif pygame.mouse.get_pos() != Helper.mousePrev:
            Helper.mouseDelta = [pygame.mouse.get_pos()[0] - Helper.mousePrev[0],pygame.mouse.get_pos()[1] - Helper.mousePrev[1]]
            Helper.mousePrev = pygame.mouse.get_pos()
        else:
            Helper.mouseDelta = [0,0]


    @staticmethod
    def DrawText(screen,text,size,position,color,AA=False) -> None:
        """
        Draws text to the screen given

        Keyword arguments:
        screen -- Pygame.surface
        text -- String to write
        size -- Int - text size in .pt (I think)
        position -- (x,y) - Location on screen to be rendered at
        AA -- Anti Aliasing
        """
        font = pygame.font.Font(None,size)
        text = font.render(text,AA,color)
        text_rect = text.get_rect()
        text_rect.center = position
        screen.blit(text,text_rect)

# Need a button which can be selected
class Button:
    # not interactive yet
    def __init__(self,Text,Position,width,height,*Args):
        """
        Draws text to the screen given

        Keyword arguments:

        text -- String to write

        position -- (x,y) Location on screen to be rendered at

        width -- Box Width

        height -- Box Height

        DoFunc -- Function Refrence to be called when clicked

        Args  -- Tuple of args to be sent to the DoFunc when clicked

        """

        self.text = Text

        self.position = Position
        self.width = width
        self.height = height

        # Function to be executed on click
        self.Execute = Args[0]
        self.Args = Args[1]

        self.clicked = False

        self.surface = pygame.Surface(Position,flags=pygame.SRCALPHA)
        self.Rect = pygame.Rect(Position,(width,height))
    
    # -> Describes the return type, not input parameters
    def Draw(self,Window,BG,Border=True) -> None: 
        # Draw: Border - BG - Text
        if not Border:
            self.surface.fill(BG)
        Helper.DrawText(self.surface,self.text,20,(self.width//2,self.height//2),(255,255,255))
        Window.blit(self.surface,self.Rect)
    
    # TODO: make this good
    #   issues:
    #       - Functions as variables
    #       - Single click functionallity
    # Draws and Logic
    def Update(self,Window,BG) -> None:
        
        if self.CheckCollision():
            if pygame.mouse.get_pressed() == (1,0,0) and not self.clicked:
                self.clicked = True
            else:
                self.clicked = False


        self.Draw(Window,BG,Border=False)
    
    # If mouse is inside the box
    def CheckCollision(self):
        if self.Rect.collidepoint(pygame.mouse.get_pos()):
            self.surface.set_alpha(125)
            return True
        self.surface.set_alpha(255)
        return False
        
    

