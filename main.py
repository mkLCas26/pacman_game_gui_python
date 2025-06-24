# import libraries and files
import pygame
from pacboard import boards


pygame.init()

width = 900
height = 950
screen = pygame.display.set_mode([width, height])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font("freesansbold.ttf", 20)
level = boards


run = True
while run: 
    timer.tick(fps)
    screen.fill("black")
    draw_board()
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False
            
    pygame.display.flip()
pygame.quit()

