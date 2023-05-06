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
    os.path.join('Images', 'BlueStand.png')), (150, 300))
blue_punch = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Blue2.png')), (200, 300))

def draw_window(blue, blue_frame, blue_hp, blue_healthbar):
    blue_anim = [blue_fighter, blue_stand, blue_punch]
    WINDOW.blit(background, (0, 0)) #? background is drawn on window  
    #! health bars 
    pygame.draw.rect(WINDOW, (0,0,0), pygame.Rect(0, 0, 1200, 100)) #? black healthbar background      
    pygame.draw.rect(WINDOW, (255,0,0), pygame.Rect(700, 0 ,700, 100))  
    pygame.draw.rect(WINDOW, (0,150,0), pygame.Rect(700 + blue_healthbar, 0, blue_hp*5, 100))   

    pygame.draw.rect(WINDOW, (0,255,0), pygame.Rect(0, 600, 1200, 100)) 
    WINDOW.blit(blue_anim[blue_frame],(blue.x, blue.y)) #? blit = method to place on screen 
    pygame.display.update()

def main():
    #todo: add damage and attacks 
    blue_hp = 50
    blue_healthbar = (100 - blue_hp)*5
    #! animations 
    last_update = pygame.time.get_ticks()
    blue_animation_cooldown, red_animation_cooldown= 150, 150
    blue_frame = 0 
    blue = pygame.Rect(1050,300, FWIDTH, FHEIGHT)
    frame_rate = pygame.time.Clock()
    run = True 
    while run:
        #! updating animations 
        current_time = pygame.time.get_ticks()
        frame_rate.tick(FPS) #? control speed of while loop / second 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and blue.x + VELOCITY > red.x+150:
            blue.x -= VELOCITY 
            if current_time - last_update >= blue_animation_cooldown:
                blue_frame +=1 
                last_update = current_time
                if blue_frame >= 2:
                    blue_frame = 0 
        if keys_pressed[pygame.K_RIGHT] and blue.x - VELOCITY!= 1050:
            blue.x += VELOCITY
            if current_time - last_update >= blue_animation_cooldown:
                blue_frame +=1 
                last_update = current_time
                if blue_frame >= 2:
                    blue_frame = 0 
            
        if keys_pressed[pygame.K_l]:
            blue_frame = 2
        draw_window(blue, blue_frame, blue_hp, blue_healthbar)
        
        
    pygame.quit() #? if loop breaks then exit the pygame

if __name__== "__main__":
    main()