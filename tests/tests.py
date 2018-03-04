from cypher.substitution import Vigenere

import unittest


class TestStringMethods(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
