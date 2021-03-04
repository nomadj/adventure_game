import pygame
pygame.init()

size = width, height = 500, 500

win = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 20
height = 20
vel = 10
run = True

while run:
    pygame.time.delay(100) ## in milliseconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (100, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
    


