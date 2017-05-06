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
        self.bckg = pygame.image.load("gfx/menu/background.png").convert_alpha()
        self.x = 0
        self.c = 0
        self.b = True

        # our buttons
        self.btn_game = Button((WIDTH - 90) // 2, (HEIGHT - 30) // 2 - 40, 90, 30, "Jouer", (20, 150, 20), self.font, (0, 0, 0))
        self.btn_customize = Button((WIDTH - 90) // 2, (HEIGHT - 30) // 2, 90, 30, "Personnaliser", (20, 20, 150), self.font, (255, 255, 255))
        self.btn_quit = Button((WIDTH - 90) // 2, (HEIGHT - 30) // 2 + 40, 90, 30, "Quitter", (150, 20, 20), self.font, (0, 0, 0))

    def load(self):
        self.running = True

    def update(self):
        pass

    def render(self):
        # clear the screen before blitting anything to items
        self.win.blit(self.bckg, (self.x, 0))
        # we render all the buttons
        self.btn_game.render(self.win)
        self.btn_customize.render(self.win)
        self.btn_quit.render(self.win)

    def run(self):
        while self.running:
            self.c += 1
            if not self.c % 64:
                if self.b: self.x -= 1
                else: self.x += 1

                if self.x <= -279:
                    self.b = False
                    self.x += 1
                if self.x >= 0:
                    self.b = True
                    self.x -= 1

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
