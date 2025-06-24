# import libraries and files
import pygame
from pacboard import boards

# initialize pygame
pygame.init()

# display screen and other necessities
width = 900
height = 700
screen = pygame.display.set_mode([width, height])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font("freesansbold.ttf", 20)
level = boards
color = "blue"


def draw_board():
    num1 = ((height - 50) // 32)
    num2 = (width // 30)
    
    for row in range(len(level)): 
        for col in range(len(level[row])):
            if level[row][col] == 1:
                pygame.draw.circle(screen, "white", (col * num2 + (0.5 * num2), row * num1 + (0.5 * num1)), 4)
            if level[row][col] == 2:
                pygame.draw.circle(screen, "white", (col * num2 + (0.5 * num2), row * num1 + (0.5 * num1)), 10)
            if level[row][col] == 3:
                pygame.draw.line(screen, color, (col * num2 + (0.5 * num2), row * num1 ),
                                 (col * num2 + (0.5 * num2), (row * num1) + num1), 3)
            if level[row][col] == 4:
                pygame.draw.line(screen, color, (col * num2, row * num1 + (0.5 * num1)),
                                 ((col * num2) + num2, row * num1 + (0.5 * num1)), 3)
            

# running display
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

