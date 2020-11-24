#https://www.youtube.com/watch?v=UdsNBIzsmlI&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=3

import os
import pygame
pygame.init()

size = width, height = 500, 500

win = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.display.set_caption("First Game")

assets = os.listdir("assets")
screen_width = 500
screen_height = 480

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5
is_jump = False
jump_count = 10
run = True
left = False
right = False
walk_count = 0
walk_right = []
walk_left = []
bg = pygame.image.load('assets/bg.jpg')
char = pygame.image.load('assets/standing.png')

import os

assets = os.listdir("assets")
r = "R"
e = "E"
for file in assets:
    if e not in file:
        if r in file:
            _ = pygame.image.load("assets/" + file)
            walk_right.append(_)
            walk_left.append(pygame.transform.flip(_, True, False))
       
def redraw_game_window():
    global walk_count
    win.blit(bg, (0,0))

    if walk_count + 1 >= 27:
        walk_count = 0
        
    if left:
        win.blit(walk_left[walk_count//3], (x, y))
        walk_count += 1
    elif right:
        win.blit(walk_right[walk_count//3], (x, y))
        walk_count += 1
    else:
        win.blit(char, (x, y))
        
    pygame.display.update()
                             
while run:
    clock.tick(27)
    #pygame.time.delay(100) ## in milliseconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_width - width:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walk_count = 0
        
    if not(is_jump):
        # if keys[pygame.K_UP] and y >= vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < screen_height - height:
        #     y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count**2)*0.5*neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
                             
    redraw_game_window()

pygame.quit()
    


