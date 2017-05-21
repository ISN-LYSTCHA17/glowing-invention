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
# textentry
import textentry as txe

def split(t, c):
    w = []
    i = 0

    for e in t:
        if not w or len(w[-1]) == c:
            w.append([e])
        else:
            w[-1].append(e)

    nw = []
    for e in w:
        nw.append("".join(e))

    return nw


class Player:
    def __init__(self):
        # position is handle in a list of 2 elements (x, y)
        self.pos = [32, 32]
        # speed in pixel per move
        self.speed = TILESIZE // 2
        # the direction which the character is facing
        self.orientation = DOWN
        # all the images for the character located in gfx/player
        self.sprites = []
        # where we are going to store our indices
        self.indices = {}
        # the message
        self.message = quests.Message()
        self.dbox = dialogbox.DialogBox("", _type="_me")
        self.onendpoint = False
        self.found = False

    def load(self):
        # for each file listed in the list returned by the glob function
        # of the glob module. the glob function is applied to the directory
        # where the character is located to list all its images (aka sprites)
        for file in ["back", "front", "left", "right"]:
            # load an image using pygame image module
            img = pygame.image.load("gfx/player/" + file + ".png")
            img.convert_alpha()
            # we append an element to the sprites' list (here an image loaded before)
            self.sprites.append(img)
        # start crypting
        self.message.start()

        n = split(self.message.crypted, 128)
        n.insert(0, "Le message crypté est :")
        self.dbox.set_text(n)
        self.dbox.trigger()

    def move(self, direction, level, win):
        # only allow the player to move if we don't have all the indices
        # and if we are not on the point to decrypt the message
        if not self.onendpoint or len(self.indices) != 3:
            # copy its position in two new variables x and y
            x = self.pos[0]
            y = self.pos[1]
            # we change the orientation of the character for the new one
            self.orientation = direction

            # we create temporary position to do the tests
            new_pos_x = x
            new_pos_y = y

            def check_colliding(_x, _y):
                tests = [
                    level.collide(_x // TILESIZE    , _y // TILESIZE    ),
                    level.collide(_x // TILESIZE + 1, _y // TILESIZE    ),
                    level.collide(_x // TILESIZE    , _y // TILESIZE + 1),
                    level.collide(_x // TILESIZE + 1, _y // TILESIZE + 1)
                ]
                tests = [t for t in tests if t != NOTCOLLIDING]
                if tests == []:
                    # everything was NOTCOLLIDING
                    return NOTCOLLIDING
                if len(tests) > 1:
                    # we have more than one special value, let's return the highest one
                    tests = sorted(tests)
                    return tests[-1]
                else:
                    # len(tests) == 1
                    return tests[0]

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
                indice = None  # default value for the following tests
                # we remove the indice to avoid taking it multiple times, and
                # by the same time we check if there was one (just to be sure enough)
                if level.remove_indice(new_pos_x // TILESIZE, new_pos_y // TILESIZE):
                    # take an indice
                    indice = self.message.get_indice()
                if indice:
                    self.indices.update(indice)
                    try:
                        self.dbox.set_text(["Vous avez trouvé un indice :", "{} -> {}".format(*list(*indice.items()))])
                    except IndexError:
                        pass
                    else:
                        if not self.dbox.rendering:
                            self.dbox.trigger()
            elif collision == GOTENDPOINT:
                # the player must try to guess the real message
                if len(self.indices) == 3:
                    self.onendpoint = True

            # we affect the new pos to the player position on the screen
            self.pos = [x, y]
        else:
            # let's trigger a new dialog box to ask the player to guess the message
            nte = txe.TextBox(win, max_length=len(self.message.crypted) + 2, y=64, x=32, sx=WIDTH - 64, placeholder="Devine le message")
            text = nte.get_text()
            self.found = self.message.decrypt(self.indices, text) == DECRYPT_OK
            m = "Vous avez trouvé le message" if self.found else "Le message n'est pas correct"
            if self.found:
                self.dbox.set_text([m, "{}".format(self.message.get_clear())])
            else:
                self.dbox.set_text(m)
            if not self.dbox.rendering:
                self.dbox.trigger()

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
