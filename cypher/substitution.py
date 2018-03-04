"""
Copyright (c) Dave Flitney, 2018

Implementation of the Vigenere cypher
"""


class Vigenere:

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    alpha_table = []

    def __init__(self):
        """ Create a table of all the possible rotated alphabets """
        self.alpha_table = ["{0}{1}".format(self.alphabet[i:], self.alphabet[0:i]) for i in range(len(self.alphabet))]

    def encrypt(self, plain_text, key_word):
        """ Encrypt the text with the give key word """
        cypher_text = []
        for i, p in enumerate(list(plain_text)):
            key_letter = key_word[i % len(key_word)]
            e = self.alpha_table[self.alphabet.find(key_letter)][self.alphabet.find(p)]
            cypher_text.append(e)
        return "".join(cypher_text)

    def decrypt(self, cypher_text, key_word):
        """ Decrypt the text using the given key word """
        plain_text = []
        for i, e in enumerate(list(cypher_text)):
            key_letter = key_word[i % len(key_word)]
            p = self.alphabet[(self.alphabet.find(e) - self.alphabet.find(key_letter)) % len(self.alphabet)]
            plain_text.append(p)
        return "".join(plain_text)
