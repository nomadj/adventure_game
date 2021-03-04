import player
import os
import pygame
pygame.init()

size = width, height = 500, 500

win = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.display.set_caption("First Game")

screen_width = 500
screen_height = 480

clock = pygame.time.Clock()

def redraw_game_window():
    win.blit(player.bg, (0,0))
    man.draw(win)
    pygame.display.update()
    
man = player.Player(300, 410, 64, 64)    
run = True                             
while run:
    clock.tick(27)
    #pygame.time.delay(100) ## in milliseconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x >= man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walk_count = 0
        
    if not(man.is_jump):
        # if keys[pygame.K_UP] and man.y >= man.vel:
        #     man.y -= man.vel
        # if keys[pygame.K_DOWN] and man.y < screen_height - man.height:
        #     man.y += man.vel
        if keys[pygame.K_SPACE]:
            man.is_jump = True
            man.right = False
            man.left = False
    else:
        if man.jump_count >= -10:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count**2)*0.5*neg
            man.jump_count -= 1
        else:
            man.is_jump = False
            man.jump_count = 10
                             
    redraw_game_window()

pygame.quit()
    


