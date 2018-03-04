#!/usr/bin/env python
from cypher.substitution import Vigenere


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
        exit(-1)

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
