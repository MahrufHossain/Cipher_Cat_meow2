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

    pass


