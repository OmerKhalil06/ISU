# Omer Khalil
# 2023-04-29
# begin the basics of the game

import pygame #? import the pygame library 
import os

pygame.display.set_caption('Py-ting Game')

#! global varibles 
FPS = 30
WIDTH , HEIGHT = 1200, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
VELOCITY = 10
FWIDTH, FHEIGHT = 150, 300 

BLUE_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#! images defined 
background = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'castle.png')), (WIDTH, HEIGHT))

blue_fighter = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Blue1.png')), (150, 300))
blue_stand = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Blue2.png')), (150, 300))
blue_punch = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Blue3.png')), (210, 300))

red_fighter = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Red1.png')), (150,300)), True, False)
red_punch = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Red2.png')), (210,300)), True, False)
red_back = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Red5.png')), (170,300)), True, False)
#! function for all drawings 
def draw_window(blue, red, blue_frame, red_frame, blue_hp,red_hp, blue_healthbar, blue_able, red_able): #? draw window to create images 
    blue_anim = [blue_fighter, blue_stand, blue_punch]
    red_anim = [red_fighter, red_back, red_punch]
    WINDOW.blit(background, (0, 100)) #? background is drawn on window  
    #HP bars 
    pygame.draw.rect(WINDOW, (0,0,0), pygame.Rect(0, 0, 1200, 100)) #? black healthbar background 

    pygame.draw.rect(WINDOW, (255,0,0), pygame.Rect(0,0,500, 100))  #! red rectangle for red HP 
    pygame.draw.rect(WINDOW, (0,150,0), pygame.Rect(0,0,red_hp*5, 100))  #! green rectangle for red HP

    pygame.draw.rect(WINDOW, (255,0,0), pygame.Rect(700, 0 ,700, 100))  #? red rectangle for blue 
    pygame.draw.rect(WINDOW, (0,150,0), pygame.Rect(700 + blue_healthbar, 0, blue_hp*5, 100))   #? green rectangke for blue

    pygame.draw.rect(WINDOW, (110,0,0), pygame.Rect(0, 600, 1200, 100)) #! floor 

    WINDOW.blit((blue_anim[blue_frame]),(blue.x, blue.y))
    WINDOW.blit((red_anim[red_frame]), (red.x, red.y)) #? blit = method to place on screen 

    pygame.display.update()

def handle_hits(blue, red, blue_able, red_able):
    if blue_able == False:
        attack2 = pygame.draw.rect(WINDOW, (0,0,225), pygame.Rect(blue.x - 50, blue.y, 50, 300))
        if attack2.colliderect(red):
            pygame.event.post(pygame.event.Event(RED_HIT))

    if red_able == False:
        attack1 = pygame.draw.rect(WINDOW, (255,0,0), pygame.Rect(red.x+200, red.y, 50, 300))
        if attack1.colliderect(blue):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            
#! Main function    
def main():
    #todo: add damage and attacks 
    blue_hp = 100
    red_hp = 100
    blue_healthbar = (100 - blue_hp)*5

    blue = pygame.Rect(1050,300, FWIDTH, FHEIGHT)
    red = pygame.Rect(0,300, FWIDTH, FHEIGHT)
    #! animations 
    last_update = pygame.time.get_ticks()
    blue_animation_cooldown, red_animation_cooldown= 150, 150
    blue_frame = 0 
    red_frame = 0
    
    frame_rate = pygame.time.Clock()
  
    run = True 
    #! Cooldown 
    blue_able = True 
    red_able = True 
    blue_cd = pygame.time.get_ticks()
    red_cd = pygame.time.get_ticks()
    blue_last_attack = pygame.time.get_ticks()
    red_last_attack = pygame.time.get_ticks()


    while run:
        #! updating animations 
        blue_cd2 = pygame.time.get_ticks()
        red_cd2 = pygame.time.get_ticks()
        blue_last_attack2 = pygame.time.get_ticks()
        red_last_attack2 = pygame.time.get_ticks()

        current_time = pygame.time.get_ticks()

        frame_rate.tick(FPS) #? control speed of while loop / second 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        # cooldowns 
        if blue_cd2 - blue_cd >= 100:
            blue_able = True 
            blue_cd = blue_cd2 
            blue_frame = 0 
        
        if red_cd2 - red_cd >=100:
            red_able = True 
            red_cd = red_cd2
            red_frame = 0 

        if keys_pressed[pygame.K_l] and blue_able == True and blue_last_attack2 - blue_last_attack >= 1000: #todo add a feature that adds CD to if pressed early and stun if hit 
            blue_cd2 = pygame.time.get_ticks()
            blue_frame = 2 
            blue_able = False 
            blue_last_attack = blue_last_attack2

        if keys_pressed[pygame.K_e] and red_able == True and red_last_attack2 - red_last_attack>=1000:
            red_cd2 = pygame.time.get_ticks()
            red_frame = 2 
            red_able = False 
            red_last_attack = red_last_attack2

        if keys_pressed[pygame.K_LEFT] and blue.x + VELOCITY > red.x+150 and blue_able == True:
            blue.x -= VELOCITY
            if current_time - last_update >= blue_animation_cooldown:
                blue_frame +=1 
                last_update = current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_RIGHT] and blue.x - VELOCITY!= 1050 and blue_able == True:
            blue.x += VELOCITY
            if current_time - last_update >= blue_animation_cooldown:
                blue_frame +=1 
                last_update = current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_d] and red.x + VELOCITY < blue.x - 150 and red_able == True:
            red.x += VELOCITY 
            if current_time - last_update >= red_animation_cooldown:
                red_frame +=1 
                last_update = current_time
                if red_frame >= 2:
                    red_frame = 0 

        if keys_pressed[pygame.K_a] and red.x !=0 and red_able == True:
            red.x -= VELOCITY 
            if current_time - last_update >= red_animation_cooldown:
                red_frame +=1 
                last_update = current_time
                if red_frame >= 2:
                  red_frame = 0    

        if event.type == RED_HIT:
            red_hp -= 10
     
        if event.type == BLUE_HIT:
            blue_hp -= 10
        
    
        handle_hits(blue, red, blue_able, red_able)
        draw_window(blue, red, blue_frame, red_frame, blue_hp, red_hp, blue_healthbar, blue_able, red_able)
        
        
    pygame.quit() #? if loop breaks then exit the pygame
if __name__== "__main__":
    main()