# Omer Khalil
# 2023-04-29
# Main Game File
# todo: add way to exit out of main menu
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
APPLE_VEL = 20

WINNER_FONT = pygame.font.SysFont('VT323', 100)

#* Images  
background = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'final_battle.jpg')), (WIDTH, HEIGHT))

floor = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'floor.png')), (100,100))
logo = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'logo.png')), (70,100))

blue_fighter = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'blue1.png')), (220, 300))
blue_stand = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'blue2.png')), (220, 300))
blue_punch = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'blue3.png')), (220, 300))
blue_punch2 = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'blue4.png')), (220, 300))
blue_kick = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'blue5.png')), (300, 300))

red_fighter = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'red1.png')), (220,300)), True, False)
red_back = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'red2.png')), (220,300)), True, False)
red_punch = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'red3.png')), (220,300)), True, False)
red_punch2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'red4.png')), (220,300)), True, False)
red_kick = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'red5.png')), (220,300)), True, False)


#* sounds

punch_sound = pygame.mixer.Sound(os.path.join('Sounds', 'Punch.mp3'))


#! function for all drawings 
def draw_window(blue, red, blue_frame, red_frame, blue_hp,red_hp, blue_healthbar): #? draw window to create images 
    blue_anim = [blue_fighter, blue_stand, blue_punch, blue_punch2, blue_kick]
    red_anim = [red_fighter, red_back, red_punch, red_punch2, red_kick]
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
            if red_stun_cd2 - red_stun_cd >= 500:
                red_stun = True
                red_stun_cd = red_stun_cd2
                
        
        if blue_stun == False:
            if blue_stun_cd2 - blue_stun_cd >= 500:
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

        if blue.x >= 980:
            blue.x = 980

        if red.x <= 0:
            red.x = 0 

        if keys_pressed[pygame.K_l] and blue_stun == True and blue_able == True: #todo add a feature that adds CD to if pressed early and stun if hit 
            blue_stun = False
            blue_able = True 
            blue_cd2 = pygame.time.get_ticks()
            blue_frame = 2 
            blue_attack = pygame.Rect(blue.x - 20, blue.y, 10, 300)
            if blue_attack.colliderect(red):
                punch_sound.play()
                red_hp -= 5
                red_cd2 = 0
                red_stun == False
                blue_attack.y+=500
                red.x-=60

        if keys_pressed[pygame.K_SPACE] and blue_stun == True: #todo add a feature that adds CD to if pressed early and stun if hit 
            blue_stun = False
            blue_able = True 
            blue_cd2 = pygame.time.get_ticks()
            blue_frame = 4
            if blue.x - 120 > red.x +90:
                blue.x -= 10
            blue_attack = pygame.Rect(blue.x - 100, blue.y, 10, 300)
            if blue_attack.colliderect(red):
                punch_sound.play()
                red_hp -= 50
                red_cd2 = 0
                red_stun == False
                blue_attack.y+=500
                red.x-=1200 

        if keys_pressed[pygame.K_e]and red_stun == True:
            red_stun = False 
            red_cd2 = pygame.time.get_ticks()
            red_frame = 2
            red_attack = pygame.Rect(red.x + 170, red.y, 10, 300)
            if  red_attack.colliderect(blue):
                punch_sound.play()
                blue_hp -=5
                blue.x+= 60
                blue_cd2 = 0
                blue_stun == False 
                red_attack.y += 500
            
        if keys_pressed[pygame.K_LEFT] and blue.x + VELOCITY >= red.x + 115 and blue_stun == True:
            blue.x -= VELOCITY
            if blue_current_time - blue_last_update >= blue_animation_cooldown:
                blue_frame +=1 
                blue_last_update = blue_current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_RIGHT] and blue.x - VELOCITY!= 980 and blue_stun == True:
            blue.x += VELOCITY
            if blue_current_time - blue_last_update >= blue_animation_cooldown:
                blue_frame +=1 
                blue_last_update = blue_current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_d] and red.x + VELOCITY < blue.x - 90 and red.x-VELOCITY<= 1080 and red_stun == True:
            red.x += VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2: 
                    red_frame = 0 

        if keys_pressed[pygame.K_a] and red.x !=0 and red_stun == True:
            red.x -= VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2:
                  red_frame = 0  
        
        winner_text =  '' 

        if blue_hp <=0:
            winner_text = 'RED WINS '
            text_colour = (150,0,0)
        
        if red_hp <= 0:
            winner_text = 'BLUE WINS'
            text_colour = (0,0,150)

        draw_window(blue, red, blue_frame, red_frame, blue_hp, red_hp, blue_healthbar)

        if winner_text != '': 
            draw_winner(winner_text, text_colour)
            pygame.time.delay(3000)
            run = False
            menu()


    pygame.quit() #? if loop breaks then exit the pygame

def unbeatable_ai():
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
            if red_stun_cd2 - red_stun_cd >= 500:
                red_stun = True
                red_stun_cd = red_stun_cd2
                
        
        if blue_stun == False:
            if blue_stun_cd2 - blue_stun_cd >= 500:
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

        if blue.x >= 980:
            blue.x = 980

        if red.x <= 0:
            red.x = 0

        if keys_pressed[pygame.K_l] and blue_stun == True and blue_able == True: #todo add a feature that adds CD to if pressed early and stun if hit 
            blue_stun = False
            blue_able = True 
            blue_cd2 = pygame.time.get_ticks()
            blue_frame = 2 
            blue_attack = pygame.Rect(blue.x - 20, blue.y, 10, 300)
            if blue_attack.colliderect(red):
                punch_sound.play()
                red_hp -= 10
                red_cd2 = 0
                red_stun == False
                blue_attack.y+=500
                red.x-=60


        if blue.x <= red.x + 170 and red_stun == True:
            red_stun = False 
            red_cd2 = pygame.time.get_ticks()
            red_frame = 2
            red_attack = pygame.Rect(red.x + 165, red.y, 10, 300)
            if red_attack.colliderect(blue):
                punch_sound.play()
                blue_hp -=10
                blue.x+= 60
                blue_cd2 = 0
                blue_stun == False 
                red_attack.y += 500


        if red.x <= blue.x - 20 and red.x + VELOCITY < blue.x - 90 and red.x-VELOCITY<= 1080 and red_stun == True:
            red.x += VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2: 
                    red_frame = 0
            
        if keys_pressed[pygame.K_LEFT] and blue.x + VELOCITY >= red.x + 115 and blue_stun == True:
            blue.x -= VELOCITY
            if blue_current_time - blue_last_update >= blue_animation_cooldown:
                blue_frame +=1 
                blue_last_update = blue_current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_RIGHT] and blue.x - VELOCITY!= 980 and blue_stun == True:
            blue.x += VELOCITY
            if blue_current_time - blue_last_update >= blue_animation_cooldown:
                blue_frame +=1 
                blue_last_update = blue_current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_d] and red.x + VELOCITY < blue.x - 90 and red.x-VELOCITY<= 1080 and red_stun == True:
            red.x += VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2: 
                    red_frame = 0 

        if keys_pressed[pygame.K_a] and red.x !=0 and red_stun == True:
            red.x -= VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2:
                  red_frame = 0  
        
        winner_text =  '' 

        if blue_hp <=0:
            winner_text = 'RED WINS '
            text_colour = (150,0,0)
        
        if red_hp <= 0:
            winner_text = 'BLUE WINS'
            text_colour = (0,0,150)

        draw_window(blue, red, blue_frame, red_frame, blue_hp, red_hp, blue_healthbar)

        if winner_text != '': 
            draw_winner(winner_text, text_colour)
            pygame.time.delay(3000)
            run = False
            menu()


    pygame.quit() #? if loop breaks then exit the pygame
def med_ai():
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
            if red_stun_cd2 - red_stun_cd >= 500:
                red_stun = True
                red_stun_cd = red_stun_cd2
                
        
        if blue_stun == False:
            if blue_stun_cd2 - blue_stun_cd >= 500:
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

        if blue.x >= 980:
            blue.x = 980

        if red.x <= 0:
            red.x = 0

        if keys_pressed[pygame.K_l] and blue_stun == True and blue_able == True: #todo add a feature that adds CD to if pressed early and stun if hit 
            blue_stun = False
            blue_able = True 
            blue_cd2 = pygame.time.get_ticks()
            blue_frame = 2 
            blue_attack = pygame.Rect(blue.x - 20, blue.y, 10, 300)
            if blue_attack.colliderect(red):
                punch_sound.play()
                red_hp -= 10
                red_cd2 = 0
                red_stun == False
                blue_attack.y+=500
                red.x-=60


        if blue.x <= red.x + 170 and red_stun == True:
            red_stun = False 
            red_cd2 = pygame.time.get_ticks()
            red_frame = 2
            red_attack = pygame.Rect(red.x + 160, red.y, 10, 300)
            if red_attack.colliderect(blue):
                punch_sound.play()
                blue_hp -=10
                blue.x+= 60
                blue_cd2 = 0
                blue_stun == False 
                red_attack.y += 500


        if red.x <= blue.x - 20 and red.x + VELOCITY < blue.x - 90 and red.x-VELOCITY<= 1080 and red_stun == True:
            red.x += VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2: 
                    red_frame = 0
            
        if keys_pressed[pygame.K_LEFT] and blue.x + VELOCITY >= red.x + 115 and blue_stun == True:
            blue.x -= VELOCITY
            if blue_current_time - blue_last_update >= blue_animation_cooldown:
                blue_frame +=1 
                blue_last_update = blue_current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_RIGHT] and blue.x - VELOCITY!= 980 and blue_stun == True:
            blue.x += VELOCITY
            if blue_current_time - blue_last_update >= blue_animation_cooldown:
                blue_frame +=1 
                blue_last_update = blue_current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_d] and red.x + VELOCITY < blue.x - 90 and red.x-VELOCITY<= 1080 and red_stun == True:
            red.x += VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2: 
                    red_frame = 0 

        if keys_pressed[pygame.K_a] and red.x !=0 and red_stun == True:
            red.x -= VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2:
                  red_frame = 0  
        
        winner_text =  '' 

        if blue_hp <=0:
            winner_text = 'RED WINS '
            text_colour = (150,0,0)
        
        if red_hp <= 0:
            winner_text = 'BLUE WINS'
            text_colour = (0,0,150)

        draw_window(blue, red, blue_frame, red_frame, blue_hp, red_hp, blue_healthbar)

        if winner_text != '': 
            draw_winner(winner_text, text_colour)
            pygame.time.delay(3000)
            run = False
            menu()
        
    pygame.quit() #? if loop breaks then exit the pygame

def easy_ai():
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
            if red_stun_cd2 - red_stun_cd >= 500:
                red_stun = True
                red_stun_cd = red_stun_cd2
                
        
        if blue_stun == False:
            if blue_stun_cd2 - blue_stun_cd >= 500:
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

        if blue.x >= 980:
            blue.x = 980

        if red.x <= 0:
            red.x = 0

        if keys_pressed[pygame.K_l] and blue_stun == True and blue_able == True: #todo add a feature that adds CD to if pressed early and stun if hit 
            blue_stun = False
            blue_able = True 
            blue_cd2 = pygame.time.get_ticks()
            blue_frame = 2 
            blue_attack = pygame.Rect(blue.x - 20, blue.y, 10, 300)
            if blue_attack.colliderect(red):
                punch_sound.play()
                red_hp -= 10
                red_cd2 = 0
                red_stun == False
                blue_attack.y+=500
                red.x-=60


        if blue.x <= red.x + 170 and red_stun == True:
            red_stun = False 
            red_cd2 = pygame.time.get_ticks()
            red_frame = 2
            red_attack = pygame.Rect(red.x + 140, red.y, 10, 300)
            if red_attack.colliderect(blue):
                punch_sound.play()
                blue_hp -=10
                blue.x+= 60
                blue_cd2 = 0
                blue_stun == False 
                red_attack.y += 500


        if red.x <= blue.x - 20 and red.x + VELOCITY < blue.x - 90 and red.x-VELOCITY<= 1080 and red_stun == True:
            red.x += VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2: 
                    red_frame = 0
            
        if keys_pressed[pygame.K_LEFT] and blue.x + VELOCITY >= red.x + 115 and blue_stun == True:
            blue.x -= VELOCITY
            if blue_current_time - blue_last_update >= blue_animation_cooldown:
                blue_frame +=1 
                blue_last_update = blue_current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_RIGHT] and blue.x - VELOCITY!= 980 and blue_stun == True:
            blue.x += VELOCITY
            if blue_current_time - blue_last_update >= blue_animation_cooldown:
                blue_frame +=1 
                blue_last_update = blue_current_time
                if blue_frame >= 2:
                    blue_frame = 0 

        if keys_pressed[pygame.K_d] and red.x + VELOCITY < blue.x - 90 and red.x-VELOCITY<= 1080 and red_stun == True:
            red.x += VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2: 
                    red_frame = 0 

        if keys_pressed[pygame.K_a] and red.x !=0 and red_stun == True:
            red.x -= VELOCITY 
            if red_current_time - red_last_update >= red_animation_cooldown:
                red_frame +=1 
                red_last_update = red_current_time
                if red_frame >= 2:
                  red_frame = 0  
        
        winner_text =  '' 

        if blue_hp <=0:
            winner_text = 'RED WINS '
            text_colour = (150,0,0)
        
        if red_hp <= 0:
            winner_text = 'BLUE WINS'
            text_colour = (0,0,150)

        draw_window(blue, red, blue_frame, red_frame, blue_hp, red_hp, blue_healthbar)

        if winner_text != '': 
            draw_winner(winner_text, text_colour)
            pygame.time.delay(3000)
            run = False
            ()
        
    pygame.quit() #? if loop breaks then exit the pygame
#! main menu 
#window 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Button Demo')
#load images 
multi = pygame.image.load('Images/Multi.png').convert_alpha()
single = pygame.image.load('Images/Single.png').convert_alpha()
exit = pygame.image.load('Images/EXIT.png').convert_alpha()
start = pygame.image.load('Images/Start.png').convert_alpha()
setting = pygame.image.load('Images/Settings.png').convert_alpha()
#button class 
class Button():
    def __init__(self, x, y, image, clicked):
        self.image = pygame.transform.scale(image, (300, 80)) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False 
 

    def draw(self):
        action =  False 
        #get mouse position 
        pos = pygame.mouse.get_pos()

        #check mouse over button and clicked 
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True 
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False 

                       
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action  

def ply_menu():
    multiplayer_button = Button(100 ,100, multi, False)
    singleplayer_button = Button(200 , 400, single, False)
    exit_button = Button (400, 200, exit, False)
    #game loop 
    run = True 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(background, (0, 0))
        if multiplayer_button.draw():
            main()
        if singleplayer_button.draw():
            unbeatable_ai()  
        if exit_button.draw():
            run = False 
        multiplayer_button.draw()
        singleplayer_button.draw()        
        exit_button.draw()


        pygame.display.update()

    pygame.quit 

def main_menu(): 
    start_button = Button(600 ,400, start, False)
    setting_button = Button(200 , 400, setting, False)
    exit_button = Button (400, 200, exit, False)
    #game loop 
    run = True 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(background, (0, 0))
        logo = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'logo.png')), (210,300))
        #screen.blit(logo, (495, 0))
        pygame.draw.rect(WINDOW, (255,218,100), pygame.Rect(300, 0, 600, 600))


        if start_button.draw():
            ply_menu()
        if setting_button.draw():
            run = False   
        if exit_button.draw():
            run = False 
        setting_button.draw()
        start_button.draw()        
        exit_button.draw()


        pygame.display.update()


main_menu()