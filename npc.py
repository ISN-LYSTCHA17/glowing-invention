from constants import *
import pygame
from pygame.locals import *
import dialogbox
import math


class NPC:
    def __init__(self, name, x, y, orientation, message):
        self.name = name
        self.x, self.y = x, y
        self.orientation = orientation
        self.message = message
        self.has_already_spoken = False
        self.message_has_spoken = "Vous m'avez déjà parlé !"
        self.dbox = dialogbox.DialogBox(self.message, _type="")
        self.image = pygame.image.load("gfx/personnalize/" + self.name + "/" + self.orientation + ".png").convert_alpha()

    def speak(self):
        self.dbox.trigger()
        if self.has_already_spoken:
            self.dbox.set_text(self.message_has_spoken)
        if not self.has_already_spoken:
            self.has_already_spoken = True

    def render(self, win):
        self.dbox.render(win)
        win.blit(self.image, (self.x, self.y))

    def collide(self, x, y, xp, yp):
        gx, gy = self.x + NPCSIZE // 2 - xp, self.y + NPCSIZE // 2 - yp
        print(gx, gy, math.sqrt(gx ** 2 + gy ** 2))
        if math.sqrt(gx ** 2 + gy ** 2) > NPC_MAX_DIST * TILESIZE:
            return False
        if self.x <= x <= self.x + NPCSIZE and self.y <= y <= self.y + NPCSIZE:
            return True
        return False
