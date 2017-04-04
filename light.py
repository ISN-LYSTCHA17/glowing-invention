from constants import *
import pygame
import pygame.gfxdraw
import random


class PreRenderedLight():
    def __init__(self, id_, pos, size, color, variation=0,
                 ambiantLight=176, threshold=12):
        self.lightID = id_
        self.lightColor = color
        self.variation = variation
        self.lightSize = size
        self.imageList = []
        self.nbImages = 10
        self.indexBlit = 0
        self.ambiantLight = ambiantLight
        self.threshold = threshold
        self.lightPos = [
            pos[0] - self.lightSize - self.variation + TILESIZE,
            pos[1] - self.lightSize - self.variation + TILESIZE
        ]
        self._t = 0

    def load(self):
        for number in range(0, self.nbImages):
            self.imageList.append(
                pygame.Surface(
                    (self.lightSize * 2 + self.variation * 2, self.lightSize * 2 + self.variation * 2),
                    pygame.SRCALPHA,
                    32
                )
            )
            self.imageList[number].convert_alpha()
            self.imageList[number].fill((0, 0, 0, 0))
        self._render()

    def move(self, pos):
        self.lightPos = pos

    def _render(self):
        for number in range(0, self.nbImages):
            maxRange = int(self.lightSize + random.random() * self.variation)
            for i in range(1, maxRange):
                r = self.lightColor[0] * (i / maxRange)
                g = self.lightColor[1] * (i / maxRange)
                b = self.lightColor[2] * (i / maxRange)
                t = int(255 - (self.ambiantLight * (i / maxRange)))
                pygame.gfxdraw.filled_circle(
                    self.imageList[number],
                    int(self.lightSize + self.variation / 2),
                    int(self.lightSize + self.variation / 2),
                    maxRange - i,
                    (r, g, b, t)
                )

    def blit(self, surf):
        xFillRect = self.lightPos[0]
        yFillRect = self.lightPos[1]

        if 0 <= xFillRect < surf.get_width() + self.imageList[self.indexBlit].get_width() and 0 <= yFillRect < surf.get_height() + self.imageList[self.indexBlit].get_height():
            surf.blit(self.imageList[self.indexBlit], (xFillRect, yFillRect))

        self._t += 1
        if self._t >= self.threshold:
            self._t = 0
            self.indexBlit += 1

        self.indexBlit %= self.nbImages
