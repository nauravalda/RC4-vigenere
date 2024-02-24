def encrypt_autokey_vigenere(plaintext, key):
    # Encrypt a text using autokey vigenere cipher
    ciphertext = ""
    key = key.lower()
    key_len = len(key)
    plaintext = ''.join(filter(str.isalpha, plaintext.lower()))
    for i, char in enumerate(plaintext):
        if i < key_len:
            key_char = key[i]
        else:
            key_char = plaintext[i - key_len]
        shift = (ord(key_char) - ord('a')) % 26
        # remove non-alphabet characters
        if char.isalpha():
            # Cj = (Pj + Kj) mod 26
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += encrypted_char
    return ciphertext

def decrypt_autokey_vigenere(ciphertext, key):
    # Decrypt a text using autokey vigenere cipher
    plaintext = ""
    key = key.lower()
    key_len = len(key)
    ciphertext = ''.join(filter(str.isalpha, ciphertext.lower()))
    for i, char in enumerate(ciphertext):
        if i < key_len:
            key_char = key[i]
        else:
            key_char = plaintext[i - key_len]
        shift = (ord(key_char) - ord('a')) % 26
        if char.isalpha():
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext += decrypted_char
    return plaintext

# test
plaintext = "negarapenghasilminyakmentahdidunia"
key = "INDO"
ciphertext = encrypt_autokey_vigenere(plaintext, key)
print(ciphertext)
print(decrypt_autokey_vigenere(ciphertext, key))

