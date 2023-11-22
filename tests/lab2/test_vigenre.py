import unittest
from src.lab2.vigenre import *


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

if __name__ == '__main__':
    unittest.main()
