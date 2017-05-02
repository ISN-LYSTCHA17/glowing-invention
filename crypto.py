# crypting and decrypting functions
# about caesar, vigenere, polybe and
# affine

def crypt(crypting_type, code, keys):
    # crypting_type is a string representing the kind of crypting method
    # code is also a string
    # keys is a list
    try:
        if crypting_type == "affine":
            return affine_crypt(code, keys[0], keys[1])
        elif crypting_type == "caesar":
            return caesar_crypt(code, keys[0])
        elif crypting_type == "vigenere":
            return vigenere_crypt(code, keys[0])
        elif crypting_type == "polybe":
            return polybe_crypt(code, keys[0])
        else:
            print("I do not know this crypting method")
            return code
    except Exception as e:
        print("Got an error when crypting, probably wrong keys")
        print(e)
        return code

def decrypt(crypting, code, keys):
    # crypting is a string representing the kind of scripting
    # code is the crypted message (string)
    # keys is a list
    try:
        if crypting == "affine":
            return affine_decrypt(code, keys[0], keys[1])
        elif crypting == "caesar":
            return caesar_decrypt(code, keys[0])
        elif crypting == "vigenere":
            return vigenere_decrypt(code, keys[0])
        elif crypting == "polybe":
            return polybe_decrypt(code, keys[0])
        else:
            print("I do not know this decrypting method")
            return code
    except Exception:
        print("Got an error when decrypting, probably wrong keys")
        return code


def affine_crypt(code, key, key2):
    code = code.lower()  # we turn the whole code into lowercase

    alphabet = list("abcdefghijklmnopqrstuvwxyz ")

    # an inline function to get easily access to the crypted character giving the index of
    # the character in the message
    # is strictly the equivalent of f: x |--> (ax + b)[27]
    get_character_index = lambda x: (key * x + key2) % len(alphabet)

    crypted = []

    for c in code:
        # we get the new character at alphabet[index]
        #   with index = get_character_index(x)
        #      with  x = the index of the character in the alphabet
        crypted.append(alphabet[get_character_index(alphabet.index(c))])

    return "".join(crypted)


def affine_decrypt(code, key, key2):
    decrypted = []
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")
    k = 0
    p_second = lambda _k: -(_k * key2) % len(alphabet)

    while (k * key) % len(alphabet) != 1:
        k += 1

    for c in code:
        decrypted.append(alphabet[(k * alphabet.index(c) + p_second(k)) % len(alphabet)])

    return "".join(decrypted)


def caesar_crypt(code, key):
    key = key.lower()  # we turn the whole key into lowercase, same with the code
    code = code.lower()

    crypted = []

    # we create a list containing the abc,
    # one element => one letter
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")

    # create the new abc regarding to the given key
    # example :
    # key = 'd'
    # crypted_abc = 'defghijklmnopqrstuvwxyz' + 'abc'
    # we cut the abc list where the key is and reassemble it
    crypted_abc = alphabet[alphabet.index(key):] + alphabet[:alphabet.index(key)]

    for c in code:
        # for each character in code
        # we add a character to crypted :
        #    which is located in crypted_abc at its index in the abc
        # example :
        # c = 'e'
        # its index in the abc is 4 (a is 0)
        # so we take the character in the crypted_abc at the index 4
        # if the key is 'd' as before, the new character will be 'h'
        crypted.append(crypted_abc[alphabet.index(c)])

    # we create a string from each character contained in the list named crypted
    return "".join(crypted)


def caesar_decrypt(code, key):
    decrypted = []

    alphabet = list("abcdefghijklmnopqrstuvwxyz ")

    # create the new abc regarding to the given key
    # example :
    # key = 'd'
    # crypted_abc = 'defghijklmnopqrstuvwxyz' + 'abc'
    # we cut the abc list where the key is and reassemble it
    crypted_abc = alphabet[alphabet.index(key):] + alphabet[:alphabet.index(key)]

    for c in code:
        decrypted.append(alphabet[crypted_abc.index(c)])

    return "".join(decrypted)


def vigenere_crypt(code, key):
    crypted = []
    key = key.lower()  # we turn the wholme key into lowercase, same with the code
    code = code.lower()

    # we create a list containing the abc,
    # one element => one letter
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")

    # we create the crypted abc as a list
    crypted_abc = []
    # we must reformat the key to eliminate the duplicated characters
    reformatted_key = []
    for c in key:
        # for each character in the key :D
        if c not in reformatted_key:
            # if the character is not in the reformatted_key list
            # we add it to the list
            reformatted_key.append(c)
    for c in reformatted_key:
        # we add the key to our new abc
        crypted_abc.append(c)
    for c in alphabet:
        # for each character in the abc
        if c not in crypted_abc:
            # if the character is not in the new abc, we add it to our crypted abc
            crypted_abc.append(c)

    for c in code:
        # for each character in code
        # we add a character to crypted :
        #    which is located in crypted_abc at its index in the abc
        crypted.append(crypted_abc[alphabet.index(c)])

    return "".join(crypted)


def vigenere_decrypt(code, key):
    decrypted = []

    # we create a list containing the abc,
    # one element => one letter
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")

    # we create the crypted abc as a list
    crypted_abc = []
    # we must reformat the key to eliminate the duplicated characters
    reformatted_key = []
    for c in key:
        # for each character in the key :D
        if c not in reformatted_key:
            # if the character is not in the reformatted_key list
            # we add it to the list
            reformatted_key.append(c)
    for c in reformatted_key:
        # we add the key to our new abc
        crypted_abc.append(c)
    for c in alphabet:
        # for each character in the abc
        if c not in crypted_abc:
            # if the character is not in the new abc, we add it to our crypted abc
            crypted_abc.append(c)

    for c in code:
        decrypted.append(alphabet[crypted_abc.index(c)])

    return "".join(decrypted)


def polybe_crypt(code, key):
    square = []

    for i in range(key):
        # we have 6 lines
        # we add an array representing a line
        square.append([])
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")
    index = 0
    # for each letter in the alphabet we place them in the array
    for c in alphabet:
        # if the size of the line is >= to 6 (ex if key = 6)
        if len(square[index]) > key - 1:
            index += 1
        square[index].append(c)
    crypted = []
    for c in code:
        for y, line in enumerate(square):
            for x, elem in enumerate(line):
                if elem.lower() == c:
                    crypted.append(str(x) + str(y))
                    break
    return "".join(crypted)


def polybe_decrypt(code, key):
    decrypted = []

    square = []

    for i in range(key):
        # we have 6 lines
        # we add an array representing a line
        square.append([])
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")
    index = 0
    # for each letter in the alphabet we place them in the array
    for c in alphabet:
        # if the size of the line is >= to 6 (ex if key = 6)
        if len(square[index]) > key - 1:
            index += 1
        square[index].append(c)

    couples = []
    for c in code:
        if not couples or len(couples[-1]) == 2:
            couples.append([int(c)])
        else:
            couples[-1].append(int(c))

    for cc in couples:
        decrypted.append(square[cc[1]][cc[0]])

    return "".join(decrypted)


# if we start the script directly, not when we import it
if __name__ == '__main__':
    # tests
    msg = "ceci est un test"

    print(msg)

    cc = caesar_crypt(msg, "e")
    vc = vigenere_crypt(msg, "vigenere")
    pc = polybe_crypt(msg, 7)
    ac = affine_crypt(msg, 2, 4)

    print("Crypting")
    print("Caesar", cc, sep="\n")
    print("Vigenere", vc, sep="\n")
    print("Polybe", pc, sep="\n")
    print("Affine", ac, sep="\n")

    dcc = caesar_decrypt(cc, "e")
    dvc = vigenere_decrypt(vc, "vigenere")
    dpc = polybe_decrypt(pc, 7)
    dac = affine_decrypt(ac, 2, 4)

    print("\nDecrypting")
    print("Caesar", dcc, sep="\n")
    print("Vigenere", dvc, sep="\n")
    print("Polybe", dpc, sep="\n")
    print("Affine", dac, sep="\n")
