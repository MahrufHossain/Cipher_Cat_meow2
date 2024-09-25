"""This is a file for unittest the ciphers code."""
import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from typing import Any
import unittest

from ciphers import Caeser_Cipher

class TestCiphers(unittest.TestCase):
    def test_caeser_cipher(self):
        self.assertEqual(Caeser_Cipher.encrypt(text="Hello World", key="Sky"), "Khoor Zruog")
        self.assertEqual(Caeser_Cipher.decrypt(text="Khoor Zruog", key="Sky"), "Hello World")



if __name__ == "__main__":
    unittest.main()