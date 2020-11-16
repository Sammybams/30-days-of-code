import pygame
from pygame.locals import *
from sys import exit

pygame.init()

Start = "X"
grid = [[None,None,None],
        [None,None,None],
        [None,None,None]]

winner = None
pause = False
screen = pygame.display.set_mode((390,415))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()
def initialize_board(screen):
    """
    Initialize the background and return it.
    This takes in a properly initialized pyGame display variable as its only parameter.
    Sets up the background of the board.
    Sets the color of the background using the RGB format.
    Draws the vertical and horizontal grid lines on the background that partitions the
    section of the background that is your game board into the expected nine boxes. 
    """ 
    background = pygame.Surface(screen.get_size()).convert()
    background.fill((224,224,224))

    #Vertical grid lines
    pygame.draw.line(background,(0,0,0),(130,10),(130,380),2)
    pygame.draw.line(background,(0,0,0),(260,10),(260,380),2)

    #Horizontal grid lines
    pygame.draw.line(background,(0,0,0),(10,130),(380,130),2)
    pygame.draw.line(background,(0,0,0),(10,260),(380,260),2)

    return background

def draw_status(board):
    """
    This function renders the current status (like the players turn and winner) at the bottom of the game board.
    It takes in the already initialized background as its parameter.
    First determines the message to be returned based on the current playing status.
    Sets the font for the message and renders the messsage into a variable.
    Erases any previous message and copy the rendered message onto the board.
    """
    global Start, winner
    
    if (winner is None):
        message = Start + "'s turn"
    else:
        message = winner + " wins!"

    my_font = pygame.font.SysFont("comicsansms",30)
    text = my_font.render(message,1, (10,10,10))

    board.fill((224,224,224),(0,380,380,25))
    board.blit(text,(10,380))
    
def show_board(screen,board):
    """
    This function draws/redraws the game board on the display now containing your message.
    It takes in the initialized pyGame display (same one that the initialize_board function took) and the
    background (same as the draw_status function's parameter).
    First it calls the draw_status function thereby adding the message section to the board; then it displays the board.
    """
    draw_status(board)
    screen.blit(board,(0,0))
    pygame.display.flip()

def board_position(mouse_X, mouse_Y):
    """
    Takea in a set of coordinates from the mouse as separate parameters and determines which box (row, column) the user clicked.
    It takes in the X and Y coordinates of the mouse clicked point and returns a tuple row and column clicked.
    """
    #Determine the row clicked
    if mouse_Y<130:
        row = 0
    elif mouse_Y<260:
        row = 1
    elif mouse_Y<390:
        row = 2
    else:
        row = None
    
    #Determine the column clicked
    if mouse_X<130:
        col = 0
    elif mouse_X<260:
        col = 1
    else:
        col = 2
    #Returns a tuple of row and column clicked
    return row,col

def depict_move(board,board_row,board_col,piece):
    """
    This function draws an X or O on the board in the specified row and column.
    It takes in the board, the row and column to be drawn in as separate parameters and the piece to be drawn.
    The function identifies the piece to be drawn and draws it in the right board space.
    """
    center_X = (board_col*130)+65
    center_Y = (board_row*130)+65

    if piece=='O':
        pygame.draw.circle(board,(0,0,0),(center_X,center_Y),40,1)
    else:
        pygame.draw.line(board,(0,0,0),(center_X-33,center_Y-33),
                         (center_X+33,center_Y +33),2)
        pygame.draw.line(board,(0,0,0),(center_X+33,center_Y-33),
                         (center_X-33,center_Y +33),2)
    #It sets the inserted piece to it's location on the grid.
    grid[board_row][board_col]=piece

def click_board(board):
    """
    This function gets the mouse position and activates the depict_move function.
    It takes in the play board as parameter, determines where the user clicked and if the space is not already occupied.
    Then it calls the depict_move function to draw the appropriate piece then changes the turn.
    """
    global grid,Start
    (mouse_X,mouse_Y)=pygame.mouse.get_pos()
    print(mouse_X,mouse_Y)
    (row,col) = board_position(mouse_X,mouse_Y)

    if ((grid[row][col]=='X') or (grid[row][col]=='O')):
        return
    depict_move(board,row,col,Start)
    
    #Changes turn
    if Start=='X':
        Start = 'O'
    else:
        Start = 'X'

def game_over(board):
    """
    This function determines if anyone has won the game.
    It takes in the board as a parameter.
    it then checks the different winning conditions and draws a line on the board
    across the winning path to signify the end of the game.
    """
    global grid,winner
    
    #Checks for winning rows
    for row in range(3):
        if ((grid[row][0] == grid[row][1]==grid[row][2]) and
            (grid[row][0] is not None)):
            winner = grid[row][0]
            pygame.draw.line(board,(0,0,0),(20,(row+1)*130 - 65),
                             (370,(row+1)*130 - 65),2)
            break
        
    #Checking for winning columns
    for col in range(3):
        if ((grid[0][col] == grid[1][col]==grid[2][col]) and
            (grid[0][col] is not None)):
            winner = grid[0][col]
            pygame.draw.line(board,(0,0,0),((col+1)*130 - 65,20),
                             ((col+1)*130 - 65,370),2)
            break
    
    #Checking for winning diagonals
    if ((grid[0][0] == grid[1][1]==grid[2][2]) and
        (grid[0][0] is not None)):
        winner = grid[0][0]
        pygame.draw.line(board,(0,0,0),(20,20),
                         (370,370),2)
        
    if ((grid[0][2] == grid[1][1]==grid[2][0]) and
        (grid[0][2] is not None)):
        winner = grid[0][2]
        pygame.draw.line(board,(0,0,0),(370,20),
                         (20,370),2)

def quitgame():
    """Calls the game to quit when a quit button is clicked."""
    pygame.quit()
    exit()

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
    text_s = small_text.render(msg,True, (10,10,10))
    text_rect_s = text_s.get_rect()
    text_rect_s.center = (x+(w//2),y+(h//2))
    screen.blit(text_s, text_rect_s)

def unpause():
    """Sets 'pause' to False when called to unpause game."""
    global pause
    pause = False
    
def paused():
    """Pauses our game when the letter 'p' is clicked and displays a 'Continue' or 'Quit' button."""
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((224,224,224))
        my_font = pygame.font.SysFont("comicsansms",60)
        text = my_font.render("PAUSED",True, (10,10,10))
        text_rect = text.get_rect()
        text_rect.center = (195,185)
        screen.blit(text, text_rect)

        button("Continue",60,260,100,25,(161,161,161),(128,128,128),unpause)
        button("Quit",245,260,65,25,(161,161,161),(128,128,128),quitgame)
                
        pygame.display.update()
        
def reset_game():
    """Resets the game when the 'Play Again' button is clicked."""
    global grid, winner, Start
    Start = 'X' 
    winner = None
    grid = [[None]*3, [None]*3, [None]*3]
    main()
    
def new_win():
    """
    Finds if we have a winner and displays the win message or otherwise a draw message.
    Displays the 'Play Again' and 'Quit' buttons by calling the button function.
    """
    if winner!=None:
        my_font = pygame.font.SysFont("comicsansms",90)
        text = my_font.render(winner + " wins!",True, (10,10,10))
        text_rect = text.get_rect()
        text_rect.center = (195,185)
        screen.blit(text, text_rect)
    else:
        my_font = pygame.font.SysFont("comicsansms",90)
        text = my_font.render("It's a Draw",True, (10,10,10))
        text_rect = text.get_rect()
        text_rect.center = (195,185)
        screen.blit(text, text_rect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        button("Play Again",60,260,100,25,(161,161,161),(128,128,128),reset_game)
        button("Quit",245,260,65,25,(161,161,161),(128,128,128),quitgame)
                
        pygame.display.update()
        
def game_intro():
    """Gives our game a start-up page and displays the 'Play' and 'Quit' buttons by calling the button function."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((224,224,224))
        pygame.display.update()
        my_font = pygame.font.SysFont("timesnewromanboldttf",60)
        text = my_font.render("Tic-Tac-Toe",True, (10,10,10))
        text_rect = text.get_rect()
        text_rect.center = (195,185)
        screen.blit(text, text_rect)
        
        button("Play",80,260,65,25,(161,161,161),(128,128,128),main)
        button("Quit",245,260,65,25,(161,161,161),(128,128,128),quitgame)
                
        pygame.display.update()
        
def main():
    """Contains our main game loop, which runs until it breaks out of the while loop."""
    global pause
    board = initialize_board(screen)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type==MOUSEBUTTONDOWN:
                click_board(board)
            elif event.type == KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            elif winner!=None:
                new_win()
            elif winner==None:
                if all(j!=None for i in grid for j in i):
                    new_win()
            game_over(board)
            show_board(screen,board)
        clock.tick(30)
        
#Starts our game intro page.
game_intro()
