from ciphers import Caeser_Cipher
import random


cipher_dictionary: dict = {
    "Caeser_Cipher": [
        "Moonlight",
        "Claw",
        "Serendipity",
        "Fury",
        "Gale",
        "Zealot",
        "Aura",
        "Cryptic",
        "Ridge",
        "Flare",
    ],
    "Viginere_Cipher": [
        "Eclipse",
        "Fox",
        "Labyrinth",
        "Surge",
        "Whisper",
        "Oblivion",
        "Arc",
        "Phantom",
        "Bolt",
        "Radiance",
    ],
    "Playfair_Cipher": [
        "Zen",
        "Monolith",
        "Pyre",
        "Harmonic",
        "Trace",
        "Vapor",
        "Saber",
        "Dream",
        "Majestic",
        "Echoes",
    ],
    "Beaufort_Cipher": [
        "Titan",
        "Chimera",
        "Glint",
        "Spectacle",
        "Frost",
        "Wisp",
        "Horizon",
        "Shift",
        "Ripple",
        "Crescent",
    ],
    "Railefence_Cipher": [
        "Lynx",
        "Radiant",
        "Orb",
        "Excalibur",
        "Waves",
        "Flame",
        "Surreal",
        "Nest",
        "Conflux",
        "Silver",
    ],
    "ColumnarTransposition_Cipher": [
        "Ivory",
        "Basilisk",
        "Obsidian",
        "Flare",
        "Vault",
        "Crimson",
        "Void",
        "Nexus",
        "Sentinel",
        "Talon",
    ],
    "Affine_Cipher": [
        "Glyph",
        "Fragment",
        "Swan",
        "Shadow",
        "Bliss",
        "Torque",
        "Omni",
        "Archer",
        "Veil",
        "Sierra",
    ],
    "Autokey_Cipher": [
        "Stark",
        "Midnight",
        "Quartz",
        "Haven",
        "Infernal",
        "Wave",
        "Aegis",
        "Noble",
        "Shroud",
        "Twilight",
    ],
    "RunningKey_Cipher": [
        "Tempest",
        "Ray",
        "Paradox",
        "Blaze",
        "Cipher",
        "Glimpse",
        "Scribe",
        "Rune",
        "Nebula",
        "Arcane",
    ],
    "KeyWord_Cipher": [
        "Valor",
        "Cascade",
        "Volt",
        "Bane",
        "Epoch",
        "Sable",
        "Warden",
        "Breeze",
        "Epochal",
        "Zion",
    ],
}


def random_key() -> tuple:

    cipher_name = random.choice(list(cipher_dictionary.keys()))
    key = random.choice(cipher_dictionary[cipher_name])

    return (cipher_name, key)


def main():
    while True:
        print(
            "What do you want to do?\n1. Encrypt\n2. Decrypt\n3. Exit\n---------------------------------------------------"
        )

        choice: int = int(input("Please enter your choice: "))

        if choice == 1:
            text: str = str(input("Enter your text: "))

            key = random.choice(list(cipher_dictionary["Caeser_Cipher"]))

            encrypted_text = Caeser_Cipher.encrypt(text=text, key=key)

            print(key, text, encrypted_text)

        elif choice == 2:
            text: str = str(input("Enter your text: "))

            key: str = str(input("Enter your key: "))

            decrypted_text = Caeser_Cipher.decrypt(text, key)

            print(decrypted_text)

        elif choice == 3:

            return

        else:
            print("Invalid choice!!")


if __name__ == "__main__":
    main()
