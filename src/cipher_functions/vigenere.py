
def vigenere(inputtext, key, encrypt=True):
    key = key.lower()
    key_len = len(key)
    inputtext = ''.join(filter(str.isalpha, inputtext.lower()))
    outputtext = ''
    for i, char in enumerate(inputtext):
        key_char = key[i % key_len]
        shift = (ord(key_char) - ord('a')) % 26
        if char.isalpha():
            if encrypt:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                outputtext += encrypted_char
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                outputtext += decrypted_char
    return outputtext.upper()

# test
# file_path = "D:/Coll Things/Semester 6/KRIPTO/classic-ciphers/src/cipher_functions/test.txt"
# file = open(file_path, "r")
# text = file.read()
# file.close()
# print(text)
# print(vigenere(text, "kripto", True))
# print(vigenere(vigenere(text, "kripto", True), "kripto", False))




