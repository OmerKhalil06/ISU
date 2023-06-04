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
background = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'Cat.test.jpg')), (WIDTH, HEIGHT))
blue_fighter = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Blue1.png')), (150, 300))
blue_stand = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'BlueStand.png')), (150, 300))
red_fighter = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'Red1.png')), (150,300)), True, False)



def draw_window(blue, red): #? draw window to create images 
    WINDOW.blit(background, (0, 0)) #? background is drawn on window 
    #WINDOW.fill((255,255,255))  #todo: add real background later  
    pygame.draw.rect(WINDOW, (0,255,0), pygame.Rect(0, 600, 1200, 100)) 
    WINDOW.blit(blue_fighter,(blue.x, blue.y))
    WINDOW.blit(red_fighter, (red.x, red.y)) #? blit = method to place on screen 
    pygame.display.update()
    
def main():
    blue = pygame.Rect(1050,300, FWIDTH, FHEIGHT)
    red = pygame.Rect(0,300, FWIDTH, FHEIGHT)
    frame_rate = pygame.time.Clock()
    MIDDLE = ((red.x +blue.x)//2)
    run = True 
    while run:
        
        frame_rate.tick(FPS) #? control speed of while loop / second 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and blue.x + VELOCITY > red.x+100:
            blue.x -= VELOCITY 
            #todo: add animations to a list and cycle through them in a while loop 
        if keys_pressed[pygame.K_RIGHT] and blue.x - VELOCITY!= 1050:
            blue.x += VELOCITY
        if keys_pressed[pygame.K_d] and red.x + VELOCITY < blue.x - 100:
            red.x += VELOCITY 
        if keys_pressed[pygame.K_a] and red.x !=0:
            red.x -= VELOCITY 

        draw_window(blue, red)
        
        
    pygame.quit() #? if loop breaks then exit the pygame
if __name__== "__main__":
    main()