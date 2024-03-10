import pygame 
import random

class Cactus:
    def __init__(self, param, img, display_width, display_height):
        self.param = pygame.Rect(display_width + random.randint(0, 300),
                                 display_height - 100 - param[1],
                                 param[0],
                                 param[1])
        
        self.img = img