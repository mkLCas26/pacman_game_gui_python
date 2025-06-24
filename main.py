# import libraries and files
import pygame
import math
from pacboard import boards

# initialize pygame
pygame.init()

# display screen and other necessities
width = 900
height = 950
screen = pygame.display.set_mode([width, height])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font("freesansbold.ttf", 20)
level = boards
color = "blue"
pi = math.pi
player_images = []

for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f"media/pacman_player/{i}.png"), (45, 45)))
player_x = 450
player_y = 663
direction = 0
counter = 0

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
    # 0 - right, 1 - left, 2 - up, 3 - down
    if direction == 0:
        screen.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))


# running display
run = True
while run: 
    timer.tick(fps)
    if counter < 19:
        counter += 1
    else:
        counter = 0
        
    screen.fill("black")
    draw_board()
    draw_player()
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3
            
    pygame.display.flip()
pygame.quit()

