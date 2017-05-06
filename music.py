import pygame


def sound(fp):
    return pygame.mixer.Sound(fp)


def play(snd):
    snd.play()


def stop(snd):
    snd.stop()


def is_playing():
    return pygame.mixer.get_busy()
