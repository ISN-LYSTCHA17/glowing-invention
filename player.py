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

    def move(self, direction, level):
        # copy its position in two new variables x and y
        x = self.pos[0]
        y = self.pos[1]
        # we change the orientation of the character for the new one
        self.orientation = direction
        
        # we create temporary position to do the tests
        new_pos_x = x
        new_pos_y = y
        
        if direction == UP:
            # we go up, we take off the speed to move up the player on the screen
            new_pos_y -= self.speed
            # we check the collision. True if colliding, otherwise False
            #                         we take the bloc in x divid by the size of a bloc, same in y
            collision = level.collide(new_pos_x // TILESIZE, new_pos_y // TILESIZE)
            # if the bloc is NOT colliding
            # we apply the new pos
            if not collision:
                x = new_pos_x
                y = new_pos_y
        elif direction == DOWN:
            new_pos_y += self.speed
            collision = level.collide(new_pos_x // TILESIZE, new_pos_y // TILESIZE)
            if not collision:
                y = new_pos_y
                x = new_pos_x
        elif direction == RIGHT:
            new_pos_x += self.speed
            collision = level.collide(new_pos_x // TILESIZE, new_pos_y // TILESIZE)
            if not collision:
                y = new_pos_y
                x = new_pos_x
        elif direction == LEFT:
            new_pos_x -= self.speed
            collision = level.collide(new_pos_x // TILESIZE, new_pos_y // TILESIZE)
            if not collision:
                y = new_pos_y
                x = new_pos_x

        # we affect the new pos to the player position on the screen
        self.pos = [x, y]

    def render(self, win):
        # we are given a reference to the window,
        # with which we can blit (display an image) on
        # specifying a position
        win.blit(self.sprites[self.orientation], self.pos)
    
    def update(self):
        # update animations and all that stuff (or not)
        pass
