import pytest

from rsa_pasaforte import utility


@pytest.mark.parametrize('numeral, boolean', [
    (11, True),
    (24, False),
    (17, True)
])
def test_is_a_prime_number(numeral, boolean):
    assert utility.is_a_prime_number(numeral) == boolean


def test_generate_prime_numbers():
    assert len(utility.generate_prime_numbers()) == 2


@pytest.mark.parametrize('operands, answer', [
    ((0, 7), (7, 0, 1)),
    ((11, 13), (1, 6, -5)),
    ((17, 19), (1, 9, -8))
])
def test_extended_euclidean_algorithm_gcd(operands, answer):
    assert utility.extended_euclidean_algorithm_gcd(*operands) == answer


@pytest.mark.parametrize('operands, multiplicative_inverse', [
    ((5, 7), 3),
    ((11, 13), 6),
    ((17, 19), 9)
])
def test_modular_multiplicative_inverse(operands, multiplicative_inverse):
    assert utility.modular_multiplicative_inverse(*operands) == multiplicative_inverse


@pytest.mark.parametrize('operands, boolean', [
    ((5, 7), True),
    ((10, 20), False),
    ((17, 19), True),
])
def test_are_coprime(operands, boolean):
    assert utility.are_coprime(*operands) == boolean


def test_generate_keys():
    assert len(utility.generate_keys()) == 2
