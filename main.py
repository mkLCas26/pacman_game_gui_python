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
flicker = False
turns_allowed = [False, False, False, False]
direction_command = 0
player_speed  = 2
score = 0

def draw_misc():
    score_text = font.render(f'Score: {score}', True, "white")
    screen.blit(score_text, (10, 920))
                             
def check_collisions(scor):
    num1 = (height - 50) // 32
    num2 = width // 30
    if 0 < player_x < 870:
        if level[center_y // num1][center_x // num2] == 1:
            level[center_y // num1][center_x // num2] = 0 
            scor += 10
        if level[center_y // num1][center_x // num2] == 2:
            level[center_y // num1][center_x // num2] = 0 
            scor += 50
    
    return scor

def draw_board():
    num1 = ((height - 50) // 32)
    num2 = (width // 30)
    
    for row in range(len(level)): 
        for col in range(len(level[row])):
            if level[row][col] == 1:
                pygame.draw.circle(screen, "white", (col * num2 + (0.5 * num2), row * num1 + (0.5 * num1)), 4)
            if level[row][col] == 2 and not flicker:
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

def check_position(centerx, centery):
    turns = [False, False, False, False]
    num1 = (height - 50) // 32
    num2 = (width // 30)
    num3 = 15
    #check collisions
    if centerx // 30 < 29:
        if direction == 0:
            if level[centery // num1][(centerx - num3) // num2] < 3:
                turns[1] = True
        if direction == 1:
            if level[centery // num1][(centerx + num3) // num2] < 3:
                turns[0] = True
        if direction == 2:
            if level[(centery + num3) // num1][centerx// num2] < 3:
                turns[3] = True
        if direction == 3:
            if level[(centery - num3) // num1][centerx // num2] < 3:
                turns[2] = True
                
        if direction == 2 or direction == 3:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num3)//num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num3)//num1][centerx // num2] < 3:
                    turns[2] = True
            
            if 12 <= centery % num1 <= 18:
                if level[centery//num1][(centerx - num2) // num2] < 3:
                    turns[1] = True
                if level[centery//num1][(centerx + num2) // num2] < 3:
                    turns[0] = True
                    
        if direction == 0 or direction == 1:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num3)//num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num3)//num1][centerx // num2] < 3:
                    turns[2] = True
            
            if 12 <= centery % num1 <= 18:
                if level[centery//num1][(centerx - num2) // num2] < 3:
                    turns[1] = True
                if level[centery//num1][(centerx + num2) // num2] < 3:
                    turns[0] = True
                    
    else:
        turns[0] = True
        turns[1] = True
    return turns

def move_player(play_x, play_y):
    if direction == 0 and turns_allowed[0]:
        play_x += player_speed
    elif direction == 1 and turns_allowed[1]:
        play_x -= player_speed
    if direction == 2 and turns_allowed[2]:
        play_y -= player_speed
    elif direction == 3 and turns_allowed[3]:
        play_y += player_speed
    return play_x, play_y


# running display
run = True
while run: 
    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True
        
    screen.fill("black")
    draw_board()
    draw_player()
    draw_misc()
    
    center_x = player_x + 23
    center_y = player_y + 24   
    turns_allowed = check_position(center_x, center_y)
    player_x, player_y = move_player(player_x, player_y)
    score = check_collisions(score)
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction
      
    if direction_command == 0 and turns_allowed[0]:
        direction = 0
    if direction_command == 1 and turns_allowed[1]:
        direction = 1
    if direction_command == 2 and turns_allowed[2]:
        direction = 2
    if direction_command == 3 and turns_allowed[3]:
        direction = 3
            
    if player_x > 900:
        player_x = -47
    elif player_x < -50:
        player_x = 897
          
    pygame.display.flip()
pygame.quit()

