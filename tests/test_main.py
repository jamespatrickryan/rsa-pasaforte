import pytest

from rsa_pasaforte import main


@pytest.mark.parametrize('operands, result', [
    ((5, 10, 1), 0),
    ((15, 25, 10), 5),
    ((8, 10, 12), 4)
])
def test_modular_exponentiation(operands, result):
    assert main.modular_exponentiation(*operands) == result


@pytest.mark.parametrize('operands, modular_exponentiation', [
    ((5, 10, 1), 0),
    ((15, 25, 10), 5),
    ((8, 10, 12), 4)
])
def test_rsa(operands, modular_exponentiation):
    key = operands[1:]
    numeral = operands[0]
    assert main.rsa(key, numeral) == modular_exponentiation


@pytest.mark.parametrize('character, index', [
    ('j', 9),
    ('u', 20),
    ('r', 17)
])
def test_character_to_index(character, index):
    assert main.character_to_index(character) == index


@pytest.mark.parametrize('plaintext, indices', [
    ('James', [36, 0, 12, 4, 18]),
    ('Patrick', [42, 0, 19, 17, 8, 2, 10]),
    ('Ryan', [44, 24, 0, 13])
])
def test_plaintext_to_indices(plaintext, indices):
    assert main.plaintext_to_indices(plaintext) == indices


@pytest.mark.parametrize('plaintext, ciphertext', [
    ('James', [73490, 0, 124167, 1790, 187304]),
    ('Patrick', [56667, 0, 209320, 221646, 139951, 160441, 103467]),
    ('Ryan', [260434, 187819, 0, 154541])
])
def test_encrypt(plaintext, ciphertext):
    assert main.encrypt(plaintext, (166999, 293807)) == ciphertext


@pytest.mark.parametrize('ciphertext, indices', [
    ([73490, 0, 124167, 1790, 187304],
     [36, 0, 12, 4, 18]),
    ([56667, 0, 209320, 221646, 139951, 160441, 103467],
     [42, 0, 19, 17, 8, 2, 10]),
    ([260434, 187819, 0, 154541],
     [44, 24, 0, 13])
])
def test_ciphertext_to_indices(ciphertext, indices):
    assert main.ciphertext_to_indices(ciphertext, (4591, 293807)) == indices


@pytest.mark.parametrize('index, character', [
    (9, 'j'),
    (20, 'u'),
    (17, 'r')
])
def test_to_character(index, character):
    assert main.to_character(index) == character


@pytest.mark.parametrize('ciphertext, plaintext', [
    ([73490, 0, 124167, 1790, 187304],
     'James'),
    ([56667, 0, 209320, 221646, 139951, 160441, 103467],
     'Patrick'),
    ([260434, 187819, 0, 154541],
     'Ryan')
])
def test_decrypt(ciphertext, plaintext):
    assert main.decrypt(ciphertext, (4591, 293807)) == plaintext
