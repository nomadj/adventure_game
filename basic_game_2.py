import pygame
pygame.init()

size = width, height = 500, 500

win = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.display.set_caption("First Game")

screen_width = 500
screen_height = 500
x = 50
y = 50
width = 20
height = 20
vel = 15
is_jump = False
jump_count = 8
run = True

while run:
    pygame.time.delay(100) ## in milliseconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - width:
        x += vel
    if not(is_jump):
        if keys[pygame.K_UP] and y >= vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screen_height - height:
            y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -8:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count**2)*0.5*neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8
        
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (100, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
    


