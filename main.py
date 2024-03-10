import pygame, random
from cactus import Cactus
from Objects import Object, open_random_objects, move
from Button import Button 
import os
import sys



pygame.init()

clock = pygame.time.Clock()
display_width = 1080
display_height = 720
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dion')
icon = pygame.image.load('Assets/img/icon.png')
pygame.display.set_icon(icon)



menu_fon = pygame.image.load('Assets/img/menu_fon.png')
menu_fon = pygame.transform.scale(menu_fon, (1080, 720))






pause_button = Button(72, 70, pygame.image.load('Assets/img/pause.png'), display)


fon_1 = pygame.image.load("Assets/img/fon.png")
fon_x = 0
fon_width = 3240
fon_height = 720
fon_y = 0
fon_1 = pygame.transform.scale(fon_1, (fon_width, fon_height))

fon_2 = pygame.image.load("Assets/img/fon.png")
fon_2_x = 2000
fon_2 = pygame.transform.scale(fon_2, (fon_width, fon_height))


health_img = pygame.image.load("Assets/img/heart.png")
health = 3
health_img = pygame.transform.scale(health_img, (40, 40))


jump_sound0 = pygame.mixer.Sound("Assets/sounds/jump/прыжок0.mp3")
jump_sound1 = pygame.mixer.Sound("Assets/sounds/jump/прыжок1.mp3")
jump_sound2 = pygame.mixer.Sound("Assets/sounds/jump/прыжок2.mp3")
jump_sound3 = pygame.mixer.Sound("Assets/sounds/jump/прыжок3.mp3")
jump_sound4 = pygame.mixer.Sound("Assets/sounds/jump/прыжок4.mp3")
funny_sound = pygame.mixer.Sound("Assets/sounds/funny sound/смешной звук.mp3")
fail_sound = pygame.mixer.Sound("Assets/sounds/fail/проигрыш.mp3")
fail_sound.set_volume(0.1)


jump_sounds = [jump_sound0, jump_sound1, jump_sound2, jump_sound3, jump_sound4]

pygame.mixer.music.load("Assets/sounds/fon music/фоновая музыка.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


cactus_img = []
direction_cactus = 'Assets/img/cactus/'
list_files = os.listdir(direction_cactus)
for i in list_files:
    cactus_img.append(pygame.image.load(direction_cactus + i))
print(cactus_img)

lives = 3

print(cactus_img[0].get_size())

cactus_param = [(69, 51), (37, 90), (40,80)] 

img_player = []
direction_player = 'Assets/img/player/'
list_files = os.listdir(direction_player)
for i in list_files:
    img_player.append(pygame.image.load(direction_player + i))

cloud = open_random_objects(display_height, display_width)

player_width = 60
player_height = 80
player_x = 100
player_y = 600 - player_height
player = pygame.Rect(player_x, player_y, player_width, player_height)
make_jump = False
jump_counter = 30

cactus_width = 20
cactus_height = 70
cactus_x = display_width
cactus_y = 600 - cactus_height
cactus = pygame.Rect(cactus_x, cactus_y, cactus_width, cactus_height)

bird_width = 100
bird_height = 15
bird_x = display_width
bird_y = 300
bird = pygame.Rect(bird_x, bird_y, bird_width, bird_height)

def run_fon():
    global fon_x, fon_2_x
    if fon_x < fon_2_x:
        display.blit(fon_1, (fon_x ,fon_y))
        display.blit(fon_2, (fon_2_x, fon_y))
    else:
        display.blit(fon_2, (fon_2_x, fon_y))
        display.blit(fon_1, (fon_x ,fon_y))
        
    if fon_x <= -2000:
        fon_x = 2000
    else:
        fon_x -= 2

    if fon_2_x <= -2000:
        fon_2_x = 2000
    else:
        fon_2_x -= 2
    print(fon_x, fon_2_x)
        

def draw_cactus(cactus):
    global cactus_list
    if cactus.param.x >= -cactus.param.width:
        display.blit(cactus.img, cactus.param)
        cactus.param.x -= 4
    else:
        cactus_list.remove(cactus)
        cactus_list = create_cactus(cactus_list)

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        print_text('Paused. Press enter to continue', 270, display_height // 2)

        keys = pygame.key.get_pressed()
        if keys [pygame.K_RETURN]:     
            paused = False 
        pygame.display.update()
        clock.tick(15)

#def draw_bird(bird):
    #if bird.x >= -bird.width:
        #pygame.draw.rect(display, (128, 128, 0), bird)
        #bird.x -= 4
    #else:
        #bird.x = display_width + random.randint(0, 500)
        
def print_text(message, x, y, color=(0,0,0), font_type = "Assets/font/Aguante-Regular.otf", font_size = 30):
    font = pygame.font.Font(font_type, font_size)
    text = font.render(message, True, color)
    display.blit(text, (x, y))

def create_cactus(cactus_list:list):
    choise = random.randint(0, len(cactus_img)-1)
    img = cactus_img[choise]
    param = cactus_img[choise].get_size()
    if len(cactus_list) == 0:
        cactus_list.append(Cactus(param, img, display_width, display_height))
    elif cactus_list[-1].param.x < display_width:
        cactus_list.append(Cactus(param, img, display_width, display_height))
    else: 
        cactus_list.append(Cactus(param, img, cactus_list[-1].param.x + 300, display_height))
    return cactus_list

    #cactus_list.append(pygame.Rect(cactus_x + random.randint(300, 350), cactus_y, cactus_width, cactus_height))
    #cactus_list.append(pygame.Rect(cactus_x + random.randint(350, 700), cactus_y, cactus_width, cactus_height))
    #cactus_list.append(pygame.Rect(cactus_x + random.randint(1150, 1500), cactus_y, cactus_width, cactus_height))
    #cactus_list.append(pygame.Rect(cactus_x + random.randint(1500, 1850), cactus_y, cactus_width, cactus_height))
    #cactus_list.append(pygame.Rect(cactus_x + random.randint(1850, 2000), cactus_y, cactus_width, cactus_height))
    #cactus_list.append(pygame.Rect(cactus_x + random.randint(2000, 2200), cactus_y, cactus_width, cactus_height))

def create_list_cactus(count):
    l = []    
    for i in range(count):
        l  = create_cactus(l)
    return l
    

def show_health():
    global health
    show = 0
    x = 20 
    while health != show:
        display.blit(health_img, (x, 10))
        x = x + 40
        show = show + 1

count_cactus = 4
cactus_list = create_list_cactus(count_cactus)

def create_bird(bird_list:list):
    bird_list.append(pygame.Rect(bird_x + random.randint(0, 500), bird_y  - 100, bird_width, bird_height))
    bird_list.append(pygame.Rect(bird_x + random.randint(500, 1000), bird_y - 100, bird_width, bird_height))

bird_list = []
create_bird(bird_list)

s_jump = False 

def jump():
    global player, make_jump, jump_counter, s_jump 
    if jump_counter>= -30:
        player.y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30 
        make_jump = False
        player.y = player_y
        s_jump = False

n = len(img_player) * 5
img_counter = n

def draw_player():
    
    global img_counter, n 
    if img_counter == n:
        img_counter = 0

    display.blit(img_player[img_counter // 5], (player.x, player.y))
    img_counter += 1


def check_health():
    global health
    health = health - 1
    print("health", health)
    if health == 0:
        fail_sound.play()
        return False 
    else:
        return True

stop_pause = True
def get_click():
    global stop_pause
    stop_pause = False


def function_pause():
    global stop_pause
    show = True 
   
    continue_button = Button(100, 100, pygame.image.load("Assets/img/continue.png"), display)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        continue_button.draw(500, 320, get_click)
        if not stop_pause:
            break
        pygame.display.update()
        clock.tick(30)
    

score = 0 
above = False

def count_score(bariers):
    global score, above
    if not above:
        for barier in bariers:
            barier = barier.param
            if barier.x <= player.x + player.width / 2 <= barier.x + barier.width:
                if player.y +player.height - 5 <= barier.y:
                    above = True 
                    break
    else:
        if jump_counter == -30:
            score += 1
            above = False

def run_game(): 
    game = True
    global make_jump, lives, cactus_list, s_jump, health, pause_button
    health = 3
    create_cactus(cactus_list)
    while game:
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        move(cloud, display, display_width)
        keys = pygame.key.get_pressed()
        if keys [pygame.K_SPACE]:
            make_jump = True 
            if s_jump == False:
                r_s = random.choice(jump_sounds)
                r_s.set_volume(0.1)
                r_s.play()
                s_jump = True

        if keys [pygame.K_UP]:
            funny_sound.play()
            


        if keys[pygame.K_ESCAPE]:
            pause()

        if make_jump:
            jump()
        #display.fill((255, 255, 255))
        run_fon()
        pause_button.draw(950, 10, function_pause)
        count_score(cactus_list)
        print_text("score " + str(score), 500, 10)
        #button.draw(300, 200)
        show_health()
        #pygame.draw.rect(display, (100, 100, 123), player)
        
        draw_player()
        
        for i in cactus_list:
            draw_cactus(i)
            if i.param.colliderect(player):
               
                if not check_health():
                    game = False 
                # cactus_list.remove(i)
                # cactus_list = create_cactus(cactus_list)
                cactus_list = create_list_cactus(count_cactus)
        show_health()      
        #for i in bird_list:
            #draw_bird(i)

        if keys[pygame.K_LSHIFT]:
            print_text("Name: Danya, Age: 13", 20, 670, font_size=30)

        if keys[pygame.K_e]:
            print_text("Danya", 20, 20, font_size = 30)
        

        pygame.display.update()
        clock.tick(60)
    # return game_over()
    show_menu()

def exit_game():

    for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.quit()
    sys.exit()

def start_game():
    global scores, make_jump, jump_counter, user_y, health

    while run_game():
        scores = 0
        make_jump = False
        jump_counter = 30
        user_y = display_height - player_height - 100
        health = 2

def show_menu():
    show = True 
    exit_button = Button(91//1.5, 110//1.5, pygame.image.load('Assets/img/exit.png'), display)
    start_button = Button(374//1.3, 158//1.3, pygame.image.load('Assets/img/start.png'), display)
    nastroiki_button = Button(74//1.5, 74//1.5, pygame.image.load('Assets/img/nastroiki.png'), display)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        display.blit(menu_fon, (0,0))
        start_button.draw(display_width//2 - start_button.width//2, 236, start_game)
        exit_button.draw(display_width - exit_button.width - 10, display_height - exit_button.height - 10, exit_game)
        nastroiki_button.draw(11, 12)
        pygame.display.update()
        clock.tick(5)


def game_over():
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.mixer.music.stop()
        print_text('GAME OVER. Pressed escape to exit or return to continue', 270, display_height // 2)

        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:     
            #stopped = False 
            #return stopped
            show_menu()
        elif keys [pygame.K_RETURN]:
            stopped = True
            return stopped 
        pygame.display.update()
        clock.tick(15)

show_menu()

while run_game():
    pass  
pygame.quit()
sys.exit()



