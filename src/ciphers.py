from abc import abstractmethod, ABC
import math


class Cipher(ABC):
    """This is an abstract class to build the cipher classes."""

    @abstractmethod
    def encrypt(self, text: str, key: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, text: str, key: str) -> str:
        pass


class Caesar_Cipher(Cipher):

    def encrypt(self, text: str, key: str) -> str:

        encrypted: str = ""
        key = key.upper()
        shift: int = len(key)
        for char in text.upper():
            if char.isalpha():
                shift_amount = 65
                encrypted += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            else:
                encrypted += char
        return encrypted

    def decrypt(self, text: str, key: str) -> str:
        decrypted: str = ""
        key = key.upper()
        shift: int = len(key)

        for char in text.upper():
            if char.isalpha():
                shift_amount = 65
                decrypted += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)

            else:
                decrypted += char

        return decrypted


class Vigenere_Cipher(Cipher):

    def encrypt(self, text: str, key: str) -> str:
        ciphertext = []
        key = key.upper()
        key_length = len(key)

        for i, letter in enumerate(text.upper()):
            if letter.isalpha():
                # Shift based on the key
                shift = ord(key[i % key_length]) - ord("A")
                encrypted_letter = chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
                ciphertext.append(encrypted_letter)
            else:
                ciphertext.append(letter)

        return "".join(ciphertext)

    def decrypt(self, text: str, key: str) -> str:
        plaintext = []
        key = key.upper()
        key_length = len(key)

        for i, letter in enumerate(text.upper()):
            if letter.isalpha():
                # Reverse the shift based on the key
                shift = ord(key[i % key_length]) - ord("A")
                decrypted_letter = chr(
                    (ord(letter) - ord("A") - shift + 26) % 26 + ord("A")
                )
                plaintext.append(decrypted_letter)
            else:
                plaintext.append(letter)

        return "".join(plaintext)


class Playfair_Cipher:
    def __init__(self):
        self.matrix = []

    def generate_matrix(self, key: str):
        # Prepare key by removing duplicates and merging with the alphabet
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key = key.upper().replace("J", "I")  # Convert to uppercase and replace J with I
        key = "".join(sorted(set(key), key=key.index))  # Remove duplicates in order
        used = set(key)

        # Create matrix by adding unused characters from the alphabet
        full_key = key + "".join([char for char in alphabet if char not in used])
        self.matrix = [full_key[i : i + 5] for i in range(0, 25, 5)]

    def format_text(self, text: str):
        # Prepare the text: remove spaces, replace J with I, and add padding X where necessary
        text = text.upper().replace("J", "I").replace(" ", "")
        formatted = ""
        i = 0
        while i < len(text):
            formatted += text[i]
            if i + 1 < len(text) and text[i] == text[i + 1]:
                formatted += "X"  # Add padding X if two letters are the same
                i += 1
            elif i + 1 < len(text):
                formatted += text[i + 1]
                i += 2
            else:
                i += 1
        if len(formatted) % 2 != 0:
            formatted += "X"  # Add padding X if text length is odd
        return formatted

    def find_position(self, char):
        # Find the row and column of a character in the matrix
        for row in range(5):
            for col in range(5):
                if self.matrix[row][col] == char:
                    return row, col
        return None

    def encrypt(self, text: str, key: str) -> str:
        self.generate_matrix(key)
        text = self.format_text(text)
        encrypted_text = ""

        for i in range(0, len(text), 2):
            row1, col1 = self.find_position(text[i])
            row2, col2 = self.find_position(text[i + 1])

            # Same row, shift right
            if row1 == row2:
                encrypted_text += self.matrix[row1][(col1 + 1) % 5]
                encrypted_text += self.matrix[row2][(col2 + 1) % 5]
            # Same column, shift down
            elif col1 == col2:
                encrypted_text += self.matrix[(row1 + 1) % 5][col1]
                encrypted_text += self.matrix[(row2 + 1) % 5][col2]
            # Rectangle case, swap columns
            else:
                encrypted_text += self.matrix[row1][col2]
                encrypted_text += self.matrix[row2][col1]

        return encrypted_text

    def decrypt(self, text: str, key: str) -> str:
        self.generate_matrix(key)
        decrypted_text = ""

        for i in range(0, len(text), 2):
            row1, col1 = self.find_position(text[i])
            row2, col2 = self.find_position(text[i + 1])

            # Same row, shift left
            if row1 == row2:
                decrypted_text += self.matrix[row1][(col1 - 1) % 5]
                decrypted_text += self.matrix[row2][(col2 - 1) % 5]
            # Same column, shift up
            elif col1 == col2:
                decrypted_text += self.matrix[(row1 - 1) % 5][col1]
                decrypted_text += self.matrix[(row2 - 1) % 5][col2]
            # Rectangle case, swap columns
            else:
                decrypted_text += self.matrix[row1][col2]
                decrypted_text += self.matrix[row2][col1]

        return decrypted_text


class Beaufort_Cipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def char_to_index(self, char):
        """Converts a character to its corresponding index in the alphabet."""
        return self.alphabet.index(char)

    def index_to_char(self, index):
        """Converts an index back to its corresponding character in the alphabet."""
        return self.alphabet[index % 26]

    def format_key(self, text, key):
        """Repeats or truncates the key to match the length of the text."""
        key = key.upper().replace(" ", "")
        if len(key) < len(text):
            key = (key * (len(text) // len(key))) + key[: len(text) % len(key)]
        return key.upper()

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt the text using the Beaufort cipher. (Same process for decryption)"""
        text = text.upper().replace(" ", "")  # Remove spaces and convert to uppercase
        key = self.format_key(text, key)  # Adjust the key to match the text length
        encrypted_text = ""

        for i in range(len(text)):
            if "A" <= text[i] <= "Z":
                text_index = self.char_to_index(text[i])
                key_index = self.char_to_index(key[i])
                # Beaufort Cipher uses modular subtraction
                encrypted_char = self.index_to_char((key_index - text_index) % 26)
                encrypted_text += encrypted_char
            else:
                encrypted_text += text[i]  # Non-alphabet characters remain unchanged

        return encrypted_text

    def decrypt(self, text: str, key: str) -> str:
        """Decrypt the text using the Beaufort cipher. (Same process as encryption)"""
        # Beaufort cipher is reciprocal, so encryption and decryption are the same
        return self.encrypt(text, key)


class RailFence_Cipher:
    def encrypt(self, text: str, key: str) -> str:
        """Encrypts text using the Rail Fence Cipher with the number of rails determined by the length of the key."""
        num_rails = len(key)  # Use the length of the key as the number of rails
        rail = [""] * num_rails
        direction_down = False  # To control the direction (zigzag pattern)
        row = 0  # Start from the top rail

        # Remove spaces from the text and convert to uppercase
        text = text.replace(" ", "").upper()

        for char in text:
            rail[row] += char  # Place character in the current row
            # Change direction at the top or bottom rail
            if row == 0 or row == num_rails - 1:
                direction_down = not direction_down
            # Move to the next row
            row += 1 if direction_down else -1

        # Combine the rows to form the ciphertext
        encrypted_text = "".join(rail)
        return encrypted_text

    def decrypt(self, text: str, key: str) -> str:
        """Decrypts text using the Rail Fence Cipher with the number of rails determined by the length of the key."""
        num_rails = len(key)  # Use the length of the key as the number of rails
        rail = [
            ["\n"] * len(text) for _ in range(num_rails)
        ]  # Create a grid for the zigzag pattern
        direction_down = None
        row, col = 0, 0

        # Mark the positions in the grid where the text characters will go
        for i in range(len(text)):
            if row == 0:
                direction_down = True
            if row == num_rails - 1:
                direction_down = False
            rail[row][col] = "*"
            col += 1
            row += 1 if direction_down else -1

        # Now fill the characters into the marked positions
        index = 0
        for i in range(num_rails):
            for j in range(len(text)):
                if rail[i][j] == "*" and index < len(text):
                    rail[i][j] = text[index]
                    index += 1

        # Read the grid in a zigzag pattern to reconstruct the original text
        decrypted_text = []
        row, col = 0, 0
        for i in range(len(text)):
            if row == 0:
                direction_down = True
            if row == num_rails - 1:
                direction_down = False
            if rail[row][col] != "\n":
                decrypted_text.append(rail[row][col])
                col += 1
            row += 1 if direction_down else -1

        return "".join(decrypted_text)


class ColumnarTransposition_Cipher:
    def __init__(self):
        pass

    def _create_empty_matrix(self, rows, cols):
        """Helper function to create an empty matrix for encryption and decryption."""
        return [[""] * cols for _ in range(rows)]

    def _sort_key(self, key: str):
        """Returns a list of positions for the columns sorted by the key."""
        return sorted(range(len(key)), key=lambda k: key[k])

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt the text using Columnar Transposition Cipher."""
        text = text.replace(" ", "")  # Remove spaces from the text
        num_cols = len(key)  # Number of columns determined by the key length
        num_rows = -(
            -len(text) // num_cols
        )  # Calculate the number of rows (ceiling division)

        # Create the grid for the transposition
        matrix = self._create_empty_matrix(num_rows, num_cols)

        # Fill the matrix row by row
        index = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if index < len(text):
                    matrix[r][c] = text[index]
                    index += 1

        # Sort the columns by the key order
        sorted_key_indices = self._sort_key(key)

        # Read the columns in the order determined by the key
        encrypted_text = ""
        for c in sorted_key_indices:
            for r in range(num_rows):
                if matrix[r][c] != "":
                    encrypted_text += matrix[r][c]

        return encrypted_text

    def decrypt(self, text: str, key: str) -> str:
        """Decrypt the text using Columnar Transposition Cipher."""
        num_cols = len(key)  # Number of columns is the length of the key
        num_rows = -(
            -len(text) // num_cols
        )  # Calculate the number of rows (ceiling division)

        # Sort the columns by the key order
        sorted_key_indices = self._sort_key(key)

        # Create the grid to place the ciphertext characters
        matrix = self._create_empty_matrix(num_rows, num_cols)

        # Fill the matrix column by column in the order determined by the sorted key
        index = 0
        for c in sorted_key_indices:
            for r in range(num_rows):
                if index < len(text):
                    matrix[r][c] = text[index]
                    index += 1

        # Read the matrix row by row to retrieve the plaintext
        decrypted_text = ""
        for r in range(num_rows):
            for c in range(num_cols):
                if matrix[r][c] != "":
                    decrypted_text += matrix[r][c]

        return decrypted_text


class Affine_Cipher:
    def __init__(self):
        self.alphabet_size = 26

    def _mod_inverse(self, a, m):
        """Find the modular inverse of a under modulo m."""
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError(f"No modular inverse for {a} under modulo {m}")

    def _adjust_a(self, a):
        """Adjust 'a' so that it's coprime with 26."""
        while math.gcd(a, self.alphabet_size) != 1:
            a += 1
        return a

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt the text using Affine Cipher with word length as key."""
        a = len(key)  # Use the length of the key (word) as 'a'
        b = ord(key[0].upper()) - ord("A")  # Use first letter of the key as 'b'

        a = self._adjust_a(a)  # Ensure 'a' is coprime with 26
        encrypted_text = ""

        for char in text.upper():
            if char.isalpha():
                x = ord(char) - ord("A")
                # Affine encryption formula: (a * x + b) % 26
                encrypted_char = (a * x + b) % self.alphabet_size
                encrypted_text += chr(encrypted_char + ord("A"))
            else:
                encrypted_text += char  # Non-alphabet characters remain unchanged

        return encrypted_text

    def decrypt(self, text: str, key: str) -> str:
        """Decrypt the text using Affine Cipher with word length as key."""
        a = len(key)  # Use the length of the key (word) as 'a'
        b = ord(key[0].upper()) - ord("A")  # Use first letter of the key as 'b'

        a = self._adjust_a(a)  # Ensure 'a' is coprime with 26
        a_inv = self._mod_inverse(a, self.alphabet_size)  # Find modular inverse of 'a'
        decrypted_text = ""

        for char in text.upper():
            if char.isalpha():
                y = ord(char) - ord("A")
                # Affine decryption formula: a_inv * (y - b) % 26
                decrypted_char = a_inv * (y - b) % self.alphabet_size
                decrypted_text += chr(decrypted_char + ord("A"))
            else:
                decrypted_text += char  # Non-alphabet characters remain unchanged

        return decrypted_text


class Autokey_Cipher:
    def __init__(self):
        self.alphabet_size = 26

    def _format_text(self, text):
        """Format the text to uppercase and remove spaces."""
        return "".join(text.split()).upper()

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt the text using the Autokey cipher."""
        text = self._format_text(text)
        key = self._format_text(key)

        # Use the length of the key as the initial part of the key
        key_length = len(key)
        full_key = key + text  # Form the full key by appending the plaintext

        encrypted_text = ""

        for i in range(len(text)):
            if text[i].isalpha():
                text_index = ord(text[i]) - ord("A")
                key_index = ord(full_key[i]) - ord("A")
                # Autokey encryption formula: (text_index + key_index) % 26
                encrypted_char = (text_index + key_index) % self.alphabet_size
                encrypted_text += chr(encrypted_char + ord("A"))
            else:
                encrypted_text += text[i]  # Non-alphabet characters remain unchanged

        return encrypted_text

    def decrypt(self, text: str, key: str) -> str:
        """Decrypt the text using the Autokey cipher."""
        text = self._format_text(text)
        key = self._format_text(key)

        # Use the length of the key as the initial part of the key
        key_length = len(key)
        full_key = list(key)  # Start with the keyword

        decrypted_text = ""

        for i in range(len(text)):
            if text[i].isalpha():
                text_index = ord(text[i]) - ord("A")
                key_index = ord(full_key[i]) - ord("A")
                # Autokey decryption formula: (text_index - key_index + 26) % 26
                decrypted_char = (
                    text_index - key_index + self.alphabet_size
                ) % self.alphabet_size
                decrypted_text += chr(decrypted_char + ord("A"))

                # Extend the key with the decrypted character
                full_key.append(chr(decrypted_char + ord("A")))
            else:
                decrypted_text += text[i]  # Non-alphabet characters remain unchanged

        return decrypted_text


class RunningKey_Cipher:
    def __init__(self):
        self.alphabet_size = 26

    def _format_text(self, text):
        """Format the text to uppercase and remove spaces."""
        return "".join(text.split()).upper()

    def _extend_key(self, text, key):
        """Extend the key to match the length of the text using a repeated key."""
        key_length = len(key)
        extended_key = (key * (len(text) // key_length)) + key[: len(text) % key_length]
        return extended_key

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt the text using Running Key cipher."""
        text = self._format_text(text)
        key = self._format_text(key)

        # Extend the key to match the length of the text
        extended_key = self._extend_key(text, key)

        encrypted_text = ""

        for i in range(len(text)):
            if text[i].isalpha():
                text_index = ord(text[i]) - ord("A")
                key_index = ord(extended_key[i]) - ord("A")
                # Running Key encryption formula: (text_index + key_index) % 26
                encrypted_char = (text_index + key_index) % self.alphabet_size
                encrypted_text += chr(encrypted_char + ord("A"))
            else:
                encrypted_text += text[i]  # Non-alphabet characters remain unchanged

        return encrypted_text

    def decrypt(self, text: str, key: str) -> str:
        """Decrypt the text using Running Key cipher."""
        text = self._format_text(text)
        key = self._format_text(key)

        # Extend the key to match the length of the text
        extended_key = self._extend_key(text, key)

        decrypted_text = ""

        for i in range(len(text)):
            if text[i].isalpha():
                text_index = ord(text[i]) - ord("A")
                key_index = ord(extended_key[i]) - ord("A")
                # Running Key decryption formula: (text_index - key_index + 26) % 26
                decrypted_char = (
                    text_index - key_index + self.alphabet_size
                ) % self.alphabet_size
                decrypted_text += chr(decrypted_char + ord("A"))
            else:
                decrypted_text += text[i]  # Non-alphabet characters remain unchanged

        return decrypted_text


class Keyword_Cipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def _create_cipher_alphabet(self, key: str):
        """Create the cipher alphabet based on the keyword."""
        key = "".join(
            sorted(set(key), key=key.index)
        )  # Remove duplicates but keep order
        cipher_alphabet = key.upper()

        # Append remaining letters of the alphabet that are not in the keyword
        for char in self.alphabet:
            if char not in cipher_alphabet:
                cipher_alphabet += char

        return cipher_alphabet

    def encrypt(self, text: str, key: str) -> str:
        """Encrypt the text using the Keyword Cipher."""
        cipher_alphabet = self._create_cipher_alphabet(key)
        encrypted_text = ""

        for char in text.upper():
            if char.isalpha():
                # Find the index of the character in the standard alphabet and use the cipher alphabet
                index = self.alphabet.index(char)
                encrypted_text += cipher_alphabet[index]
            else:
                encrypted_text += char  # Keep non-alphabet characters unchanged

        return encrypted_text

    def decrypt(self, text: str, key: str) -> str:
        """Decrypt the text using the Keyword Cipher."""
        cipher_alphabet = self._create_cipher_alphabet(key)
        decrypted_text = ""

        for char in text.upper():
            if char.isalpha():
                # Find the index of the character in the cipher alphabet and use the standard alphabet
                index = cipher_alphabet.index(char)
                decrypted_text += self.alphabet[index]
            else:
                decrypted_text += char  # Keep non-alphabet characters unchanged

        return decrypted_text
