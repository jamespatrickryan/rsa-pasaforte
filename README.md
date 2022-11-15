# RSA (Rivest-Shamir-Adleman) public-key cryptosystem algorithm

This is a Python [RSA asymmetric cryptography algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) uploaded on an autonomous instance of the package index ([TestPyPI](https://test.pypi.org/project/rsa-pasaforte/)) deliberated for probation. ![Tests](https://github.com/jamespatrickryan/rsa-pasaforte/actions/workflows/tests.yml/badge.svg)

## How-Tos

### Precursive

Execute the `venv` module as a script to initiate a [virtual environment](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a,part%20of%20your%20operating%20system.):

```bash
$ python -m venv venv
```

Activate it:

```bash
$ source venv/Scripts/activate
```

Install the package:

```bash
(venv)
$ pip install -i https://test.pypi.org/simple/ rsa-pasaforte
```

And invoke the Python Interactive Interpreter:

```bash
(venv)
$ python
```

## Usage or Demonstration

`import` it:

```python
>>> from rsa_pasaforte import utility, main
```

Employ the `generate_keys()` function within the `utility` module and *tuple*-unpack or destructure it.

Its return value type hint is:

```python
Tuple[Tuple[int, int], Tuple[int, int]]
```

```python
>>> public_key, private_key = utility.generate_keys()
```

The `encryption` key is public and distinct from the `decryption` key (held undisclosed).

```python
public_key: Tuple[int, int]
private_key: Tuple[int, int]
```

Initialize the `plaintext` variable with a string literal of your preference.

```python
>>> plaintext = 'Python'
```

Toss the `plaintext` and `public_key` as arguments of the `main` module’s `encrypt()` subroutine.

```python
ciphertext: Iterable[int]
```

```python
>>> ciphertext = main.encrypt(plaintext, public_key)
>>> print(*ciphertext)
3606640 4172688 6583515 3193439 436542 872288
```

To crack the `ciphertext`, hand it over with the `private_key` as arguments of the `decrypt()` subroutine.

```python
>>> plaintext = main.decrypt(ciphertext, private_key)
>>> print(plaintext)
Python
```
