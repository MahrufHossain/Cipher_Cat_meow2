"""This is a file for unittest the ciphers code."""

import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from typing import Any
import unittest

from ciphers import *


class TestCiphers(unittest.TestCase):

    def test_caesar_cipher(self):
        self.assertEqual(Caesar_Cipher.encrypt("Hello World", 3), "Khoor Zruog")
        self.assertEqual(Caesar_Cipher.decrypt("Udymts", 5), "Python")

    def test_vigenere_cipher(self):
        self.assertEqual(
            Vigenere_Cipher.encrypt("Hello World", "Elephant"), "Lzjdm Xjffq"
        )
        self.assertEqual(
            Vigenere_Cipher.decrypt("Lqwxfr we Qwrw", "LEMON"), "Attack at Dawn"
        )

    def test_play_fair_cipher(self):
        self.assertEqual(Playfair_Cipher.encrypt("Hello World"), "Svool Dliow")
        self.assertEqual(Playfair_Cipher.decrypt("Kbgslm"), "Python")

    def test_rail_fence_cipher(self):
        self.assertEqual(RaileFence_Cipher.encrypt("Hello World", 3), "Hoo l!lWd")
        self.assertEqual(RaileFence_Cipher.decrypt("Ti tsshi aet", 2), "This is a test")

    def test_beaufort_cipher(self):
        self.assertEqual(Beaufort_Cipher.encrypt("Hello World", "Lion"), "Lkcb Iwqlo")
        self.assertEqual(
            Beaufort_Cipher.decrypt("Tafc Aatwxe", "Cipher"), "Attack at Dawn"
        )

    def test_affine_cipher(self):
        self.assertEqual(Affine_Cipher.encrypt("Hello World"), "2351131514323445")
        self.assertEqual(Affine_Cipher.decrypt("53423144"), "Python")

    def test_running_key_cipher(self):
        self.assertEqual(RunningKey_Cipher.encrypt("Hello World", 5, 8), "Qtaad Btyfa")
        self.assertEqual(
            RunningKey_Cipher.decrypt("Ewdvfn ev Xamj", 3, 1), "Attack at Dawn"
        )

    def test_autokey_cipher(self):
        self.assertEqual(Autokey_Cipher.encrypt("Hello World"), "BABAA ABBAA")
        self.assertEqual(Autokey_Cipher.decrypt("BAABA"), "Python")

    def test_keyWord_Cipher(self):
        self.assertEqual(
            KeyWord_Cipher.encrypt("Hello World", "qwertyuiopasdfghjklzxcvbnm"),
            "Wnngz Dvgun",
        )
        self.assertEqual(
            KeyWord_Cipher.decrypt("Attack", "abcdefghijklmnopqrstuvwxyz"),
            "Attack",
        )

    def test_columnar_transposition_cipher(self):
        self.assertEqual(
            ColumnarTransposition_Cipher.encrypt("Hello World", "HACK"), "Woedllor H"
        )
        self.assertEqual(
            ColumnarTransposition_Cipher.decrypt("h t esisit", "KEY"), "This is a test"
        )


if __name__ == "__main__":
    unittest.main()
