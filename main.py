import pygame, sys
from button import Button
import requests
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
BG = pygame.image.load("sudoku_py/assets/Background.png")
def get_font(size): return pygame.font.SysFont("TIMES NEW ROMAN", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("sudoku_py/assets/Play Rect.png"), pos=(640, 250), text_input="PLAY", font=get_font(75), base_color="white", hovering_color="red")
        DIFFICULTY_BUTTON = Button(image=pygame.image.load("sudoku_py/assets/Options Rect.png"), pos=(640, 400), text_input="DIFFICULTY", font=get_font(75), base_color="white", hovering_color="red")
        QUIT_BUTTON = Button(image=pygame.image.load("sudoku_py/assets/Quit Rect.png"), pos=(640, 550), text_input="QUIT", font=get_font(75), base_color="white", hovering_color="red")
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

        difficultyselect_TEXT = get_font(45).render("DIFFICULTY SELECT (broken)", True, "white")
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
                    # HARD
                if difficulty_HARD.checkForInput(difficultyselect_MOUSE_POS):
                    difficulty = ("https://sugoku.herokuapp.com/grid?difficulty=hard")
                    response = requests.get(difficulty)
                    grid = response.json()['grid']
                    return grid, response, difficulty, main(grid, response, difficulty)
                    # MEDIUM
                if difficulty_MEDIUM.checkForInput(difficultyselect_MOUSE_POS):
                    difficulty = ("https://sugoku.herokuapp.com/grid?difficulty=medium")
                    response = requests.get(difficulty)
                    grid = response.json()['grid']
                    return grid, response, difficulty, main(grid, response, difficulty)
                    # EASY
                if difficulty_EASY.checkForInput(difficultyselect_MOUSE_POS):
                    difficulty = ("https://sugoku.herokuapp.com/grid?difficulty=easy")
                    response = requests.get(difficulty)
                    grid = response.json()['grid']
                    return grid, response, difficulty, main(grid, response, difficulty)              
        pygame.display.update()
          
# BOARD VARIABLES
background_colour = (251,247,245)
buffer = 5
difficulty = "https://sugoku.herokuapp.com/grid?difficulty=easy"
response = requests.get(difficulty)
# Below is doppleganger, originally grid = response.json()['board'] was used but no longer functioned, this is to show off the ui in video
grid = [[1, 4, 7, 0, 0, 0, 0, 0, 3],
        [2, 5, 0, 0, 0, 1, 0, 0, 0],
        [3, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 2, 0, 0, 0, 4],
        [0, 0, 0, 4, 1, 0, 0, 2, 0],
        [9, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 9],
        [4, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 0, 0, 8, 0, 0, 7]]
grid_original = [[grid[x][y]for y in range(len(grid[0]))] for x in range(len(grid))]
original_grid_element_colour = (52, 31, 151)
# INSERTION FUNCTION
def insert(position):
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
# MAIN FUNCTION
def main():
    #Gives the program a recognisable title
    pygame.display.set_caption("Philip Norris")
    #Fills background with whatever colour you have chosen
    SCREEN.fill(background_colour)
    #Instructs pygame to use Comic Sans MS as it's font for the grid
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
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
                insert((pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.display.update()

main_menu()