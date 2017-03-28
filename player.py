# import drawing lib
import pygame
# game constants
from constants import *
# lib to list all the files in a specified directory
# using a specified pattern
import glob
# import quests management and all that stuff
import quests
# dialog box
import dialogbox


class Player:
    def __init__(self):
        # position is handle in a list of 2 elements (x, y)
        self.pos = [0, 0]
        # speed in pixel per move
        self.speed = 4
        # the direction which the character is facing
        self.orientation = DOWN
        # all the images for the character located in gfx/player
        self.sprites = []
        # where we are going to store our indices
        self.indices = {}
        # the message
        self.message = quests.Message()
        self.dbox = dialogbox.DialogBox("")

    def load(self):
        # for each file listed in the list returned by the glob function
        # of the glob module. the glob function is applied to the directory
        # where the character is located to list all its images (aka sprites)
        for file in glob.glob("gfx/player/*.png"):
            # load an image using pygame image module
            img = pygame.image.load(file)
            img.convert_alpha()
            # we append an element to the sprites' list (here an image loaded before)
            self.sprites.append(img)
        # start crypting
        self.message.start()

    def move(self, direction, level):
        # copy its position in two new variables x and y
        x = self.pos[0]
        y = self.pos[1]
        # we change the orientation of the character for the new one
        self.orientation = direction

        # we create temporary position to do the tests
        new_pos_x = x
        new_pos_y = y

        def check_colliding(x, y):
            return level.collide(x // TILESIZE    , y // TILESIZE    ) or \
                   level.collide(x // TILESIZE + 1, y // TILESIZE    ) or \
                   level.collide(x // TILESIZE    , y // TILESIZE + 1) or \
                   level.collide(x // TILESIZE + 1, y // TILESIZE + 1)

        if direction == UP:
            # we go up, we take off the speed to move up the player on the screen
            new_pos_y -= self.speed
        elif direction == DOWN:
            new_pos_y += self.speed
        elif direction == RIGHT:
            new_pos_x += self.speed
        elif direction == LEFT:
            new_pos_x -= self.speed

        # we check the collision. | True if colliding, otherwise False
        #                         | we take the bloc in x divid by the size of a bloc, same in y
        collision = check_colliding(new_pos_x, new_pos_y)
        # if the bloc is NOT colliding
        # we apply the new pos
        if collision != COLLIDING:
            x = new_pos_x
            y = new_pos_y
        if collision == GOTINDICE:
            # take an indice
            indice = self.message.get_indice()
            self.indices.update(indice)
            self.dbox.set_text(["Vous avez trouvé un indice :", "{} -> {}".format(*list(*indice.items()))])
            self.dbox.trigger()
            # we remove the indice to avoid taking it multiple times
            level.remove_indice(new_pos_x // TILESIZE, new_pos_y // TILESIZE)
        if collision == GOTENDPOINT:
            # the player must try to guess the real message
            pass

        # we affect the new pos to the player position on the screen
        self.pos = [x, y]

    def stop_dialogs(self):
        if self.dbox.rendering:
            self.dbox.trigger()

    def render(self, win):
        # we are given a reference to the window,
        # with which we can blit (display an image) on
        # specifying a position
        win.blit(self.sprites[self.orientation], self.pos)
        # we render the dialog box of our player
        self.dbox.render(win)

    def update(self):
        # update animations and all that stuff (or not)
        pass
