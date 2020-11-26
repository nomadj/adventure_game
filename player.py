import pygame
import os

bg = pygame.image.load('assets/bg.jpg')
char = pygame.image.load('assets/standing.png')
walk_right = []
walk_left = []
assets = os.listdir("assets")
r = "R"
e = "E"

for file in assets:
    if e not in file:
        if r in file:
            _ = pygame.image.load("assets/" + file)
            walk_right.append(_)
            walk_left.append(pygame.transform.flip(_, True, False))

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.standing = True
        self.hitbox = (self.x+17, self.y+11, 27, 52)
        
    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                win.blit(walk_left[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(walk_right[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.right:
                win.blit(walk_right[0], (self.x, self.y))
            else:
                win.blit(walk_left[0], (self.x, self.y))
        self.hitbox = (self.x+17, self.y+11, 27, 52)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
