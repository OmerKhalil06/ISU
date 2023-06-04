import pygame 
#window 
HEIGHT = 500 
WIDTH = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Button Demo')
#load images 
blue_fighter = pygame.image.load('Images/blue1.png').convert_alpha()
red_fighter = pygame.image.load('Images/red1.png').convert_alpha()

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
start_button = Button(100,200, blue_fighter, False)
exit_button = Button( 450, 200, red_fighter, False)
#game loop 
run = True 
while run:
    screen.fill((202,228, 241))

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
