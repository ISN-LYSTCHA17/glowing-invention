# import drawing lib
import pygame
# pygame constants as events' constants
from pygame.locals import *
# game constants
from constants import *
from buttonwimage import ButtonWImage
import glob
import os
import textentry
from button import Button
import shutil


class Personnalize:
    def __init__(self, win):
        self.running = False
        self.win = win

        self.dbox = textentry.TextBox(self.win, font=pygame.font.SysFont("arial", 18), sy=22, x=((WIDTH - 120) // 2), y=HEIGHT - 32)
        self.btns = []
        x, y = 200, 20
        i = 0
        for folder in sorted(glob.glob("gfx/personnalize/*")):
            self.btns.append(ButtonWImage(x, y, 64, 64, folder + "/front.png", (128, 48, 120)))
            i += 1
            if i == 5:
                y = 20
                x = WIDTH - 264
            else:
                y += 74
        self.valid_btn = Button((WIDTH - 80) // 2, (HEIGHT - 32), 50, 22, "Valider", (12, 200, 35), pygame.font.SysFont("arial", 18), (0, 0, 0))
        self.has_valid = False
        self.selected = -1

    def load(self):
        self.running = True

    def update(self):
        pass

    def render(self):
        pygame.draw.rect(self.win, (20, 175, 170), (0, 0) + self.win.get_size())
        for btn in self.btns:
            btn.render(self.win)
        if not self.has_valid:
            self.valid_btn.render(self.win)
        else:
            self.dbox.mainloop()

    def create_game(self):
        with open("saves/game", "w") as file:
            file.write(self.dbox.input)
        folder = sorted(glob.glob("gfx/personnalize/*"))[self.selected]
        for f in glob.glob(folder + "/*.png"):
            if os.path.exists("gfx/player/" + os.path.basename(f)):
                os.remove("gfx/player/" + os.path.basename(f))
            shutil.copyfile(f, "gfx/player/" + os.path.basename(f))

    def run(self):
        while self.running:
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    self.running = False
                elif ev.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for i, btn in enumerate(self.btns):
                        if btn.collide(x, y):
                            if self.selected != -1:
                                self.btns[self.selected].color = (128, 48, 120)
                            self.selected = i
                            btn.color = (50, 120, 50)
                            break
                    if not self.has_valid:
                        if self.valid_btn.collide(x, y):
                            self.has_valid = True

            if not self.dbox.is_running():
                self.create_game()
                self.running = False

            self.update()

            self.render()

            pygame.display.flip()
