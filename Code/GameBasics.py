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

#? images defined 
background = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'cat.test.jpg')), (WIDTH, HEIGHT))
blue_fighter = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'Blue1.png')), (100, 200))
red_fighter = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'Red1.png')), (100,200))

def draw_window(): #? draw window to create images 
    WINDOW.blit(background, (0,0)) #? background is drawn on window 
    pygame.draw.rect(WINDOW, (255,255,255), pygame.Rect(0, 600, 1200, 100)) 
    WINDOW.blit(blue_fighter,(1000, 400))
    WINDOW.blit(red_fighter, (1000,400)) #? blit = method to place on screen 
    
    
    pygame.display.update()
    
def main():
    frame_rate = pygame.time.Clock()
    run = True 
    while run:
        frame_rate.tick(FPS) #? control speed of while loop / second 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
        draw_window()
        
        
    pygame.quit() #? if loop breaks then exit the pygame
if __name__== "__main__":
    main()