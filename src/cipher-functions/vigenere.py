def encrypt_vigenere(plaintext, key):
    key = key.lower()
    key_len = len(key)
    plaintext = ''.join(filter(str.isalpha, plaintext.lower()))
    ciphertext = ''
    for i, char in enumerate(plaintext):
        key_char = key[i % key_len]
        shift = (ord(key_char) - ord('a')) % 26
        # remove non-alphabet characters
        if char.isalpha():
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += encrypted_char
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    # Decrypt a text
    plaintext = ""
    key = key.lower()
    key_len = len(key)
    ciphertext = ''.join(filter(str.isalpha, ciphertext.lower()))
    for i, char in enumerate(ciphertext):
        key_char = key[i % key_len]
        shift = (ord(key_char) - ord('a')) % 26
        if char.isalpha():
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext += decrypted_char
    return plaintext

# test
# plaintext = "halooooo"
# key = "heru"
# ciphertext = encrypt_vigenere(plaintext, key)
# print(ciphertext)
# print(decrypt_vigenere(ciphertext, key))