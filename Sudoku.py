import pygame
import requests


response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json(['board'])
grid_original = [[grid[x][y]for y in range(len(grid[0]))] for x in range(len(grid))]
original_grid_element_colour = (52, 31, 151)


width = 550
background_colour = (251,247,245)

def main():
    pygame.init()
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku")
    win.fill(background_colour)
    myfont = pygame.font.SysFont('Times New Roman', 35)
# draws the grid the game is played on
    for i in range(0, 10):
        #checks the divisibilty of the number to combine the hard lines with the thinner ones.
        if(i%3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500), 4 )
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )
        #generates main 9x9 grid
        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500), 2 )
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()

    for i in range(len(grid)): # THE INDICES "I" AND "J" ARE CORESPONDINGLY HORIZONTAL(J) AND VERTICAL(I)
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_colour)
                win.blit(value, ((j+1)*50 + 15, (i+1*50 + 15)))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()