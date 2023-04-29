import pygame 
import os #! define path for images 
pygame.font.init() #initialize fonts 
pygame.mixer.init() #initialize sounds 
 

#TODO
#!  
#? 
#* 
# 
WIDTH, HEIGHT = 1200 , 700 #! make it here or put in tuple below
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  #? create window 
pygame.display.set_caption("First Game")  #? create name of game 

WHITE=(255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0 , 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT) #? create a rectangle for boder with x, y, w, h

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('tutorial assets', 'Assets_Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('tutorial assets', 'Assets_Gun+Silencer.mp3'))

HEALTH_FONT = pygame.font.SysFont('comicsans', 30) #size 
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 120 #? capped frame rate 
VEL = 5 #? velocity 
BULLET_VEL = 7 #? create velocity for bullet
MAX_BULLETS = 10
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT=pygame.USEREVENT+1 #? represnts the number for the user event 
RED_HIT = pygame.USEREVENT +2 #! user evnts to check if an event occurs 

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('tutorial assets','spaceship_yellow.png')) #? creating the path to access image 
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('tutorial assets','spaceship_red.png'))
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('tutorial assets', 'space.png')), (WIDTH, HEIGHT))
''' 
YELLOW_SPACESHIP = pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (55, 40)) #? resize image with name and size
'''

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (55, 40)), 90) #? rotate image by angle
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE,(0,0))
    #WIN.fill((WHITE))  #? fill screen with colour and RGB tuple value 
    pygame.draw.rect(WIN, BLACK, BORDER) #? colour rectangle
    
    red_health_text = HEALTH_FONT.render('Health:' +str(red_health), 1, WHITE ) #!render text through font
    yellow_health_text = HEALTH_FONT.render('Health:' +str(yellow_health), 1, WHITE )
    WIN.blit(red_health_text,( WIDTH - red_health_text.get_width() -10, 10))
    WIN.blit(yellow_health_text,(10, 10))

    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) #? draw surfaces on screen with blit and the position
    WIN.blit(RED_SPACESHIP,(red.x, red.y))

    for bullets in red_bullets:
        pygame.draw.rect(WIN, RED, bullets)
    for bullets in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullets)

    pygame.display.update() #! display must be updated for changed 

def yellow_handle_movement(keys_pressed, yellow): #? create a function
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  #? conditional for key being pressed 
            yellow.x -= VEL #? moving character 
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # right #? dont allow if the movment will be out of bounds 
            yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0 : #Up
            yellow.y-=VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - 60: #Down 
            yellow.y +=VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:# left #? conditional for key being pressed 
            red.x -= VEL #? moving character 
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # right 
            red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0 :  #Up
            red.y-=VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height - 30 < HEIGHT - 50:  #down 
            red.y+=VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet): #? check if rectangles collide
            pygame.event.post(pygame.event.Event(RED_HIT)) #! if this happens then post this event
            yellow_bullets.remove(bullet)
        elif  bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

             
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet): 
            pygame.event.post(pygame.event.Event(YELLOW_HIT)) 
            red_bullets.remove(bullet)
        elif bullet.x < 0:  #? adding projectile boundries
             red_bullets.remove(bullet)
def draw_winner(text):   
    draw_text = WINNER_FONT.render(text, 1, WHITE ) 
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2,
                            HEIGHT/2 - draw_text.get_height()/2))         
    pygame.display.update()
    pygame.time.delay(2000) #delay the time by 5 seconds/5k miliseconds
def main(): # main function
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) #? rectangle to represnt image with x, y, width and height
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) #! pass to draw window down below 

    red_bullets=[] #? create storage for all bullets
    yellow_bullets=[]

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock() #? Creating a clock object to set FPS and controls speed of while loop

    run = True 
    while run:
        clock.tick(FPS) #? Run the while loop at the FPS 
        for event in pygame.event.get():  #!
            if event.type == pygame.QUIT: #? if the QUIT button/event occurs or is pressed then exit code with run = false 
                run = False               #!
        
            if event.type == pygame.KEYDOWN: #? check what key is pressed]
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5) #! create a rectangle for bullet with location, width and height
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play() #! play sound 

                if event.key == pygame.K_RCTRL and len(red_bullets)< MAX_BULLETS:
                    bullet = pygame.Rect(red.x , red.y + red.height//2 -2, 10, 5) #!  no width as it is one the right hand side
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT: 
                yellow_health-=1
                BULLET_HIT_SOUND.play() 

        print(red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed() #? tells the program what keys are being pressed
        yellow_handle_movement(keys_pressed, yellow) #? use of function with conditions 
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health) #! call the function to draw 
        winner_text=''
        if yellow_health <=0:
            winner_text = 'Red Wins!'
        if red_health<=0:
            winner_text = 'Yellow Wins!'
        if winner_text !='':
            draw_winner(winner_text)
            #break #! QUIT GAME AFTER WIN
        
    
    pygame.quit()

if __name__ == "__main__": #? only runs this function if this file is run directly and 
    main()