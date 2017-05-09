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
# music homemade module
import music
# time
import time
import glob
import sys

txt_intro = [
    "[Au téléphone] Hum... ....",
    "Qui es-tu?",
    "(Ton nom)? C'est ca?",
    "Tu dois sûrement te demander pourquoi je t'appelle et qui je suis mais ce dernier",
    "restera secret. On ne sait jamais.",
    "Pourquoi je t'appelle? Très bonne question. En fait, je vais t'expliquer:",
    "Un groupe mal attentionné a pris le contrôle d'un des plus grands ordinateurs du monde",
    "et compte s'en servir pour contrôler les cryptages donc les ordinateurs et les réseaux",
    "du monde entier afin de réduire le monde dans le chaos. Des codes cryptés malfaisants",
    "se trouvent un peu partout et notre seule solution est de trouver un expert en",
    "décryptage pour décoder et détruire ces codes. Et cette solution ... c'est toi. Nous",
    "avons entendu parler de tes prouesses en codage et nous sommes persuadés que tu es",
    "notre seul et unique espoir. Nous et le monde avons besoin de toi. Acceptes-tu de",
    "rejoindre cette aventure?",
    "",
    "Bien, je vais t'expliquer ce qui t'attend. Quatre types de codage sont possibles ici:",
    "le caesar, le vigenere, l'affine et le polybe. Chacun de ces codages te permettra de",
    "trouver un message codé. Tu trouveras, dans les différents endroits de ton périple,",
    "des indices ou des indications pour les trouver qui te seront données par des",
    "personnes, te permettant de t'aider dans la résolution de ton message codé. Donc parle",
    "aux personnes que tu croiseras sur ton chemin.",
    "Quand tu auras trouvé plusieurs indices, tu pourras atteindre un certain endroit où tu",
    "pourras dire et décrypter le message. Si tu te trompes, tu devras continuer à trouver",
    "d'autres indices, revenir au point de rendez-vous et trouver le code.",
    "As-tu tout bien compris?",
    "",
    "Très bien. Bon, il est temps que je te laisse dormir. Une grande aventure t'attend,",
    "demain. Nous te souhaitons bonne chance et n'oublie pas, le destin de notre monde",
    "repose entre tes mains..."
]
txt_affine = ["aaa"]
txt_caesar = ["bbb"]
txt_polybe = ["ccc"]
txt_vigenere = ["ddd"]

class Game:
    def __init__(self, win):
        self.running = False
        self.win = win
        self.player = Player()
        self.level = Level()
        self.beginning = time.time()
        self.font = pygame.font.SysFont("arial", 18)
        self.sounds = list(glob.glob("sounds/*.ogg"))
        self.csound = 0
        self.sound = music.sound(self.sounds[self.csound])
        self.indices_show = False

    def load(self):
        self.player = Player()
        self.level = Level()
        self.beginning = time.time()
        self.font = pygame.font.SysFont("arial", 18)
        self.sounds = list(glob.glob("sounds/*.ogg"))
        self.csound = 0
        self.sound = music.sound(self.sounds[self.csound])
        self.indices_show = False

        self.running = True
        # set the key repeat after 200ms of continuing keyboard input
        # repeated each 100ms
        pygame.key.set_repeat(200, 100)
        # load the player
        self.player.load()
        # load the level
        self.level.load()
        # play the music
        music.play(self.sound)

        # small loop to display the type of crypting
        btns = [
            Button(10, 10, WIDTH - 20, HEIGHT - 20, txt_intro, (128, 128, 128), self.font, (255, 255, 255)),
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
        if self.indices_show:
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
                    elif ev.key == K_e:
                        self.indices_show = not self.indices_show

            # if the player has found the secret message we quit the game
            if self.player.found and not self.player.dbox.rendering:
                break

            # update game values
            self.update()

            # render game objets
            self.render()
            self.win.blit(
                self.font.render(
                    str(pygame.mouse.get_pos()[0] // TILESIZE) + "," + str(pygame.mouse.get_pos()[1] // TILESIZE),
                    True, (0, 0, 0)), (pygame.mouse.get_pos()[0] + 20, pygame.mouse.get_pos()[1]))


            # flip the screen to display the modifications
            pygame.display.flip()

            # music
            if not music.is_playing():
                self.csound = (self.csound + 1) % len(self.sounds)
                self.sound = music.sound(self.sounds[self.csound])
                music.play(self.sound)

        if music.is_playing():
            music.stop(self.sound)
        self.sound = music.sound(self.sounds[-1])
        music.play(self.sound)

        # end
        if self.player.found:
            bulle = pygame.image.load("gfx/gui/bubble.png").convert_alpha()
            btn_quit = Button((WIDTH - 90) // 2 - 90, (HEIGHT - 20) // 2, 90, 20, "Quitter le jeu", (150, 20, 20), self.font, (255, 255, 255))
            btn_continue = Button((WIDTH - 70) // 2 + 90, (HEIGHT - 20) // 2, 70, 20, "Continuer", (20, 150, 20), self.font, (255, 255, 255))
            while True:
                ev = pygame.event.poll()
                if ev.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if btn_quit.collide(x, y):
                        sys.exit(0)
                    if btn_continue.collide(x, y):
                        break
                self.win.blit(bulle, (10, self.win.get_height() // 2 - bulle.get_height() // 2))
                btn_quit.render(self.win)
                btn_continue.render(self.win)
                pygame.display.flip()

        if music.is_playing():
            music.stop(self.sound)
