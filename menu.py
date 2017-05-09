# import drawing lib
import pygame
# pygame constants as events' constants
from pygame.locals import *
# game constants
from constants import *
# we import the button class
from button import Button
import os


txt_first = [
    "Tu vas etre redirigé vers l'interface de création de personnage",
    "étant donné que ceci est ta première partie :) !"
]


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
        self.btn_new = Button((WIDTH - 100) // 2, (HEIGHT - 30) // 2 - 40, 100, 30, "Nouvelle partie", (20, 150, 20), self.font, (0, 0, 0))
        self.btn_game = Button((WIDTH - 90) // 2, (HEIGHT - 30) // 2 - 40, 90, 30, "Jouer", (20, 150, 20), self.font, (0, 0, 0))
        self.btn_customize = Button((WIDTH - 90) // 2, (HEIGHT - 30) // 2, 90, 30, "Personnaliser", (20, 20, 150), self.font, (255, 255, 255))
        self.btn_quit = Button((WIDTH - 90) // 2, (HEIGHT - 30) // 2 + 40, 90, 30, "Quitter", (150, 20, 20), self.font, (0, 0, 0))

        self.txt_first_game = Button(10, (HEIGHT - 44) // 2, WIDTH - 20, 44, txt_first, (128, 128, 128), self.font, (255, 255, 255))

    def load(self):
        self.running = True
        self.new_game = not os.path.exists("saves/game")

    def update(self):
        pass

    def render(self):
        # clear the screen before blitting anything to items
        self.win.blit(self.bckg, (self.x, 0))
        # we render all the buttons
        if not self.new_game:
            self.btn_game.render(self.win)
            self.btn_customize.render(self.win)
        else:
            self.btn_new.render(self.win)
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
                    if not self.new_game:
                        if self.btn_game.collide(x, y):
                            return MENU_GAME
                        elif self.btn_customize.collide(x, y):
                            return MENU_PERSONNALIZE
                    else:
                        if self.btn_new.collide(x, y):
                            while True:
                                ev = pygame.event.poll()
                                if ev.type == MOUSEBUTTONDOWN:
                                    x, y = pygame.mouse.get_pos()
                                    if self.txt_first_game.collide(x, y):
                                        break
                                self.txt_first_game.render(self.win)
                                pygame.display.flip()
                            return MENU_PERSONNALIZE
                    if self.btn_quit.collide(x, y):
                        return MENU_QUIT

            self.update()

            self.render()

            pygame.display.flip()

        return MENU_QUIT
