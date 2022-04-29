import pygame
import requests

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json(['board'])
grid_original = [[grid[x][y]for y in range(len(grid[0]))] for x in range(len(grid))]


width = 550
background_colour = (251,247,245)

def main():
    pygame.init()
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku")
    win.fill(background_colour)

    for i in range(0, 10):
        if(i%3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500), 4 )
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )
            #pygame.draw.line(win, (0,0,0), (), (), 2 )
        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500), 2 )
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()