import pygame 
import os 

#window 
HEIGHT = 500 
WIDTH = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Button Demo')
#load images 
button1 = pygame.image.load('Images/Multi.png').convert_alpha()
button2 = pygame.image.load('Images/Single.png').convert_alpha()
background = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'dojo.jpg')), (WIDTH, HEIGHT))


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
start_button = Button(100,200, button1, False)
exit_button = Button( 450, 200, button2, False)
#game loop 
run = True 
while run:
    screen.blit(background, (0, 0))
    if start_button.draw():
        print('start')
        #or run the function 
    if exit_button.draw():
        print('exit')
        run = False 
    start_button.draw()
    exit_button.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    pygame.display.update()

pygame.quit 
