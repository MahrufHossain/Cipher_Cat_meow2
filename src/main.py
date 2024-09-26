from ciphers import *
import random
import time

cipher_dictionary: dict = {
    "Caesar_Cipher": [
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
    "Vigenere_Cipher": [
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
    "RailFence_Cipher": [
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
    "Keyword_Cipher": [
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
    cipher_name, key = random_key()
    if cipher_name == "Caesar_Cipher":
        cipher = Caesar_Cipher()

    elif cipher_name == "Vigenere_Cipher":
        cipher = Vigenere_Cipher()
    elif cipher_name == "Playfair_Cipher":
        cipher = Playfair_Cipher()
    elif cipher_name == "Beaufort_Cipher":
        cipher = Beaufort_Cipher()
    elif cipher_name == "RailFence_Cipher":
        cipher = RailFence_Cipher()
    elif cipher_name == "ColumnarTransposition_Cipher":
        cipher = ColumnarTransposition_Cipher()
    elif cipher_name == "Affine_Cipher":
        cipher = Affine_Cipher()
    elif cipher_name == "Autokey_Cipher":
        cipher = Autokey_Cipher()
    elif cipher_name == "RunningKey_Cipher":
        cipher = RunningKey_Cipher()
    elif cipher_name == "Keyword_Cipher":
        cipher = Keyword_Cipher()

    while True:
        print(
            "---------------------------------------------------\nWhat do you want to do?\n1. Encrypt\n2. Decrypt\n3. Exit\n---------------------------------------------------"
        )

        try:
            choice: int = int(input("Please enter your choice: "))

            if choice == 1:
                text: str = str(
                    input(
                        "---------------------------------------------------\nEnter your text:\t"
                    )
                )

                key = random.choice(list(cipher_dictionary[cipher_name]))
                encrypted_text = cipher.encrypt(text=text, key=key)
                print("---------------------------------------------------")
                print(f"Your Encrypted Text:\t{encrypted_text}.\t\tYour Key:\t{key}")

            elif choice == 2:
                text: str = str(
                    input(
                        "---------------------------------------------------\nEnter your text:\t"
                    )
                )

                key: str = str(
                    input(
                        "---------------------------------------------------\nEnter your key: "
                    )
                )

                decrypted_text = cipher.decrypt(text, key)
                print("---------------------------------------------------")
                print(f"Your Decrypted Text:\t{decrypted_text}")

            elif choice == 3:
                print("---------------------------------------------------\nExiting")
                time.sleep(2)
                return

            else:
                print("Invalid choice!!")

        except ValueError:
            print("\nInter an integer.")
            continue


if __name__ == "__main__":
    main()
