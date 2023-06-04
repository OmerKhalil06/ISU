# Omer Khalil
# 2023-04-29
# Main Game File

import pygame #? import the pygame library 
import os
pygame.font.init() #initialize fonts 
pygame.mixer.init() #initialize sounds 

pygame.display.set_caption('Py-ting Game')

#! global varibles 
FPS = 60
WIDTH , HEIGHT = 1200, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
VELOCITY = 10
FWIDTH, FHEIGHT = 150, 300 

WINNER_FONT = pygame.font.SysFont('VT323', 100)



#* Images  
background = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'dojo.jpg')), (WIDTH, HEIGHT))

floor = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'floor.png')), (100,100))
logo = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'logo.png')), (70,100))

blue_fighter = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'blue1.png')), (220, 300))
blue_stand = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'blue2.png')), (220, 300))
blue_punch = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'blue3.png')), (220, 300))
blue_punch = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'blue4.png')), (220, 300))

red_fighter = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'red1.png')), (220,300)), True, False)
red_back = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'red2.png')), (220,300)), True, False)
red_punch = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'red3.png')), (220,300)), True, False)
red_punch2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'red4.png')), (220,300)), True, False)


#* sounds

punch_sound = pygame.mixer.Sound(os.path.join('Sounds', 'Punch.mp3'))


#! function for all drawings 
def draw_window(blue, red, blue_frame, red_frame, blue_hp,red_hp, blue_healthbar): #? draw window to create images 
    blue_anim = [blue_fighter, blue_stand, blue_punch]
    red_anim = [red_fighter, red_back, red_punch]
    WINDOW.blit(background, (0, 0)) #? background is drawn on window  
    
    #HP bars 
    pygame.draw.rect(WINDOW, (0,255,0), pygame.Rect(0,0,500, 100))  #! red rectangle for red HP 
    pygame.draw.rect(WINDOW, (255,0,0), pygame.Rect(0,0,(100-red_hp)*5, 100))  #! green rectangle for red HP
    
    pygame.draw.rect(WINDOW, (0,0,0), pygame.Rect(500, 0, 200, 100)) #? black healthbar background 

    pygame.draw.rect(WINDOW, (255,0,0), pygame.Rect(700, 0 ,700, 100))  #? red rectangle for blue 
    pygame.draw.rect(WINDOW, (0,255,0), pygame.Rect(700 + blue_healthbar, 0, blue_hp*5, 100))   #? green rectangke for blue

    pygame.draw.rect(WINDOW, (0,0,0), pygame.Rect(0, 0, 1200, 20))
    pygame.draw.rect(WINDOW, (0,0,0), pygame.Rect(0, 80, 1200, 20))
    
    WINDOW.blit(logo, (560, 0))
    
    WINDOW.blit(blue_anim[blue_frame],(blue.x, blue.y))
    WINDOW.blit((red_anim[red_frame]), (red.x, red.y)) #? blit = method to place on screen 
    
    pygame.display.update()
    
def draw_winner(text, text_colour):   
    draw_text = WINNER_FONT.render(text, 1, text_colour ) 
    pygame.draw.rect(WINDOW, (200, 200,250),  pygame.Rect(400, 300 , 405, 100))
    WINDOW.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2)) 
    pygame.display.update()
    pygame.time.delay(1000)
    #! call main menu 
        
#! Main function    
def main():
    #todo: add damage and attacks 
    blue_hp = 100
    red_hp = 100
    blue_healthbar = (100 - blue_hp)*5

    blue = pygame.Rect(980,300, FWIDTH, FHEIGHT)
    red = pygame.Rect(0,300, FWIDTH, FHEIGHT)
    #! animations 
    blue_last_update = pygame.time.get_ticks()
    red_last_update = pygame.time.get_ticks()
    blue_animation_cooldown, red_animation_cooldown= 150, 150
    blue_frame = 0 
    red_frame = 0
    
    frame_rate = pygame.time.Clock()
  
    run = True 
    #! Cooldown 
    blue_cd = pygame.time.get_ticks()
    red_cd = pygame.time.get_ticks()

    red_stun = True 
    blue_stun = True

    blue_ko = False 
    red_ko = False 
    

    red_stun_cd = pygame.time.get_ticks() 
    blue_stun_cd = pygame.time.get_ticks()



    while run:
        #! updating animations 
        blue_cd2 = pygame.time.get_ticks()
        red_cd2 = pygame.time.get_ticks()

        red_stun_cd2 = pygame.time.get_ticks()
        blue_stun_cd2 = pygame.time.get_ticks()

        blue_current_time = pygame.time.get_ticks()
        red_current_time = pygame.time.get_ticks()
        frame_rate.tick(FPS) #? control speed of while loop / second 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
       
        keys_pressed = pygame.key.get_pressed()

        # cooldowns 

        if red_stun == False:
            if red_stun_cd2 - red_stun_cd >= 1000:
                red_stun = True
                red_stun_cd = red_stun_cd2
                
        
        if blue_stun == False:
            if blue_stun_cd2 - blue_stun_cd >= 1000:
                blue_stun = True
                blue_stun_cd = blue_stun_cd2

        if blue_cd2 - blue_cd >= 400:
            blue_able = True 
            blue_cd = blue_cd2 
            blue_frame = 0
        
        if red_cd2 - red_cd >=400:
            red_able = True 
            red_cd = red_cd2
            red_frame = 0

        if blue.x >=  980:
            blue.x = 980

        if red.x <= 0:
            red.x =0 
        if keys_pressed[pygame.K_l] and blue_stun == True and red_ko == False: #todo add a feature that adds CD to if pressed early and stun if hit 
            blue_stun = False
            blue_cd2 = pygame.time.get_ticks()
            blue_frame = 2 
            blue_attack = pygame.draw.rect(WINDOW, (0,0,225), pygame.Rect(blue.x - 20, blue.y, 10, 300))
            if blue_attack.colliderect(red):
                punch_sound.play()
                red_hp -= 10
                red_cd2 = 0
                red_able == False
                blue_attack.y+=500
                red.x-=60


        if blue.x <= red.x + 220 and red_stun == True and blue_ko == False:
            red_stun = False 
            red_cd2 = pygame.time.get_ticks()
            red_frame = 2
            red_attack = pygame.draw.rect(WINDOW, (255,0,0), pygame.Rect(red.x + 220, red.y, 10, 300))
            if  red_attack.colliderect(blue):
                punch_sound.play()
                blue_hp -=10
                blue.x+= 60
                blue_cd2 = 0
                blue_stun == False 
                red_attack.y += 500
            
        if keys_pressed[pygame.K_LEFT] and blue.x + VELOCITY >= red.x + 115 and blue_stun == True and red_ko == False:
            blue.x -= VELOCITY
            if blue_current_time - blue_last_update >= blue_animation_cooldown:
                blue_frame +=1 
                blue_last_update = blue_current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_RIGHT] and blue.x - VELOCITY!= 980 and blue_able == True and red_ko == False:
            blue.x += VELOCITY
            if blue_current_time - blue_last_update >= blue_animation_cooldown:
                blue_frame +=1 
                blue_last_update = blue_current_time
                if blue_frame >= 2:
                    blue_frame = 0 


        if red.x <= blue.x - 20 and red.x + VELOCITY < blue.x - 90 and red.x-VELOCITY<= 1080 and red_stun == True and blue_ko == False:
            red.x += VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2: 
                    red_frame = 0 

        
        winner_text =  '' 

        if blue_hp <=0:
            winner_text = 'RED WINS '
            blue_ko = True
            text_colour = (150,0,0)
        
        if red_hp <= 0:
            winner_text = 'BLUE WINS'
            text_colour = (0,0,150)

        draw_window(blue, red, blue_frame, red_frame, blue_hp, red_hp, blue_healthbar)

        if winner_text != '':
            draw_winner(winner_text, text_colour)

    pygame.quit() #? if loop breaks then exit the pygame
if __name__== "__main__":
    main()
