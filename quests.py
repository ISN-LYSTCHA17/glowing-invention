import crypto
import random
from constants import *


messages = [
    "ceci est un test",
    "voici un message crypte",
    "bonjour a tous je suis un message",
    "un petit message a transporter",
    "bienvenue à tous chez moi"
]

crypting_method = [
    "affine",
    "caesar",
    "vigenere",
    "polybe"
]


def choose_crypting_and_message():
    return random.choice(messages), random.choise(crypting_method)


class Message:
    def __init__(self):
        self.__msg, self.crypting_meth = choose_crypting_and_message()
        self.crypted = ""

    def start(self):
        self.crypted = crypto.crypt(self.__msg, self.crypting_meth)

    def decrypt(self, indices):
        if "crypting" in indices.keys() and "keys" in crypting.keys():
            if crypto.decrypt(indices["crypting"], indices["keys"]) == self.__msg:
                return DECRYPT_OK
            return DECRYPT_FAILED
        return DECRYPT_NOT_ENOUGH_INDICES


class Indice:
    def __init__(self, content):
        self.content = content
