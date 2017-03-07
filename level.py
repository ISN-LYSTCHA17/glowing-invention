# import drawing lib
import pygame
# game constants
from constants import *
# lib to list all the files in a specified directory
# using a specified pattern
import glob


class Level:
    def __init__(self):
        # initialisation of the level
        self.data = []
        self.tiles = []
        # default values, not loaded ones
        self.solid_blocs = [0, 1, 2]
    
    def load_level(self, path):
        # load a level with the path given
        
        # we open the level at "path" in reading mode ("r")
        # and we put its data in a var named file
        with open(path, "r") as file:
            # we read all the lines of the file
            # which each one will be put in a list
            lines = file.readlines()
            # for each line in the read lines
            for a_line in lines:
                yn = []
                # for each character in the line
                for c in a_line:
                    # we check if the read character is a number
                    if c.isdigit():
                        yn.append(int(c))
                # we append the converted line to the level
                self.data.append(yn)
    
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
        bloc = self.data[y][x]
        # we check if the bloc is in the list of the solid blocs
        # if it is, we return True otherwise False :)
        if bloc in self.solid_blocs:
            return True
        else:
            return False
    
    def render(self, win):
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


if __name__ == '__main__':
    pygame.init()
    w = pygame.display.set_mode((WIDTH, HEIGHT))
    le = Level()
    le.load()
    while pygame.event.poll().type != pygame.QUIT:
        le.render(w)
        pygame.display.flip()
    pygame.quit()