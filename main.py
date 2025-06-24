# import libraries and files
import pygame
import math
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
pi = math.pi
player_imges = []

for i in range(1, 5):
    player_imges.append(pygame.transform.scale(pygame.image.load(f"media/pacman_player/{i}.png"), (45, 45)))



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
            if level[row][col] == 5:
                pygame.draw.arc(screen, color, 
                                [(col * num2 - (num2 * 0.4)) - 2, (row * num1 + (0.5 * num1)), num2, num1], 0, pi/2, 3)
            if level[row][col] == 6:
                pygame.draw.arc(screen, color, 
                                [(col * num2 + (num2 * 0.5)), (row * num1 + (0.5 * num1)), num2, num1], pi/2, pi, 3)
            if level[row][col] == 7:
                pygame.draw.arc(screen, color, 
                                [(col * num2 + (num2 * 0.5)), (row * num1 - (0.4 * num1)), num2, num1], pi, 3 * pi/2, 3)
            if level[row][col] == 8:
                pygame.draw.arc(screen, color, 
                                [(col * num2 - (num2 * 0.4)) - 2, (row * num1 - (0.4 * num1)), num2, num1], 3 * pi/2, 2 * pi, 3)   
            if level[row][col] == 9:
                pygame.draw.line(screen, "white", (col * num2, row * num1 + (0.5 * num1)),
                                 ((col * num2) + num2, row * num1 + (0.5 * num1)), 3)

def draw_player():
    pass


# running display
run = True
while run: 
    timer.tick(fps)
    screen.fill("black")
    draw_board()
    draw_player()
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False
            
    pygame.display.flip()
pygame.quit()

