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
# time
import time
import sys

txt_vigenere = "aaa"
txt_polybe = "bbb"
txt_caesar = "ccc"
txt_affine = "ddd"

class Game:
    def __init__(self, win):
        self.running = False
        self.win = win
        self.player = Player()
        self.level = Level()
        self.beginning = time.time()
        self.font = pygame.font.SysFont("arial", 18)

    def load(self):
        self.running = True
        # set the key repeat after 200ms of continuing keyboard input
        # repeated each 100ms
        pygame.key.set_repeat(200, 100)
        # load the player
        self.player.load()
        # load the level
        self.level.load()

        # small loop to display the type of crypting
        btns = [
            Button(10, 10, WIDTH - 20, HEIGHT - 20, txt_affine,   (128, 128, 128), self.font, (255, 255, 255)),
            Button(10, 10, WIDTH - 20, HEIGHT - 20, txt_caesar,   (128, 128, 128), self.font, (255, 255, 255)),
            Button(10, 10, WIDTH - 20, HEIGHT - 20, txt_polybe,   (128, 128, 128), self.font, (255, 255, 255)),
            Button(10, 10, WIDTH - 20, HEIGHT - 20, txt_vigenere, (128, 128, 128), self.font, (255, 255, 255))
        ]
        while True:
            ev = pygame.event.poll()
            if ev.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # if we displayed all the help messages, we stop and it will start the game
                if not btns:
                    break
                else:
                    # if we clicked on the displayed button we stop displaying it
                    if btns[0].collide(x, y):
                        btns.pop(0)
            # if we displayed all the help messages, we stop and it will start the game
            if not btns:
                break
            else:
                btns[0].render(self.win)
            pygame.display.flip()

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
        # then display a list of the indices
        pygame.draw.rect(self.win, (128, 128, 255), (WIDTH - 140, 0, 140, 140))
        i = 0
        for k, v in self.player.indices.items():
            if k != "end":
                self.win.blit(self.font.render(str(k) + " -> " + str(v), True, (0, 0, 0)), (WIDTH - 130, 10 + 30 * i))
                i += 1

    def stop_dialogs(self):
        self.player.stop_dialogs()
        if self.level.speaking_npc and self.level.speaking_npc.dbox.rendering:
            self.level.speaking_npc.dbox.trigger()

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
                    x, y = pygame.mouse.get_pos()
                    self.level.click_for_npc(x, y, self.player.pos[0], self.player.pos[1])
                # handling events : checking if we need to move the player
                #  WASD = ZQSD for pygame
                elif ev.type == KEYDOWN:
                    if ev.key == K_w:
                        self.player.move(UP, self.level, self.win)
                    elif ev.key == K_s:
                        self.player.move(DOWN, self.level, self.win)
                    elif ev.key == K_a:
                        self.player.move(LEFT, self.level, self.win)
                    elif ev.key == K_d:
                        self.player.move(RIGHT, self.level, self.win)
                    elif ev.key == K_SPACE:
                        self.stop_dialogs()

            # if the player has found the secret message we quit the game
            if self.player.found and not self.player.dbox.rendering:
                break

            # update game values
            self.update()

            # render game objets
            self.render()

            # flip the screen to display the modifications
            pygame.display.flip()

        # end
        if self.player.found:
            btn_quit = Button(0, 0, 100, 20, "Quitter le jeu", (150, 20, 20), self.font, (255, 255, 255))
            btn_continue = Button(100, 200, 100, 20, "Continuer", (20, 150, 20), self.font, (255,255,255))
            while True:
                ev = pygame.event.poll()
                if ev.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if btn_quit.collide(x, y):
                        sys.exit(0)
                    if btn_continue.collide(x,y)  :
                        break
                btn_quit.render(self.win)
                btn_continue.render(self.win)
                pygame.display.flip()
