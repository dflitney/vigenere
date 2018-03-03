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


def main():
    """ Example program to demonstrate usage for the Vigenere class """

    import argparse

    parser = argparse.ArgumentParser(description="Encrypt/decrypt messages using Vigenere cypher method.")
    parser.add_argument("--key", "-k", action="store", default="CORAL", help="The Vigenere cypher key.")
    parser.add_argument("--encrypt", "-E", action="store_true", help="Encrypt message", default=False)
    parser.add_argument("--decrypt", "-D", action="store_true", help="Decrypt message", default=False)
    parser.add_argument("--verbose", "-V", action="store_true", default=False,
                        help="Additional output - handy for debugging!")
    parser.add_argument("--plain-text-file", "-p", action="store", default=None,
                        help="Path to a file containing the plain text message.")

    args = parser.parse_args()

    if not args.encrypt and not args.decrypt:
        print("You MUST select one of encrypt/decrypt.")

    if args.plain_text_file:
        with open(args.plain_text_file, 'r') as f:
            text = f.read().strip().upper()
    else:
        text = input("Enter your message text: ")

    vigenere = Vigenere()

    if args.verbose:
        print(text)

    if args.encrypt:
        encrypted = vigenere.encrypt(text, args.key)
        print(encrypted)
        if args.verbose:
            print(vigenere.decrypt(encrypted, args.key))

    if args.decrypt:
        decrypted = vigenere.decrypt(text, args.key)
        print(decrypted)
        if args.verbose:
            print(vigenere.encrypt(decrypted, args.key))


if __name__ == "__main__":
    main()
