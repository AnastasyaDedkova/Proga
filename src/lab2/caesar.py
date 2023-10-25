# import doctest
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    Args:
        plaintext (str): text to be encrypted
        shift (int): encryption shift

    Returns:
        ciphertext (str): text that has been encrypted

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if (ord(i) >= 65 and ord(i) < 88) or (ord(i) >= 97 and ord(i) < 120):
            ciphertext += chr(ord(i) + shift)
        elif (ord(i) >= 88 and ord(i) < 91) or (ord(i) >= 120 and ord(i) < 123):
            ciphertext += chr(ord(i) - shift - 20)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    Args:
        ciphertext (srt): text to be decrypted
        shift (int): decryption shift

    Returns:
        plaintext (str): text that has been decrypted

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if (ord(i) >= 68 and ord(i) < 91) or (ord(i) >= 100 and ord(i) < 123):
            plaintext += chr(ord(i) - shift)
        elif (ord(i) >= 65 and ord(i) < 68) or (ord(i) >= 97 and ord(i) < 100):
            plaintext += chr(ord(i) + shift + 20)
        else:
            plaintext += i

    return plaintext


# doctest.testmod()
