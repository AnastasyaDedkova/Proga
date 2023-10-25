def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    Args:
        plaintext (str): text to be encrypted
        keyword (str): word to be used for encryption

    Returns:
        ciphertext (str): text that has been encrypted
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keylen = len(keyword)
    key = keyword.upper()
    i = 0
    for j in plaintext:
        if not j.isalpha():
            ciphertext += j
        else:
            if j.isupper():
                a = "A"
            else:
                a = "a"
            ciphertext += chr(ord(a) + ((ord(j) - ord(a)) + (ord(key[i]) - ord("A"))) % 26)
            i += 1
            if i == keylen:
                i = 0
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    Args:
        ciphertext (str): text to be decrypted
        keyword (str): the word that was used for encryption

    Returns:
        plaintext (str): text that has been decrypted

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    tmp_text = ""
    keylen = len(keyword)
    key = keyword.upper()
    i = 0
    for j in ciphertext:
        if not j.isalpha():
            plaintext += j
        else:
            if j.isupper():
                a = "A"
            else:
                a = "a"
            plaintext += chr(ord(a) + ((ord(j) - ord(a)) - (ord(key[i]) - ord("A"))) % 26)
            i += 1
            if i == keylen:
                i = 0
    return plaintext