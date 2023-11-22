import unittest
from src.lab2.vigenre import *
import random
import string


class ViginereTestCase(unittest.TestCase):
    def test_encrypt(self): # тест корректной работы фунции шифрования encrypt_viginere()
        self.assertEqual(encrypt_vigenere("", "G"), '')
        self.assertEqual(encrypt_vigenere("ABC", "Bb"), 'BCD')
        self.assertEqual(encrypt_vigenere("abc", "bB"), 'bcd')
        self.assertEqual(encrypt_vigenere("w", "w"), 's')
        self.assertEqual(encrypt_vigenere("WOW", "Wa"), 'SOS')
        self.assertEqual(encrypt_vigenere("Vigenere cipher", "Python"), 'Kgzlbrgc vpdutp')

    def test_decrypt(self): # тест корректной работы фунции дешифрования decrypt_viginere()
        self.assertEqual(decrypt_vigenere("", "G"), '')
        self.assertEqual(decrypt_vigenere("BCD", "Bb"), 'ABC')
        self.assertEqual(decrypt_vigenere("bcd", "bB"), 'abc')
        self.assertEqual(decrypt_vigenere("s", "w"), 'w')
        self.assertEqual(decrypt_vigenere("SOS", "Wa"), 'WOW')
        self.assertEqual(decrypt_vigenere("Kgzlbrgc vpdutp", "Python"), 'Vigenere cipher')

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))

if __name__ == '__main__':
    unittest.main()
