# drawing lib
import pygame
# game core
from game import Game
# game menu
from menu import Menu
# character personnalization interface
from personnalize import Personnalize
# import game constants
from constants import *


def start():
    print("Starting game")
    pygame.init()  # start the graphic engine

    # create a window
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    # create all components such as the game, the menu and the personnalization interface
    game = Game(win)
    menu = Menu(win)
    personnalize = Personnalize(win)

    # checking the return of the menu
    result = MENU_UNDEFINED
    while result != MENU_QUIT:  # the menu.run() return MENU_QUIT(2) to exit
        # we must reload it each time to reset its variables
        menu.load()
        result = menu.run()  # we get the result of the run

        # if the menu returned MENU_GAME(0), it means that the player wants to
        # start the game
        if result == MENU_GAME:
            # load and run component
            game.load()
            game.run()
        # if the menu returned MENU_PERSONNALIZE(1), it means that the player
        # wants to create his/her own character
        elif result == MENU_PERSONNALIZE:
            # load and run component
            personnalize.load()
            personnalize.run()

    # free all pygame components (=quit pygame)
    pygame.quit()
    print("Quitting")


# if we start this file directly, __name__ will be set to '__main__'
# so we start the game globally
if __name__ == '__main__':
    start()
