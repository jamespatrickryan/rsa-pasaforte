from typing import TypeAlias, Tuple, List
import math
import random


Keys: TypeAlias = Tuple[Tuple[int, int], Tuple[int, int]]


def is_a_prime_number(numeral: int) -> bool:
    limit: int = int(math.sqrt(numeral) + 1)

    divisor: int
    for divisor in range(2, limit):
        if numeral % divisor == 0:
            return False
    else:
        return True


def generate_prime_numbers() -> Tuple[int, ...]:
    maximum: int = 10_000
    prime_numbers: List[int] = [2]

    numeral: int
    for numeral in range(3, maximum, 2):
        if is_a_prime_number(numeral):
            prime_numbers.append(numeral)

    return tuple(random.choices(prime_numbers, k=2))


def extended_euclidean_algorithm_gcd(
        a: int, b: int) -> Tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    else:
        gcd: int
        x: int
        y: int
        gcd, x, y = extended_euclidean_algorithm_gcd(b % a, a)

        z: int = (y
                  - (b // a)
                  * x)

        return gcd, z, x


def modular_multiplicative_inverse(
        a: int, m: int) -> int:
    z: int
    _, z, _ = extended_euclidean_algorithm_gcd(a, m)

    return (z % m + m) % m


def are_coprime(a: int, b: int) -> bool:
    gcd: int = extended_euclidean_algorithm_gcd(a, b)[0]

    return gcd == 1


def generate_keys() -> Keys:
    p: int
    q: int
    p, q = generate_prime_numbers()
    n: int = p * q
    # Euler’s totient function
    phi: int = (p - 1) * (q - 1)

    while True:
        numeral: int = random.randint(2, phi - 1)
        if are_coprime(numeral, phi):
            e: int = numeral
            break
    d: int = modular_multiplicative_inverse(e, phi)

    return (e, n), (d, n)
