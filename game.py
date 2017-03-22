# pygame constants, such as the events' code
from pygame.locals import *
# drawing lib
import pygame
# game constants
from constants import *
# we import the button class
from button import Button
# player
from player import Player
# level
from level import Level
# random message choosing + random crypting method
import quests


class Game:
    def __init__(self, win):
        self.running = False
        self.win = win
        self.player = Player()
        self.level = Level()
        self.message = quests.Message()

    def load(self):
        self.running = True
        # set the key repeat after 200ms of continuing keyboard input
        # repeated each 100ms
        pygame.key.set_repeat(200, 100)
        # load the player
        self.player.load()
        # load the level
        self.level.load()
        # start the crypting
        self.message.start()

    def update(self):
        # game updating method
        self.player.update()

    def render(self):
        # game rendering method
        # clear the screen before blitting anything to items
        pygame.draw.rect(self.win, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
        # first render map
        self.level.render(self.win)
        # then player otherwise the player will be behind the map
        self.player.render(self.win)

    def run(self):
        # main game loop
        while self.running:
            # events' dispatching loop
            for ev in pygame.event.get():
                # handle quit event
                if ev.type == QUIT:
                    self.running = False
                # handle clic
                elif ev.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.pos()
                # handling events : checking if we need to move the player
                #  WASD = ZQSD for pygame
                elif ev.type == KEYDOWN:
                    if ev.key == K_w:
                        self.player.move(UP, self.level)
                    elif ev.key == K_s:
                        self.player.move(DOWN, self.level)
                    elif ev.key == K_a:
                        self.player.move(LEFT, self.level)
                    elif ev.key == K_d:
                        self.player.move(RIGHT, self.level)

            # update game values
            self.update()

            # render game objets
            self.render()

            # flip the screen to display the modifications
            pygame.display.flip()
