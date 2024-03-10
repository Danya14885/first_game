import pygame
import random

cloud_img = [pygame.image.load("Assets/img/Cloud0.png"), pygame.image.load("Assets/img/Cloud1.png")]


class Object:
    def __init__(self, y, img, display_width, display_height, speed):
        self.param = pygame.Rect(display_width + random.randint(0,300), display_height-y+random.randrange(10, 80), 50, 50)
        self.img = img
        self.speed = speed
    
def open_random_objects(display_width, display_height):
    choise = random.randrange(0, 2)
    img_of_cloud = cloud_img[choise]

    cloud = Object(800, img_of_cloud, display_width, display_height, 2)
    return cloud

def move(object:Object, display, display_width):
    if object.param.x >= -object.param.width:
        display.blit(object.img, (object.param.x, object.param.y))
        object.param.x -= object.speed
    else: 
            object.param.x = display_width + 100 +random.randint(-80, 60)
            object.param.y = object.param.y + random.randint(-20, 20)

