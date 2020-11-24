#https://www.youtube.com/watch?v=vc1pJ8XdZa0&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=6

import os
import pygame
import projectiles as proj
import player
import enemies
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
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
    
    
man = player.Player(300, 410, 64, 64)
goblin = enemies.Enemy(100, 410, 64, 64, 450)
bullets = []
run = True                             
while run:
    clock.tick(27)
    #pygame.time.delay(100) ## in milliseconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            proj.Projectile.facing = -1
        else:
            proj.Projectile.facing = 1
        if len(bullets) < 5:
            bullets.append(proj.Projectile(round(man.x+man.width//2),round(man.y + man.height //2),6,(0,0,0), proj.Projectile.facing))

    if keys[pygame.K_LEFT] and man.x >= man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.walk_count = 0
        man.standing = True
        
    if not(man.is_jump):
        # if keys[pygame.K_UP] and man.y >= man.vel:
        #     man.y -= man.vel
        # if keys[pygame.K_DOWN] and man.y < screen_height - man.height:
        #     man.y += man.vel
        if keys[pygame.K_UP]:
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
    


