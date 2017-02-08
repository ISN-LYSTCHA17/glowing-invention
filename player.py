# import drawing lib
import pygame
# game constants
from constants import *
# lib to list all the files in a specified directory
# using a specified pattern
import glob


class Player:
    def __init__(self):
        # position is handle in a list of 2 elements (x, y)
        self.pos = [0, 0]
        # speed in pixel per move
        self.speed = 4
        # the direction which the character is facing
        self.orientation = DOWN
        # all the images for the character located in gfx/player
        self.sprites = []

    def load(self):
        # for each file listed in the list returned by the glob function
        # of the glob module. the glob function is applied to the directory
        # where the character is located to list all its images (aka sprites)
        for file in glob.glob("gfx/player/*.png"):
            # load an image using pygame image module
            img = pygame.image.load(file)
            img.convert_alpha()
            # we append an element to the sprites' list (here an image loaded before)
            self.sprites.append(img)

    def move(self, direction):
        # copy its position in two new variables x and y
        x = self.pos[0]
        y = self.pos[1]
        # we change the orientation of the character for the new one
        self.orientation = direction

        if direction == UP:
            pass
        elif direction == DOWN:
            pass
        elif direction == RIGHT:
            pass
        elif direction == LEFT:
            pass

        self.pos = [x, y]

    def render(self, win):
        # we are given a reference to the window,
        # with which we can blit (display an image) on
        # specifying a position
        win.blit(self.sprite[self.orientation], self.pos)
