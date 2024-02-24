# Extended vigènere cipher 256 ascii chars
#
def encrypt_extended_vigenere(plaintext, key):
    # Encrypt a text using extended vigenere cipher
    ciphertext = ""
    for i in range(0, len(plaintext)):
        ciphertext += chr((ord(plaintext[i]) + ord(key[i % len(key)])) % 256)
    return ciphertext

def decrypt_extended_vigenere(ciphertext, key):
    # Decrypt a text using extended vigenere cipher
    plaintext = ""
    for i in range(0, len(ciphertext)):
        plaintext += chr((ord(ciphertext[i]) - ord(key[i % len(key)])) % 256)
    return plaintext

# test
# plaintext = "halo?@JI"
# key = "oke"
# ciphertext = encrypt_extended_vigenere(plaintext, key)
# print(ciphertext)
# print(decrypt_extended_vigenere(ciphertext, key))
