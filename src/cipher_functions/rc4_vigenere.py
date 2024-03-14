# RC4 cipher with vigenere-algorithm-reinforced PRGA
# 
# Inputs:
# - Plaintext/ciphertext as byte array
# - Key as byte array
# Output: Ciphertext as byte array
def rc4(text, key, encrypt=True):

    # Initialise cipher byte array
    cipher = bytearray(text)

    # KSA
    # S array initialization
    S = [c for c in range(256)]
    # S array permutation
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    # PRGA
    i = 0
    j = 0
    for k in range(len(text)):
        i = (i+1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        u = S[t]
        v = key[t % len(key)] # Vigenere substitution
        w = (u + v) % 256 # Apply vigenere substitution
        cipher[k] = cipher[k] ^ w

    return cipher

if __name__ == '__main__':
    from binascii import hexlify
    plain = bytearray("Plaintext",'utf-8')
    key = bytes("Key",'utf-8')
    enc = rc4(plain,key)
    print(hexlify(plain).decode('ascii').upper())
    print(rc4(enc,key,False).decode())