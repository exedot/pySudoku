import pygame, sys
from button import Button
import requests
pygame.init()



SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
BG = pygame.image.load("sudoku_py/assets/Background.png")
def get_font(size): return pygame.font.SysFont("Comic Sans MS", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("sudoku_py/assets/Play Rect.png"), pos=(640, 250), text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        DIFFICULTY_BUTTON = Button(image=pygame.image.load("sudoku_py/assets/Options Rect.png"), pos=(640, 400), text_input="difficultyselect", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("sudoku_py/assets/Quit Rect.png"), pos=(640, 550), text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, DIFFICULTY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main()
                if DIFFICULTY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    difficultyselect(difficulty, response, grid)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

def difficultyselect(difficulty, response, grid):
    while True:
        difficultyselect_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        difficultyselect_TEXT = get_font(45).render("This is the DIFFICULTY SELECT screen.", True, "white")
        difficultyselect_RECT = difficultyselect_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(difficultyselect_TEXT, difficultyselect_RECT)

        BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(40), base_color="white", hovering_color="Green")
        difficulty_HARD = Button(image=None, pos=(320, 200), text_input="HARD MODE", font = get_font(40), base_color="white", hovering_color="Green")
        difficulty_MEDIUM = Button(image=None, pos=(640, 200), text_input="MEDIUM MODE", font = get_font(40), base_color="white", hovering_color="Green")
        difficulty_EASY = Button(image=None, pos=(960, 200), text_input="EASY MODE", font = get_font(40), base_color="white", hovering_color="Green")

        
        for button in [BACK, difficulty_EASY, difficulty_MEDIUM, difficulty_HARD ]:
            button.changeColor(difficultyselect_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(difficultyselect_MOUSE_POS):
                    main_menu()
                if difficulty_HARD.checkForInput(difficultyselect_MOUSE_POS):
                    difficulty = ("https://sugoku.herokuapp.com/board?difficulty=hard")
                    response = requests.get(difficulty)
                    grid = response.json()['board']
                    return grid, response, difficulty, main(grid, response, difficulty)
                if difficulty_MEDIUM.checkForInput(difficultyselect_MOUSE_POS):
                    difficulty = ("https://sugoku.herokuapp.com/board?difficulty=medium")
                    response = requests.get(difficulty)
                    grid = response.json()['board']
                    return grid, response, difficulty, main(grid, response, difficulty)
                if difficulty_EASY.checkForInput(difficultyselect_MOUSE_POS):
                    difficulty = ("https://sugoku.herokuapp.com/board?difficulty=easy")
                    response = requests.get(difficulty)
                    grid = response.json()['board']
                    return grid, response, difficulty, main(grid, response, difficulty)              
        pygame.display.update()  

background_colour = (251,247,245)
buffer = 5
difficulty = "https://sugoku.herokuapp.com/board?difficulty=easy"
response = requests.get(difficulty)
grid = response.json()['board']
grid_original = [[grid[x][y]for y in range(len(grid[0]))] for x in range(len(grid))]
original_grid_element_colour = (52, 31, 151)

def insert(SCREEN, position):
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        #Checking which event has taken place
        for event in pygame.event.get():
            #If the player has quit, the program returns that outcome and is terminated
            if event.type == pygame.QUIT:
                return
            #If key is pressed then:
            if event.type == pygame.KEYDOWN:
                #Determines whether input is not equal to zero
                if(grid_original[i-1][j-1] !=0):
                    return
                if(event.key == 48):
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(SCREEN, background_colour, (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    pygame.display.update()
                if(0< event.key - 48 <10): #searching for valid input
                    pygame.draw.rect(SCREEN, background_colour, (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    value = myfont.render(str(event.key-48), True, (0,0,0))
                    SCREEN.blit(value, (position[0]*50 + 15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                return()
            return()

def main(grid, response, difficulty):
    TEXT = get_font(45).render("SUDOKU", True, "Black")
    MOUSE_POS = pygame.mouse.get_pos()
    SOLVED = Button(image=None, pos=(640,360), text_input="SOLVED", font=get_font(75), base_color="Black", hovering_color="Green")
    SCREEN.blit(TEXT, SOLVED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if SOLVED.checkForInput(MOUSE_POS):
                validate()

    #Gives the program a recognisable title
    pygame.display.set_caption("SVDOKV")
    #Fills background with whatever colour you have chosen
    SCREEN.fill(background_colour)
    #Instructs pygame to use Comic Sans MS as it's font for the grid
    myfont = get_font(35)
    # draws the grid the game is played on
    for i in range(0, 10):
        #checks the divisibilty of the number to combine the hard lines with the thinner ones.
        if(i%3 == 0):
            #draws the thicker (3x3) grid to overlay the 9x9
            pygame.draw.line(SCREEN, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500), 4 )
            pygame.draw.line(SCREEN, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )
        #generates main 9x9 grid
        pygame.draw.line(SCREEN, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500), 2 )
        pygame.draw.line(SCREEN, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()

    # THE INDICES "I" AND "J" ARE CORESPONDINGLY VERTICAL(I) & HORIZONTAL(J)
    for i in range(0, len(grid[0])): 
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_colour)
                SCREEN.blit(value, ((j+1)*50 + 15, (i+1)*50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(SCREEN, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.update()

def verify_board(sudoku):

    # Check if input is a list
    if not isinstance(sudoku, list): 
        return False
        
    # List should contain 9 elements
    if len(sudoku) != 9: 
        return False
        
    for row in sudoku:
    
        # Check if rows are strings or lists
        if not isinstance(row, (list, str)):
            return False
        
        # The length of both lists and strings must equal 9
        # Use the join method to compare both strings and lists
        text = ''.join(row)
        if len(text) != 9:
            return False
            
        # Finally, check if row is digits-only
        if not text.isdigit():
            return False
    
    # Else, return True
    return True

def repeated(sudoku):    
    
    # Iterate each row
    for row in sudoku:        
        
        # Define array to append found numbers
        found = []        
        
        # Iterate each number in the row
        for digit in row:            
            # Check if current value is already found    
            if digit not in found:
                # Store found values
                found.append(digit)            
            
            else:                
                
                # Returns True if when it sees a repeated number
                return True    
    
    # If there were not repeated numbers, return False
    return False

def to_column_list(sudoku):

    nth_digit = []
	
    for nth in range(9):
		
        # Extract and store the nth digit of each row
        nth_digit.append([ row[nth] for row in grid ]) 
	
    # Return new list
    return nth_digit

def to_regions_list(sudoku):

    regions = []
    current_region = []
    
    # Iterate regions vertically
    for k in range(0,7,3): 
        
        # Iterate regions horizontally
        for p in range(0,7,3): 
            
            # Iterate region's row
            for i in range(0+k,3+k): 
                
                # Iterate row's digit
                for j in range(0+p,3+p): 
                    current_region.append(sudoku[i][j])
                
            regions.append(current_region)
            current_region = []
            
    return regions

def check_sudoku(sudoku):
    
    no_message = 'Not a valid solution!'
    
    if not verify_board(sudoku):
        return 'Please enter a valid board.'
    
    if repeated(sudoku):
        return no_message
    
    columns_matrix = to_column_list(sudoku)
    if repeated(columns_matrix):
        return no_message
    
    regions_matrix = to_regions_list(sudoku)
    if repeated(regions_matrix):
        return no_message
    
    return 'It is a valid solution!'
main_menu()