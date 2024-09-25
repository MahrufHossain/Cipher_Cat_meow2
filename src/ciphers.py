from abc import abstractmethod, ABC

class Cipher(ABC):
    """This is an abstract class to build the cipher classes."""

    @abstractmethod
    def encrypt(self, text : str, key: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, text: str, key: str) -> str:
        pass



class Caeser_Cipher(Cipher):

    def encrypt(text: str, key: str) -> str:
        
        encrypted : str = ""

        shift : int = len(key)

        for char in text:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                encrypted += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            else:
                encrypted += char
        return encrypted
    
    def decrypt(text: str, key: str) -> str:
        decrypted : str = ""

        shift : int = len(key)

        for char in text:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)

            else:
                decrypted += char

        return decrypted





