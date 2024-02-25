# Extended vigènere cipher 256 ascii chars
#

def extended_vigenere(inputtext, key, encrypt=True, byte=False):
    outputtext = ""
    if not byte:
        if encrypt:
            for i in range(0, len(inputtext)):
                outputtext += chr((ord(inputtext[i]) + ord(key[i % len(key)]) % 256))
        else:
            for i in range(0, len(inputtext)):
                outputtext += chr((ord(inputtext[i]) - ord(key[i % len(key)]) % 256))
    else:
        for i in range(len(inputtext)):
            key_byte = ord(key[i % len(key)])  # Mengonversi karakter kunci ke bilangan bulat
            if encrypt:
                output_byte = (inputtext[i] + key_byte) % 256

            else:
                output_byte = (inputtext[i] - key_byte) % 256
            outputtext += chr(output_byte)
    return outputtext

def extended_vigenere_bin(input_file, output_file, key, encrypt=True):
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            key_index = 0
            for byte in f_in.read():
                key_byte = ord(key[key_index % len(key)])
                if encrypt:
                    encrypted_byte = (byte + key_byte) % 256
                else:
                    encrypted_byte = (byte - key_byte) % 256
                f_out.write(bytes([encrypted_byte]))
                key_index += 1


# test
# plaintext = "halo?@JI"
# key = "oke"
# ciphertext = encrypt_extended_vigenere(plaintext, key)
# print(ciphertext)
# print(decrypt_extended_vigenere(ciphertext, key))

# plaintext = "halo?@JI"
# key = "oke"
# ciphertext = extended_vigenere(plaintext, key, True)
# print(ciphertext)
# print(extended_vigenere(ciphertext, key, False))

# print(extended_vigenere("°©ÔØ¿ÊÓ", "hi", False))