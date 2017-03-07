# crypting and decrypting functions
# about caesar, vigenere and polybe


def caesar_crypt(code, key):
    key = key.lower()  # we turn the wholme key into lowercase, same with the code
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
    pass


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
    pass


def polybe_crypt(code):
    pass


def polybe_decrypt(code):
    pass


# if we start the script directly, not when we import it
if __name__ == '__main__':
    # tests
    msg = "ceci est un test"
    
    print("Caesar", caesar_crypt(msg, "e"), sep="\n")
    print("Vigenere", vigenere_crypt(msg, "vigenere"), sep="\n")



