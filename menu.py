# import drawing lib
import pygame
# pygame constants as events' constants
from pygame.locals import *
# game constants
from constants import *
# we import the button class
from button import Button


class Menu:
    def __init__(self, win):
        self.running = False
        self.win = win
        # creating a font from system default fonts, with size 18
        self.font = pygame.font.SysFont("arial", 18)
        
        # our buttons
        self.btn_game = Button(10, 10, 20, 15, "Jouer", self.font)
        self.btn_customize = Button(10, 40, 20, 15, "Personnaliser", self.font)
        self.btn_quit = Button(10, 70, 20, 15, "Quitter", self.font)

    def load(self):
        self.running = True

    def update(self):
        pass

    def render(self):
        # clear the screen before blitting anything to items
        pygame.draw.rect(self.win, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
        # we render all the buttons
        self.btn_game.render(self.win)
        self.btn_customize.render(self.win)
        self.btn_quit.render(self.win)

    def run(self):
        while self.running:
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    self.running = False
                elif ev.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.btn_game.collide(x, y):
                        return MENU_GAME
                    elif self.btn_customize.collide(x, y):
                        return MENU_PERSONNALIZE
                    elif self.btn_quit.collide(x, y):
                        return MENU_QUIT

            self.update()

            self.render()

            pygame.display.flip()

        return MENU_QUIT
