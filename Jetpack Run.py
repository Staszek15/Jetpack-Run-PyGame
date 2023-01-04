import pygame
import os
import random
import math
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jetpack Run")
BG = pygame.transform.scale(pygame.image.load(os.path.join("Game stuff", "bg.jpg")), (WIDTH, HEIGHT))
TITLE = pygame.transform.scale(pygame.image.load(os.path.join("Game stuff", "Title.png")), (WIDTH // 2 + 100, HEIGHT // 3))
rules = 1
leaderboard = 2
author = 3

### Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
DARK_GREY = (80, 80, 80)
RED = (255, 0, 0)

#Fonts
HP_FONT = pygame.font.SysFont("comicsans", 40)
SCORE_FONT = pygame.font.SysFont("comicsans", 40)
BUTTON_FONT = pygame.font.SysFont("comicsans", 30)
DEFEAT_FONT = pygame.font.SysFont("comicsans", 120)
FONT = pygame.font.SysFont("comicsans", 40)

### Game settings
FPS = 60

### Sound
ZAP_SOUND = pygame.mixer.Sound(os.path.join("Game stuff", "sound.mp3"))
CLICK_SOUND = pygame.mixer.Sound(os.path.join("Game stuff", "click.mp3"))

### Buttons & texts
START_BUTTON = pygame.Rect(0, 300, 220, 40)
RULES_BUTTON = pygame.Rect(0, 360, 220, 40)
LEADERBOARD_BUTTON = pygame.Rect(0, 420, 220, 40)
AUTHOR_BUTTON = pygame.Rect(WIDTH - 200, 300, 220, 40)
EXIT_BUTTON = pygame.Rect(WIDTH - 200, 360, 220, 40)
START_BUTTON_text = BUTTON_FONT.render("Start", 1, BLACK)
RULES_BUTTON_text = BUTTON_FONT.render("Rules", 1, BLACK)
AUTHOR_BUTTON_text = BUTTON_FONT.render("Author", 1, BLACK)
LEADERBOARD_BUTTON_text = BUTTON_FONT.render("Leaderboard", 1, BLACK)
EXIT_BUTTON_text = BUTTON_FONT.render("Exit", 1, BLACK)

TRY_AGAIN_BUTTON = pygame.Rect(WIDTH // 2 - 150 - 50, 300, 150, 70)
MENU_BUTTON = pygame.Rect(WIDTH // 2 + 50, 300, 150, 70)
TRY_AGAIN_text = BUTTON_FONT.render("Try Again", 1, BLACK)
MENU_BUTTON_text = BUTTON_FONT.render("Menu", 1, BLACK)

MENU2_BUTTON = pygame.Rect(20, HEIGHT - 80, 220, 40)
MENU2_BUTTON_text = BUTTON_FONT.render("Menu", 1, BLACK)
RECTANGLE = pygame.Rect(20, 200, WIDTH - 40, 200)

RULES_text1 = FONT.render("Witaj w Laser Run!", 1, BLACK)
RULES_text2 = FONT.render("Używaj klawiszy W, S, A, D, aby unikać laserów.", 1, BLACK)
RULES_text3 = FONT.render("Na starcie gry masz 2 życia.", 1, BLACK)
AUTHOR_text1 = FONT.render("Autor: Mateusz Stasiak", 1, BLACK)
AUTHOR_text2 = FONT.render("Data: 16.04.2021", 1, BLACK)
AUTHOR_text3 = FONT.render("Gra powstała na potrzeby zajęć Politechniki Wrocławskiej.", 1, BLACK)
AUTHOR_text4 = FONT.render("Projekt inspirowany grą Jetpack Joyride produkcji", 1 , BLACK)
AUTHOR_text5 = FONT.render("Halfbrick Studios.", 1 , BLACK)


### Character settings
VEL = 5.0
SIDEVEL = 3
CHARACTER_WIDTH, CHARACTER_HEIGHT = 60, 65

### Character image
CHARACTER_IMAGE = pygame.image.load(os.path.join("Game stuff", "character.png"))
CHARACTER = pygame.transform.scale(CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))


### Laser settings
LASER_VEL = 7
MAX_LASERS = 3
OBSTACLE_WIDTH = 15
OBSTACLE_HEIGHT = random.randint(HEIGHT // 4.5, HEIGHT // 3)



### Laser image
OBSTACLE_IMAGE = pygame.image.load(os.path.join("Game stuff", "laser.png"))
colorkey1 = OBSTACLE_IMAGE.get_at((0,0))
OBSTACLE_IMAGE.set_colorkey(colorkey1, RLEACCEL)
ANGLES = [0, 10, 20, 25, 30, 35, 40, 45, 50, 55, 65, 75, 180, 170, 160, 155, 160, 155, 130, 145, 130, 125, 115, 105]
CHOSEN_ANGLE = random.choice(ANGLES)
OBSTACLE = pygame.transform.rotate(pygame.transform.scale(OBSTACLE_IMAGE, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT)), CHOSEN_ANGLE)



### User events
ZAP = pygame.USEREVENT + 1
POINT = pygame.USEREVENT + 2


def fun(name):
    run = True
    mouse_pos = pygame.mouse.get_pos()
    buttons = [MENU2_BUTTON]
    buttons_names = [MENU2_BUTTON_text]

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos
                if MENU2_BUTTON.collidepoint(click_pos):
                    CLICK_SOUND.play()
                    main_menu()
            

        WIN.blit(BG, (0,0))
        pygame.draw.rect(WIN, GREY, RECTANGLE)
        WIN.blit(TITLE, ((WIDTH - TITLE.get_width()) // 2, 10))
        
        light_buttons(buttons, buttons_names)
        if name == rules:
            WIN.blit(RULES_text1, (RECTANGLE.x + 10, RECTANGLE.y + 20))
            WIN.blit(RULES_text2, (RECTANGLE.x + 10, RECTANGLE.y + FONT.get_height() + 50))
            WIN.blit(RULES_text3, (RECTANGLE.x + 10, RECTANGLE.y + 2*FONT.get_height() + 50))
        elif name == leaderboard:
            pass
        elif name == author:
            WIN.blit(AUTHOR_text1, (RECTANGLE.x + 10, RECTANGLE.y + 20))
            WIN.blit(AUTHOR_text2, (RECTANGLE.x + 10, RECTANGLE.y + FONT.get_height() + 20))
            WIN.blit(AUTHOR_text3, (RECTANGLE.x + 10, RECTANGLE.y + 2*FONT.get_height() + 35))
            WIN.blit(AUTHOR_text4, (RECTANGLE.x + 10, RECTANGLE.y + 3*FONT.get_height() + 50))
            WIN.blit(AUTHOR_text5, (RECTANGLE.x + 10, RECTANGLE.y + 4*FONT.get_height() + 50))

        pygame.display.update()
    
    pygame.quit()


def light_buttons(buttons, buttons_names):
    mouse_pos = pygame.mouse.get_pos()  

    for button, name in zip(buttons, buttons_names):
        if button.collidepoint(mouse_pos):
            color = DARK_GREY
        else:
            color = GREY

        pygame.draw.rect(WIN, color, button)
        WIN.blit(name, (button.x + (button.width - name.get_width()) // 2, 
        button.y + (button.height - name.get_height()) // 2))



def main_menu():
    run = True
    buttons = [START_BUTTON, EXIT_BUTTON, RULES_BUTTON, AUTHOR_BUTTON, LEADERBOARD_BUTTON]
    buttons_names = [START_BUTTON_text, EXIT_BUTTON_text, RULES_BUTTON_text, AUTHOR_BUTTON_text, LEADERBOARD_BUTTON_text]

    while run:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos
                if START_BUTTON.collidepoint(click_pos):
                    CLICK_SOUND.play()
                    main()
                if EXIT_BUTTON.collidepoint(click_pos):
                    CLICK_SOUND.play()
                    quit()
                if RULES_BUTTON.collidepoint(click_pos):
                    CLICK_SOUND.play()
                    fun(rules)
                if LEADERBOARD_BUTTON.collidepoint(click_pos):
                    CLICK_SOUND.play()
                    fun(leaderboard)
                if AUTHOR_BUTTON.collidepoint(click_pos):
                    CLICK_SOUND.play()
                    fun(author)
                

        WIN.blit(BG, (0,0))
        WIN.blit(TITLE, ((WIDTH - TITLE.get_width()) // 2, 10))
        light_buttons(buttons, buttons_names)
        pygame.display.update()
        
    pygame.quit()


def draw_window(player, laser, lasers, HP, SCORE):
    WIN.blit(BG, (0,0))
    HP_text = HP_FONT.render("Healt: " + str(HP), 1, WHITE)
    WIN.blit(HP_text, (10, 10))
    SCORE_text = SCORE_FONT.render("Score: " + str(SCORE), 1, WHITE)
    WIN.blit(SCORE_text, (WIDTH - SCORE_text.get_width() - 10, 10))
    WIN.blit(CHARACTER, (player.x, player.y))
    for laser in lasers:
        
        WIN.blit(OBSTACLE, (laser.x, laser.y))
    pygame.display.update()

def defeat():
    run = True
    buttons = [MENU_BUTTON, TRY_AGAIN_BUTTON]
    buttons_names = [MENU_BUTTON_text, TRY_AGAIN_text]
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos
                if MENU_BUTTON.collidepoint(click_pos):
                    CLICK_SOUND.play()
                    main_menu()
                if TRY_AGAIN_BUTTON.collidepoint(click_pos):
                    CLICK_SOUND.play()
                    main()
                
        defeat_text = DEFEAT_FONT.render("You Lost", 1 , WHITE)
        WIN.blit(defeat_text, (WIDTH // 2 - defeat_text.get_width() // 2, HEIGHT // 2 - defeat_text.get_height() // 2 - 30))
        light_buttons(buttons, buttons_names)

        pygame.display.update()
    
    pygame.quit()
        

def player_movement(keys_pressed, player):
    global VEL
    if keys_pressed[pygame.K_a] and player.x - VEL > 0:
        player.x -= SIDEVEL
    if keys_pressed[pygame.K_d] and player.x + VEL + player.height < WIDTH:
        player.x += SIDEVEL

    
    if player.y + VEL + player.height < HEIGHT:
        if not keys_pressed[pygame.K_w]:
            VEL += 0.3

    if player.y + VEL > 0:
        if keys_pressed[pygame.K_w]:
            VEL -= 0.5
        
    if player.y + VEL + player.height < HEIGHT and player.y + VEL > 0:
        player.y += VEL

def handle_lasers(player, laser, lasers, lasers2):
    #żeby lasery nie wychodziły poza ekran + usuwanie laserow z listy
    for laser in lasers:
        if laser.y + laser.height > HEIGHT:
            laser.y -= HEIGHT - laser.y 

        if laser.y + laser.width < 0:
            laser.y += laser.width

        if laser.bottomright[0] < 0:
            lasers.remove(laser)

        laser.x -= LASER_VEL

        if player.colliderect(laser):
            pygame.event.post(pygame.event.Event(ZAP))
            lasers.remove(laser)
        
    for laser in lasers2:
        if player.x > laser.x:
            pygame.event.post(pygame.event.Event(POINT))
            lasers2.remove(laser)
     

def main():
    player = pygame.Rect(100, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    lasers = []
    lasers2 = []
    
    
    HP = 2
    SCORE = 0
    LASER_FREQUENCY = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        LASER_FREQUENCY = (LASER_FREQUENCY+1) % FPS
        laser = pygame.Rect(WIDTH, random.randint(0, HEIGHT), OBSTACLE_WIDTH, OBSTACLE_HEIGHT)      

        if LASER_FREQUENCY == 0:
            lasers.append(laser)
            lasers2.append(laser)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == ZAP:
                HP -= 1
                draw_window(player, laser, lasers, HP, SCORE)
                ZAP_SOUND.play()

            if event.type == POINT:
                SCORE += 1

        if HP <= 0:
            defeat()
            

        
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player)
        handle_lasers(player, laser, lasers, lasers2)
        draw_window(player, laser, lasers, HP, SCORE)

    pygame.quit()


if __name__ == "__main__":
    main_menu()