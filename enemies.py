import os
import pygame

assets = os.listdir('assets')
walk_left = []
walk_right = []
e = 'E'
r = 'R'
class Enemy(object):
    for file in assets:
        if e in file and r in file:
            _ = pygame.image.load('assets/' + file)
            walk_right.append(_)
            walk_left.append(pygame.transform.flip(_, True, False))

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walk_count + 1 >= 33:
            self.walk_count = 0
        if self.vel > 0:
            win.blit(walk_right[self.walk_count //3], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(walk_left[self.walk_count //3], (self.x, self.y))
            self.walk_count += 1

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
            
        
