import crypto
import random
from constants import *


messages = [
    "ceci est un test",
    "voici un message crypte",
    "bonjour a tous je suis un message",
    "un petit message a transporter",
    "bienvenue a tous chez moi",
    "mon ordinateur n est pas assez puissant",
    "les avions font vroom vroom",
    "vient prendre un cafe avec nous"
]

words = [
    "vigenere",
    "clef",
    "code",
    "niveau",
    "cryptcrush",
    "atom",
    "python",
    "programmation"
]


def ri():
    return random.randint(0, 26)


crypting_method = {
    "affine": [[1, ri()], [3, ri()], [5, ri()], [7, ri()], [9, ri()], [11, ri()], [15, ri()], [17, ri()], [19, ri()], [21, ri()], [23, ri()]],
    "caesar": [chr(i) for i in range(97, 123)],
    "vigenere": words,
    "polybe": [i for i in range(6, 18)]
}


def choose_crypting_and_message():
    return random.choice(messages), random.choice(list(crypting_method.keys()))


class Message:
    def __init__(self):
        self.__msg, self.crypting_meth = choose_crypting_and_message()
        self.crypted = ""
        self.crypting_keys = random.choice(crypting_method[self.crypting_meth])
        if not isinstance(self.crypting_keys, list):
            self.crypting_keys = [self.crypting_keys]
        self.indices_sent = 0

    def start(self):
        self.crypted = crypto.crypt(self.crypting_meth, self.__msg, self.crypting_keys)

    def get_indice(self):
        if self.indices_sent == 2:
            self.indices_sent = 3
            if self.do_we_need_two_indices():
                return {'end': "Tu as les indices, maintenant trouve le point final pour décrypter"}
            else:
                return {'key2': self.crypting_keys[1]}
        elif self.indices_sent == 1:
            self.indices_sent = 2
            return {'crypting': self.crypting_meth}
        elif self.indices_sent == 0:
            self.indices_sent = 1
            return {'key': self.crypting_keys[0]}

    def do_we_need_two_indices(self):
        if self.crypting_meth == "affine":
            return False
        else:
            return True

    def decrypt(self, indices):
        if "crypting" in indices.keys() and "key" in crypting.keys() and ("key2" in crypting.keys() or "end" in crypting.keys()):
            keys = [crypting["key"]]
            if "key2" in crypting.keys():
                keys.append(crypting["key2"])
            if crypto.decrypt(indices["crypting"], keys) == self.__msg:
                return DECRYPT_OK
            return DECRYPT_FAILED
        return DECRYPT_NOT_ENOUGH_INDICES


class Indice:
    def __init__(self, content):
        self.content = content
