import pygame 

class Button:
    def __init__(self, width , height, img, display):
        self.width = width
        self.height = height 
        self.img = img
        self.img = pygame.transform.scale(self.img, (width, height))
        self.display = display 

    def draw(self, x, y, func=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if click[0] == 1:
                print('Сработало!')
                if func is not None: 
                    return func()
        self.display.blit(self.img, (x,y))
                    