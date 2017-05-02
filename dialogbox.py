import pygame
from constants import *


class DialogBox:
    def __init__(self, text, _type="_me"):
        self.text = text
        self.font = pygame.font.SysFont("arial", 18)
        self.rendered_text = None
        self.set_text(self.text)
        self.bubble = pygame.image.load("gfx/gui/bubble" + _type + ".png").convert_alpha()
        self.rendering = False

    def set_text(self, txt):
        self.text = txt
        if isinstance(txt, (tuple, list)):
            self.rendered_text = []
            for i in txt:
                self.rendered_text.append(self.font.render(i, True, (0, 0, 0)))
        else:
            self.rendered_text = self.font.render(self.text, True, (0, 0, 0))

    def render(self, screen):
        if self.rendering:
            screen.blit(self.bubble, (10, HEIGHT - 110))
            if isinstance(self.rendered_text, list):
                for i, e in enumerate(self.rendered_text):
                    screen.blit(e, (30, HEIGHT - 100 + 22 * i))
            else:
                screen.blit(self.rendered_text, (30, HEIGHT - 100))

    def trigger(self):
        self.rendering = not self.rendering
