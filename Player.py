import pygame
import requests

#VARIABLES
#Width is used by pygame in order to account for default grid values without changing individual elements
width = 550
#Background colour, self explained
background_colour = (251,247,245)
#A buffer variable is used in order to shave off excess in each rectangle drawn later
buffer = 5
#Extracts the pre-generated, actually solvable grid from this host website
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=hard")
#Assigns the board extracted above and applies them to our generated grid
grid = response.json()['board']
grid_original = [[grid[x][y]for y in range(len(grid[0]))] for x in range(len(grid))]
original_grid_element_colour = (52, 31, 151)


####################################################################################
def insert(win, position):
    #assigns position
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
                    pygame.draw.rect(win, background_colour, (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    pygame.display.update()
                if(0< event.key - 48 <10): #searching for valid input
                    pygame.draw.rect(win, background_colour, (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    value = myfont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*50 + 15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                return()
            return()

def main():
    #Initiate pygame plugin
    pygame.init()
    #Sets the parameters of the window's width and length
    win = pygame.display.set_mode((width, width))
    #Gives the program a recognisable title
    pygame.display.set_caption("Sudoku")
    #Fills background with whatever colour you have chosen
    win.fill(background_colour)
    #Instructs pygame to use Comic Sans MS as it's font for the grid
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    # draws the grid the game is played on
    for i in range(0, 10):
        #checks the divisibilty of the number to combine the hard lines with the thinner ones.
        if(i%3 == 0):
            #draws the thicker (3x3) grid to overlay the 9x9
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500), 4 )
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )
        #generates main 9x9 grid
        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500), 2 )
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    #Allows for continuous visual update as values are passed through the above algorithm
    pygame.display.update()

    # THE INDICES "I" AND "J" ARE CORESPONDINGLY HORIZONTAL(J) AND VERTICAL(I)
    for i in range(0, len(grid[0])): 
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_colour)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50))
    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
main()