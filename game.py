# pygame constants, such as the events' code
from pygame.locals import *
# game constants
from constants import *


class Game:
    def __init__(self, win):
        self.running = False
        self.win = win

    def load(self):
        self.running = True
        # set the key repeat after 200ms of continuing keyboard input
        # repeated each 100ms
        pygame.key.set_repeat(200, 100)

    def update(self):
        # game updating method
        pass

    def render(self):
        # game rendering method
        pass

    def run(self):
        # main game loop
        while self.running:
            # events' dispatching loop
            for ev in pygame.event.get():
                # handle quit event
                if ev.type == QUIT:
                    self.running = False

            # update game values
            self.update()

            # render game objets
            self.render()

            # flip the screen to display the modifications
            pygame.display.flip()
