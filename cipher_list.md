# Ciphers


## Caeser Cipher
 - Type: Substitution cipher.
 - How it Works: Typically, the Caesar Cipher shifts the alphabet by a certain number of positions. When using a word as a key, the letters of the key determine how much each letter of the plaintext is shifted.
 - Example: With the key "WORD", each letter in the plaintext is shifted by the corresponding letter's position in the alphabet (W=23, O=15, R=18, D=4).

## Vigenere Cipher
 - Type: Polyalphabetic substitution cipher.
 - How it Works: Uses a keyword to shift the letters of the plaintext. The keyword is repeated until it matches the length of the message, and each letter in the plaintext is shifted by the position of the corresponding letter in the keyword.
 - Example: If the plaintext is "HELLO" and the key is "KEY", the key is repeated to "KEYKE". The first letter "H" is shifted by the position of "K" (10th letter), the second letter "E" by "E" (5th letter), and so on.

## Playfair Cipher
 - Type: Digraph substitution cipher.
 - How it Works: Uses a keyword to generate a 5x5 grid of letters (with I and J combined). Pairs of plaintext letters are encrypted by referencing their positions in the grid.
 - Example: With a key "MONARCHY", you generate a grid and encrypt pairs of letters by swapping them based on their position.

## Beaufort Cipher
 - Type: Polyalphabetic substitution cipher.
 - How it Works: Similar to the Vigenère cipher but works in reverse, using a word as a key. Instead of shifting the plaintext by the key’s position, you find the key letter in the cipher alphabet and use the plaintext letter’s position to determine the ciphertext.
 - Example: If the plaintext is "HELLO" and the key is "KEY", the encryption process works backward compared to Vigenère.
## Rail Fence Cipher
 - Type: Transposition cipher.
 - How it Works: Normally, the Rail Fence Cipher arranges the plaintext in a zigzag pattern on rails and then reads it row by row. When using a keyword, you can scramble the letters based on the key to add extra complexity.
 - Example: The key can be used to determine the order in which rows are read, providing more flexibility and security than the basic Rail Fence Cipher.

## Columnar Transposition Cipher
 - Type: Transposition cipher.
 - How it Works: Uses a keyword to write the plaintext into a grid with a number of columns equal to the length of the keyword. The columns are then rearranged according to the alphabetical order of the keyword’s letters.
 - Example: If the keyword is "CAT", you write the plaintext into three columns and then rearrange the columns in the order C-A-T (2nd, 1st, 3rd) before reading off the ciphertext.

## Affine Cipher
 - Type: Substitution cipher.
 - How it Works: Uses a mathematical function to transform each letter of the plaintext. With a key, you define the function that determines how letters are substituted.
 - Example: If the key is a word, you convert the word into numeric values to apply transformations.

## Autokey Cipher
 - Type: Polyalphabetic substitution cipher.
 - How it Works: Similar to the Vigenère Cipher but uses the plaintext itself as part of the key after the initial keyword. This increases the strength of the cipher as the key grows with the message.
 - Example: Start with a keyword like "SECRET", then after encrypting the first few characters, use the plaintext as part of the key for the rest.

## Running Key Cipher
-- Type: Polyalphabetic substitution cipher.
 - How it Works: Uses a key that is typically a long piece of text (like a passage from a book) for encryption. The key text is combined with the plaintext to encrypt the message.
 - Example: If your key is "Alice in Wonderland" and your plaintext is "HELLO", you match each letter of the plaintext with the corresponding letter from the key text to encrypt.
 
## Keyword Cipher
 - Type: Simple substitution cipher.
 - How it Works: The alphabet is shifted according to a keyword. The letters of the keyword are placed at the start of the alphabet, and the remaining letters follow in alphabetical order, excluding any already used in the keyword.
 - Example: With a keyword like "KEYWORD", the alphabet would become "KEYWORDABC...".