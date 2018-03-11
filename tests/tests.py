from cipher.substitution import Vigenere, Caesar

import unittest


class TestCaesar(unittest.TestCase):

    def setUp(self):
        self.csr = Caesar()

    def test_encode(self):
        decrypted_text = "ABCDEFG"
        encrypted_text = self.csr.encrypt(decrypted_text)
        self.assertEqual(encrypted_text, "NOPQRST")

    def test_decode(self):
        cipher_text = "NOPQRST"
        decrypted_text = self.csr.decrypt(cipher_text)
        self.assertEqual(decrypted_text, "ABCDEFG")

    def test_caesar5(self):
        caesar5 = Caesar(offset=5)
        encrypted_text = caesar5.encrypt("ABCDEFG")
        self.assertEqual(encrypted_text, "FGHIJKL")
        decrypted_text = caesar5.decrypt(encrypted_text)
        self.assertEqual(decrypted_text, "ABCDEFG")

    def test_example(self):
        decrypted_text = "NOW IS THE WINTER OF OUR DISCONTENT"
        encrypted_text = self.csr.encrypt(decrypted_text)
        self.assertEqual(encrypted_text, " AIMVEMFURMIV FRDMASMAGDMQVEPA FR F")

    def test_custom_alphabet(self):
        caesar5 = Caesar(offset=5, alphabet="THEQUICKBROWNFXJMPSVLAZYDG ")
        encrypted_text = caesar5.encrypt("ABCDEFG")
        self.assertEqual(encrypted_text, " FWEKSQ")



class TestVigenere(unittest.TestCase):

    def setUp(self):
        self.vig = Vigenere()

    def test_encode(self):
        key = "WOMBAT"
        decrypted_text = "NOW IS THE WINTER OF OUR DISCONTENT"
        encrypted_text = self.vig.encrypt(decrypted_text, key)
        self.assertEqual(encrypted_text, "IBHAIKVGTF ODAEFRSJTLPUJVRUTCGIGQOT")

    def test_decode(self):
        key = "WOMBAT"
        encrypted_text = "IBHAIKVGTF ODAEFRSJTLPUJVRUTCGIGQOT"
        decrypted_text = self.vig.decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, "NOW IS THE WINTER OF OUR DISCONTENT")

    def test_encode(self):
        key = "CORAL"
        decrypted_text = "WE ARE DISCOVERED STOP FLEA AT ONCE STOP"
        encrypted_text = self.vig.encrypt(decrypted_text, key)
        self.assertEqual(encrypted_text, "YSQABGNUICEBLEBGRQSDQCQFWGOQADBBDCPBFJO ")

    def test_decode(self):
        key = "CORAL"
        encrypted_text = "YSQABGNUICEBLEBGRQSDQCQFWGOQADBBDCPBFJO "
        decrypted_text = self.vig.decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, "WE ARE DISCOVERED STOP FLEA AT ONCE STOP")

    def test_example(self):
        key = "MYPASSWORD"
        decrypted_text = "THIS IS MY SECRET TEXT"
        encrypted_text = self.vig.encrypt(decrypted_text, key)
        self.assertEqual(encrypted_text, "EEXSR NNCALPTCIWONJHIQ")

