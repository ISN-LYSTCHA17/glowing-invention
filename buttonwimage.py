# import drawing lib
import pygame
# game constants
from constants import *


# this object will represent a button (with which the user can interract)
class ButtonWImage:
    def __init__(self, xpos, ypos, xsize, ysize, image, color):
        self.xpos = xpos
        self.ypos = ypos
        self.xsize = xsize
        self.ysize = ysize
        self.color = color
        self.image = pygame.image.load(image).convert_alpha()

    def render(self, win):
        # we draw a rect using pygame.draw module
        # we give the window, the color and then the rect defining
        # the rectangle
        pygame.draw.rect(win, self.color, (self.xpos, self.ypos, self.xsize, self.ysize))
        win.blit(self.image, (self.xpos, self.ypos))

    def collide(self, xmouse, ymouse):
        # we check if the (xmouse, ymouse) is in the button rect
        if self.xpos <= xmouse <= self.xpos + self.xsize and self.ypos <= ymouse <= self.ypos + self.ysize:
            # we return the boolean True if the mouse clicked on the button
            return True
        else:
            # otherwise we return the boolean False
            return False
