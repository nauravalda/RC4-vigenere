def autokey_vigenere(inputtext, key, encrypt=True):
    key = key.lower()
    key_len = len(key)
    inputtext = ''.join(filter(str.isalpha, inputtext.lower()))
    outputtext = ''
    if encrypt:
        for i, char in enumerate(inputtext):
            if i < key_len:
                key_char = key[i]
            else:
                key_char = inputtext[i - key_len]
            shift = (ord(key_char) - ord('a')) % 26
            if char.isalpha():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                outputtext += encrypted_char
    else:
        for i, char in enumerate(inputtext):
            if i < key_len:
                key_char = key[i]
            else:
                key_char = outputtext[i - key_len]
            shift = (ord(key_char) - ord('a')) % 26
            if char.isalpha():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                outputtext += decrypted_char
    return outputtext.upper()

# test
plaintext = "negarapenghasilminyakmentahdidunia"
key = "INDO"
ciphertext = autokey_vigenere(plaintext, key, True)
print(ciphertext)
print(autokey_vigenere(ciphertext, key, False))

# ciphertext = encrypt_autokey_vigenere(plaintext, key)
# print(ciphertext)
# print(decrypt_autokey_vigenere(ciphertext, key))
