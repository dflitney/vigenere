from cypher.substitution import Vigenere, Caesar

import unittest


class TestCaesar(unittest.TestCase):

    def setUp(self):
        self.csr = Caesar(offset=12)

    def test_encode(self):
        plain_text = "ABCDEFG"
        encoded_text = self.csr.encrypt(plain_text)
        self.assertEqual(encoded_text, "MNOPQRS")

    def test_decode(self):
        cipher_text = "MNOPQRS"
        plain_text = self.csr.decrypt(cipher_text)
        self.assertEqual(plain_text, "ABCDEFG")

    def test_example(self):
        plain_text = "NOW IS THE WINTER OF OUR DISCONTENT"
        encoded_text = self.csr.encrypt(plain_text)
        self.assertEqual(encoded_text, "Z HLUDLETQLHUZEQCL RL FCLPUDO ZEQZE")


class TestVigenere(unittest.TestCase):

    def setUp(self):
        self.vig = Vigenere()

    def test_encode(self):
        key = "WOMBAT"
        plain_text = "NOW IS THE WINTER OF OUR DISCONTENT"
        encoded_text = self.vig.encrypt(plain_text, key)
        self.assertEqual(encoded_text, "IBHAIKVGTF ODAEFRSJTLPUJVRUTCGIGQOT")

    def test_decode(self):
        key = "WOMBAT"
        encoded_text = "IBHAIKVGTF ODAEFRSJTLPUJVRUTCGIGQOT"
        plain_text = self.vig.decrypt(encoded_text, key)
        self.assertEqual(plain_text, "NOW IS THE WINTER OF OUR DISCONTENT")

    def test_example(self):
        key = "MYPASSWORD"
        plain_text = "THIS IS MY SECRET TEXT"
        encoded_text = self.vig.encrypt(plain_text, key)
        self.assertEqual(encoded_text, "EEXSR NNCALPTCIWONJHIQ")


if __name__ == '__main__':
    unittest.main()
