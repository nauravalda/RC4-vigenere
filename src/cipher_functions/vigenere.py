
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
    return outputtext

if __name__ == '__main__':
    plain2 = "gacor rEk1"
    key = "INDO"
    print("Key: ", key)
    print("Plain: ", plain2, " -> ", vigenere(vigenere(plain2, key, True), key, False))
    print("Ciphertext: ", vigenere(plain2, key, True))
    print("Decrypted: ", vigenere(vigenere(plain2, key, True), key, False))




