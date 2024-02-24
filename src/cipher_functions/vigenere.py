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
            # Cj = (Pj + Kj) mod 26
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
# file_path = "D:/Coll Things/Semester 6/KRIPTO/classic-ciphers/src/cipher_functions/test.txt"
# file = open(file_path, "r")
# text = file.read()
# file.close()
# print(text)
# print(encrypt_vigenere(text, "pa"))
# print(decrypt_vigenere(encrypt_vigenere(text, "pa"), "pa"))




