# Omer Khalil
# 2023-04-29
# begin the basics of the game

import pygame #? import the pygame library 
import os

pygame.display.set_caption('Py-fighter')

#? global varibles 
FPS = 30
WIDTH , HEIGHT = 1200, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
VELOCITY = 10
FWIDTH, FHEIGHT = 150, 300 

#? images defined 
background = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'castle.png')), (WIDTH, HEIGHT))

blue_fighter = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Blue1.png')), (150, 300))
blue_stand = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Blue2.png')), (150, 300))
blue_punch = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Blue3.png')), (210, 300))

red_fighter = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Red1.png')), (150,300)), True, False)
red_stand = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Red3.png')), (150,300)), True, False)
red_back = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Red5.png')), (170, 300)), True, False)

def draw_window(blue, red, blue_frame, red_frame, blue_hp,red_hp, blue_healthbar, able): #? draw window to create images 
    blue_anim = [blue_fighter, blue_stand, blue_punch]
    red_anim = [red_fighter, red_back]
    WINDOW.blit(background, (0, 100)) #? background is drawn on window  
    #! health bars 
    pygame.draw.rect(WINDOW, (0,0,0), pygame.Rect(0, 0, 1200, 100)) #? black healthbar background    
    pygame.draw.rect(WINDOW, (255,0,0), pygame.Rect(0,0,500, 100)) 
    pygame.draw.rect(WINDOW, (0,150,0), pygame.Rect(0,0,red_hp*5, 100))   
    pygame.draw.rect(WINDOW, (255,0,0), pygame.Rect(700, 0 ,700, 100))  
    pygame.draw.rect(WINDOW, (0,150,0), pygame.Rect(700 + blue_healthbar, 0, blue_hp*5, 100))   

    pygame.draw.rect(WINDOW, (110,0,0), pygame.Rect(0, 600, 1200, 100)) 
    WINDOW.blit(blue_anim[blue_frame],(blue.x, blue.y))
    WINDOW.blit(red_anim[red_frame], (red.x, red.y)) #? blit = method to place on screen 
    if able == False:
            pygame.draw.rect(WINDOW, (0,0,255), pygame.Rect(blue.x - 100, blue.y, 100, 200))
    pygame.display.update()
    
def main():
    #todo: add damage and attacks 
    blue_hp = 100
    red_hp = 100
    blue_healthbar = (100 - blue_hp)*5
    #! animations 
    last_update = pygame.time.get_ticks()
    blue_animation_cooldown, red_animation_cooldown= 150, 150
    blue_frame = 0 
    red_frame = 0
    blue = pygame.Rect(1050,300, FWIDTH, FHEIGHT)
    red = pygame.Rect(0,300, FWIDTH, FHEIGHT)
    frame_rate = pygame.time.Clock()
    run = True 

    able = True 
    cd = pygame.time.get_ticks()
    while run:
        #! updating animations 
        cd2 = pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()
        frame_rate.tick(FPS) #? control speed of while loop / second 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_l]:
            cd2 = pygame.time.get_ticks()
            blue_frame = 2 
            able = False 
            
        if cd2 - cd >= 1000:
            able = True 
            cd = cd2 
            blue_frame = 0
        if keys_pressed[pygame.K_LEFT] and blue.x + VELOCITY > red.x+150 and able == True:
            blue.x -= VELOCITY 
            if current_time - last_update >= blue_animation_cooldown:
                blue_frame +=1 
                last_update = current_time
                if blue_frame >= 2:
                    blue_frame = 0 
 
        if keys_pressed[pygame.K_RIGHT] and blue.x - VELOCITY!= 1050 and able ==True:
            blue.x += VELOCITY
            if current_time - last_update >= blue_animation_cooldown:
                blue_frame +=1 
                last_update = current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_d] and red.x + VELOCITY < blue.x - 150:
            red.x += VELOCITY 
            if current_time - last_update >= red_animation_cooldown:
                red_frame +=1 
                last_update = current_time
                if red_frame >= 2:
                    red_frame = 0 

        if keys_pressed[pygame.K_a] and red.x !=0:
            red.x -= VELOCITY 
            if current_time - last_update >= red_animation_cooldown:
                red_frame +=1 
                last_update = current_time
                if red_frame >= 2:
                    red_frame = 0

        draw_window(blue, red, blue_frame, red_frame, blue_hp, red_hp, blue_healthbar, able)
        
        
    pygame.quit() #? if loop breaks then exit the pygame
if __name__== "__main__":
    main()