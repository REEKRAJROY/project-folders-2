import pygame
import random
import os
import time
import neat

WIN_WIDTH = 600
WIN_HEIGHT = 800


BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
            self.x = x
            self.y = y
            self.tilt = 0
            self.tick_count = 0  #count number of birds
            self.vel = 0
            self.height = self.y
            self.img_count = 0
            self.img = self.IMGS[0]  #reference bird 0

    def jump(self):
        self.vel = -10.5  #negative velocity for moving up in Pygame
        self.tick_count = 0
        self.height = self.y  #where the bird moved

    def move(self):
        self.tick_count += 1
        d = self.vel*self.tick_count + 1.5*self.tick_count**2  #this will generate a wave type velocity where self.tick_count will keep on decreasing at first and then increase after hitting 0

        if d>=16:
            d = 16
        
        if d<0:
            d -= 2  #fine tune the displacement
        
        self.y = self.y + d  #tilting the bird

        if d<0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION  #ensuring bird is not rotated beyond MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL  #tilting all way down to 90 degrees
    
    def draw(self, win):
        self.img_count += 1

        # For animation of bird, loop through three images
        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # so when bird is nose diving it isn't flapping
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        # code beneath is for rotating the image 
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

        # collision
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

def draw_window(win, bird):
    win.blit(BG_IMG, (0,0))  #blit is used for drawing
    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird(200,200)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #clicking this button to quit the pygame
                run = False
        
        bird.move()
        draw_window(win, bird)




    pygame.quit()  #quiting the pygame
    quit()  #quiting the program

'''
while True:
    bird.move()  #takes care of how much the bird needs to move
'''