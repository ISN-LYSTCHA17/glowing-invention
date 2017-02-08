# import drawing lib
import pygame
# pygame constants as events' constants
from pygame.locals import *
# game constants
from constants import *


class Personnalize:
    def __init__(self, win):
        self.running = False
        self.win = win

    def load(self):
        self.running = True

    def update(self):
        pass

    def render(self):
        pass

    def run(self):
        while self.running:
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    self.running = False

            self.update()

            self.render()

            pygame.display.flip()
