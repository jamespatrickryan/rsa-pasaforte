from typing import Tuple, Iterable


ALPHABET: str = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!?,'


def modular_exponentiation(
        base: int, exponent: int,
        modulus: int) -> int:
    """This procedure is exponentiation
    (right-to-left binary method)
    conducted on top of a modulus."""

    if modulus == 1:
        return 0

    result: int = 1
    base %= modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result
                      * base
                      % modulus)
        base = (base ** 2) % modulus
        exponent >>= 1

    return result


def rsa(key: Tuple[int, int],
        numeral: int) -> int:
    return modular_exponentiation(numeral, *key)


def character_to_index(character: str) -> int:
    """This function returns the index of a
    character delineated in the alphabet."""

    return ALPHABET.index(character)


def plaintext_to_indices(
        plaintext: Iterable[str]) -> Iterable[int]:
    """This function invokes and executes
    the character-to-index subroutine per
    element in an iterable (string)."""

    return list(map(character_to_index, plaintext))


def encrypt(plaintext: Iterable[str],
            public_key: Tuple[int, int]) -> Iterable[int]:
    """This function calculates the ciphertext of a conveyed
    plaintext (character) depicted as an integer."""

    indices: Iterable[int] = plaintext_to_indices(plaintext)

    return list(rsa(public_key, index)
                for index in indices)


def ciphertext_to_indices(
        ciphertext: Iterable[int],
        private_key: Tuple[int, int]) -> Iterable[int]:
    """This function traverses the
    ciphertext, invokes RSA, and
    recasts it into an index."""

    return list(rsa(private_key, integer)
                for integer in ciphertext)


def to_character(index: int) -> str:
    """This function fetches a character from the
    alphabet through the provisioned index."""

    return ALPHABET[index]


def decrypt(ciphertext: Iterable[int],
            private_key: Tuple[int, int]) -> str:
    indices: Iterable[int] = ciphertext_to_indices(ciphertext, private_key)

    return ''.join(map(to_character, indices))
