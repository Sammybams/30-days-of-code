import pygame
from pygame.locals import *
from sys import exit
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
display_width = 608
display_height = 400
berry = pygame.image.load('berry.png')
wall = pygame.image.load('wall.png')
snake = pygame.image.load('snake.png')
gameIcon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(gameIcon)

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake-Xenzia')
clock = pygame.time.Clock()
snake_block = 16
snake_speed = 5
pause = False
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def game_wall():
    """Constructs the game's walls."""
    a = 0
    while a<38:
        #pygame.draw.rect(screen, red, [16*a,0, snake_block, snake_block])
        screen.blit(wall,(16*a,0))
        a+=1
    b=1
    while b<40:
        #pygame.draw.rect(screen, red, [0,16*b, snake_block, snake_block])
        screen.blit(wall,(0,16*b))
        b+=1

    c=1
    while c<40:
        #pygame.draw.rect(screen, red, [584,16*c, snake_block, snake_block])
        screen.blit(wall,(592,16*c))
        c+=1
    d=1
    while d<37:
        #pygame.draw.rect(screen, red, [16*d,384, snake_block, snake_block])
        screen.blit(wall,(16*d,384))
        d+=1


def my_score(score):
    """Displays the players current score."""
    score_display = score_font.render("Score: " + str(score), True, (85,107,47))
    screen.blit(score_display, [20, 20])

def level(ab):
    """Displays the players current game level."""
    value = score_font.render("Level: " + str(ab), True, (85,107,47))
    screen.blit(value, [480, 20])
    
def our_snake(snake_block, snake_list):
    """Draws the snake on the screen."""
    for x in snake_list:
        #pygame.draw.rect(screen, blue, [x[0], x[1], snake_block, snake_block])
        screen.blit(snake,[x[0], x[1], snake_block, snake_block])
 
def button(msg,x,y,w,h,ic,ac,action=None):
    """
    Takes in a message that would be displayed on button, the range of co-ordinates of the button, the different
    colour changes of the button and an action.
    Determines if the mouse is clicked within the range of the buttons and performs the inpuutted action.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    #Displays message on button
    small_text = pygame.font.SysFont("timesnewromanboldttf",20)
    text_s = small_text.render(msg,True, (192,255,62))
    text_rect_s = text_s.get_rect()
    text_rect_s.center = (x+(w//2),y+(h//2))
    screen.blit(text_s, text_rect_s)

def button1(msg,x,y,w,h,ic,ac,action=None):
    """
    Takes in a message that would be displayed on button, the range of co-ordinates of the button, the different
    colour changes of the button and an action.
    Determines if the mouse is clicked within the range of the buttons and performs the inpuutted action.

    Works the same as button one but specifically for the game_over and pause menus.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    #Displays message on button
    small_text = pygame.font.SysFont("timesnewromanboldttf",25)
    text_s = small_text.render(msg,True, (85,107,47))
    text_rect_s = text_s.get_rect()
    text_rect_s.center = (x+(w//2),y+(h//2))
    screen.blit(text_s, text_rect_s)
    
def quitgame():
    """Calls the game to quit when a quit button is clicked."""
    pygame.quit()
    exit()
    
def reset_game():
    """Resets the game when the 'Play Again' button is clicked."""
    global x,y,x_change,y_change
    x,y = 50,250
    x_change = 0
    y_change = 0
    main()
    
def unpause():
    """Sets 'pause' to False when called to unpause game."""
    global pause
    pause = False
    
def paused(color1,color2):
    """Pauses our game when the letter 'p' is clicked and displays a 'Continue' or 'Quit' button."""
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        my_font = pygame.font.SysFont("comicsansms",60)
        text = my_font.render("PAUSED",True, (85,107,47))
        text_rect = text.get_rect()
        text_rect.center = (300,160)
        screen.blit(text, text_rect)

        button1("Continue",90,260,115,27,color2,color1,unpause)
        button1("Quit",435,260,65,27,color2,color1,quitgame)
                
        pygame.display.update()
        

def new_win(color1,color2):
    """ new_win is called when the snake hits a boundary or hits it self and displays 'GAME OVER' with buttons to try again or quit."""
    my_font = pygame.font.SysFont("comicsansms",90)
    text = my_font.render("GAME OVER",True, (85,107,47))
    text_rect = text.get_rect()
    text_rect.center = (300,160)
    screen.blit(text, text_rect)
    dark_green = (85,107,47)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        button1("Try Again",90,260,115,27,color2,color1,reset_game)
        button1("Quit",435,260,65,27,color2,color1,quitgame)
        game_wall()
        pygame.display.update()
        
def main_menu():
    """Gives our game a menu page and displays the 'Play' and 'Quit' buttons by calling the button function."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
        screen.fill((85,107,47))
        pygame.display.update()
        #Displays our controls for the game.
        
        my_font = pygame.font.SysFont("timesnewromanboldttf",25)
        text = my_font.render("Controls",True, (202,255,112))
        text_rect = text.get_rect()
        text_rect.center = (60,40)
        screen.blit(text, text_rect)
        
        my_font1 = pygame.font.SysFont("timesnewromanboldttf",20)
        text1 = my_font.render("- Keyboard Up - To go up",True, (202,255,112))
        text_rect1 = text.get_rect()
        text_rect1.center = (55,70)
        screen.blit(text1, text_rect1)
        my_font2 = pygame.font.SysFont("timesnewromanboldttf",20)
        text2 = my_font.render("- Keyboard Down - To go down",True, (202,255,112))
        text_rect2 = text.get_rect()
        text_rect2.center = (55,100)
        screen.blit(text2, text_rect2)
        
        my_font3 = pygame.font.SysFont("timesnewromanboldttf",20)
        text3 = my_font.render("- Keyboard Left - To go left",True, (202,255,112))
        text_rect3 = text.get_rect()
        text_rect3.center = (55,130)
        screen.blit(text3, text_rect3)
        
        my_font4 = pygame.font.SysFont("timesnewromanboldttf",20)
        text4 = my_font.render("- Keyboard Right - To go right",True, (202,255,112))
        text_rect4 = text.get_rect()
        text_rect4.center = (55,160)
        screen.blit(text4, text_rect4)

        my_font5 = pygame.font.SysFont("timesnewromanboldttf",20)
        text5 = my_font.render("- Keyboard p - To pause game",True, (202,255,112))
        text_rect5 = text.get_rect()
        text_rect5.center = (55,190)
        screen.blit(text5, text_rect5)

        #Displays the condition to level up.
        my_font6 = pygame.font.SysFont("timesnewromanboldttf",30)
        text6 = my_font.render("Eat 10 berries to level up",True, (202,255,112))
        text_rect6 = text.get_rect()
        text_rect6.center = (60,260)
        screen.blit(text6, text_rect6)
        
        button("Play",100,320,65,25,(105,139,34),(85,107,47),main)
        button("Quit",435,320,65,25,(105,139,34),(85,107,47),quitgame)
                
        pygame.display.update()

def game_intro():
    """Gives our game a start-up page and displays the 'Play' and 'Quit' buttons by calling the button function."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
        screen.fill((85,107,47))
        pygame.display.update()
        my_font = pygame.font.SysFont("timesnewromanboldttf",60)
        text = my_font.render("Snake-Xenzia",True, (202,255,112))
        text_rect = text.get_rect()
        text_rect.center = (300,160)
        screen.blit(text, text_rect)
        
        button("Menu",100,260,65,25,(105,139,34),(85,107,47),main_menu)
        button("Quit",435,260,65,25,(105,139,34),(85,107,47),quitgame)
                
        pygame.display.update()

def main():
    """Contains our main game loop, which runs until it breaks out of the while loop."""
    global snake_speed,pause,berry,snake
    x = 50
    y = 250
 
    x_change = 0
    y_change = 0
 
    snake_list = []
    length_of_snake = 1
    level_tracker = 0
    #Creates random co-ordinates for the berry within the boundaries of the screen.
    berryx = round(random.randrange(17, 583 - snake_block) / 10.0) * 10
    berryy = round(random.randrange(17, 383 - snake_block) / 10.0) * 10
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == K_DOWN:
                    y_change = snake_block
                    x_change = 0
                elif event.key ==K_p:
                    pause = True
                    paused((0,244,0),(255,255,255))
        #Checks if the nake has hit any of the boundaries and calls new_win. 
        if x<16 or x>568 or y<16 or y>368:
            new_win((0,244,0),(255,255,255))
        
        x += x_change
        y += y_change
        screen.fill(white)
        #pygame.draw.rect(screen, green, [berryx, berryy, snake_block, snake_block])
        screen.blit(berry,[berryx, berryy, snake_block, snake_block])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        #Checks if the snake has hit itself and calls new_win.
        for m in snake_list[:-1]:
            if m == snake_head:
                new_win((0,244,0),(255,255,255))
 
        our_snake(snake_block, snake_list)
        my_score(length_of_snake-1)
        level((length_of_snake-1)//10 +1)
        game_wall()
        pygame.display.update()
        
        #Checks if the snake has eaten 10 berries and increases the speed of the snake.
        if level_tracker==10:
            #Stops increasing speed from when the the lenth of the snake is 150.
            if (length_of_snake-1)<=150:
                snake_speed+=1
                level_tracker  = level_tracker - 10
            
        #Checks if the snake has eaten a berry and creates a new berry with
        #new co-ordinates and increases it's length and level_tracker by 1.
        if x+8 in range(berryx,berryx+17) and y+8 in range(berryy,berryy+17):
            berryx = round(random.randrange(17, 583 - snake_block) / 10.0) * 10
            berryy = round(random.randrange(17, 383 - snake_block) / 10.0) * 10
            length_of_snake += 1
            level_tracker+=1
        clock.tick(snake_speed)
 

game_intro()
