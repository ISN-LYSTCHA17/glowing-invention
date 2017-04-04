# import drawing lib
import pygame
# game constants
from constants import *
# lib to list all the files in a specified directory
# using a specified pattern
import glob
# quests
import quests
# lights effects
import light


class Level:
    def __init__(self):
        # initialisation of the level
        self.data = []
        self.tiles = []
        # default values, not loaded ones
        self.solid_blocs = [0, 1, 2]
        # indices
        self.indices = []
        # end point
        self.endpoint = []
        # graphics effects
        self.lights = []

    def load_level(self, path):
        # load a level with the path given

        # we open the level at "path" in reading mode ("r")
        # and we put its data in a var named file
        with open(path, "r") as file:
            # we read all the lines of the file
            # which each one will be put in a list
            temp = file.read()
            self.data = eval(temp)["level"]
            self.indices = eval(temp)["indices"]
            self.endpoint = eval(temp)["endpoint"]
            tlights = eval(temp)["lights"]
            for e in tlights:
                self.lights.append(light.PreRenderedLight(*e))
                self.lights[-1].load()

    def load(self):
        # load the level
        self.load_level("levels/level1")
        # for each file listed in the list returned by the glob function
        # of the glob module. the glob function is applied to the directory
        # where the tiles are located to list all its blocs (aka tiles)
        #   here we use sorted(..) on glob.glob(..) to re-order all the files in alphabetical order
        for file in sorted(glob.glob("gfx/tiles/*.png")):
            # load an image using pygame image module
            img = pygame.image.load(file)
            img.convert_alpha()
            # we append an element to the sprites' list (here an image loaded before)
            self.tiles.append(img)

    def collide(self, x, y):
        # we get the bloc in (x, y) required by the player
        try:
            bloc = self.data[y][x]
        except IndexError:
            # we catch an IndexError, meaning that the previous statement throw an error
            # here it is because the y or the x are outside the level
            return COLLIDING
        # checking if we are on the end point
        if [x, y] == self.endpoint:
            return GOTENDPOINT
        # checking if we got some indice
        if [x, y] in self.indices:
            return GOTINDICE
        # we check if the bloc is in the list of the solid blocs
        # if it is, we return True otherwise False :)
        if bloc in self.solid_blocs:
            return COLLIDING
        else:
            return NOTCOLLIDING

    def remove_indice(self, x, y):
        if [x, y] in self.indices:
            self.indices.pop(self.indices.index([x, y]))

    def render(self, win):
        pygame.draw.rect(win, (120, 205, 245), (0, 0) + win.get_size())
        # rendering tiles
        y = 0
        for line in self.data:
            x = 0
            for elem in line:
                bloc_id = elem
                # print the tile to the screen
                win.blit(self.tiles[bloc_id], [x * TILESIZE, y * TILESIZE])
                x += 1
            y += 1
        for rendered_light in self.lights:
            rendered_light.blit(win)


# just to test if everything is correct ; kind of quick n' dirty
if __name__ == '__main__':
    import pygame as p ; p.init()
    w, le = p.display.set_mode((WIDTH, HEIGHT)), Level() ; le.load()
    while p.event.poll().type != p.QUIT:
        le.render(w) ; p.display.flip()
    p.quit()
