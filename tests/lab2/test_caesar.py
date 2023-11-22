import unittest
from src.lab2.caesar import *

class CaesarTestCase(unittest.TestCase):
    def test_encrypt(self): # тест работы функции шифрования encrypt_caesar()
        self.assertEqual(encrypt_caesar(""), '')
        self.assertEqual(encrypt_caesar("XYZ"), 'ABC')
        self.assertEqual(encrypt_caesar("xyz"), 'abc')
        self.assertEqual(encrypt_caesar("Aa, K - Onh! F:@ $%^*/2."), 'Dd, N - Rqk! I:@ $%^*/2.')
        self.assertEqual(encrypt_caesar("По-русски не понимаю!"), 'По-русски не понимаю!')

    def  test_decrypt(self): # тест работы функции дешифрования decrypt_caesar()
        self.assertEqual(decrypt_caesar(""), '')
        self.assertEqual(decrypt_caesar("ABC"), 'XYZ')
        self.assertEqual(decrypt_caesar("abc"), 'xyz')
        self.assertEqual(decrypt_caesar("Dd, N - Rqk! I:@ $%^*/2."), 'Aa, K - Onh! F:@ $%^*/2.')
        self.assertEqual(decrypt_caesar("По-русски всё ещё не понимаю!"), 'По-русски всё ещё не понимаю!')



if __name__ == '__main__':
    unittest.main()