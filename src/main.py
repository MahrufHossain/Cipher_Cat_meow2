from ciphers import *
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


def main():
    cipher_name = random.choice(list(cipher_dictionary.keys()))
    key = random.choice(cipher_dictionary[cipher_name])

    print(cipher_name, key)


if __name__ == "__main__":
    main()
