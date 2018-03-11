"""
Copyright (c) Dave Flitney, 2018

Cipher playground
"""

class Cipher:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    def __init__(self, *args, **kwargs):
        if "alphabet" in kwargs:
            self.alphabet=kwargs["alphabet"]

    def encrypt(self):
        raise NotImplemented

    def decrypt(self):
        raise NotImplemented


class Caesar(Cipher):

    def __init__(self, *args, **kwargs):
        super(Caesar, self).__init__(*args, **kwargs)
        i = int(kwargs.get("offset", "13"))
        self.rot_alphabet = "".join([ section for section in [ self.alphabet[i:], self.alphabet[0:i] ] ])

    def encrypt(self, plain_text):
        cipher_text = [ self.rot_alphabet[self.alphabet.find(p)] for p in list(plain_text) ]
        return "".join(cipher_text)

    def decrypt(self, cipher_text):
        plain_text = [ self.alphabet[self.rot_alphabet.find(e)] for e in list(cipher_text)]
        return "".join(plain_text)


class Vigenere(Cipher):

    alpha_table = []

    def __init__(self, *args, **kwargs):
        """ Create a table of all the possible rotated alphabets """
        super(Vigenere, self).__init__(*args, **kwargs)

    def encrypt(self, plain_text, key_word):
        """ Encrypt the text with the give key word """
        cipher_text = []
        for i, p in enumerate(list(plain_text)):
            key_letter = key_word[i % len(key_word)]
            e = self.alphabet[(self.alphabet.find(key_letter) + self.alphabet.find(p)) % len(self.alphabet)]
            cipher_text.append(e)
        return "".join(cipher_text)

    def decrypt(self, cipher_text, key_word):
        """ Decrypt the text using the given key word """
        plain_text = []
        for i, e in enumerate(list(cipher_text)):
            key_letter = key_word[i % len(key_word)]
            p = self.alphabet[(self.alphabet.find(e) - self.alphabet.find(key_letter)) % len(self.alphabet)]
            plain_text.append(p)
        return "".join(plain_text)
