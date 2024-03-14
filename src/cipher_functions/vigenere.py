# Extended vigènere cipher 256 ascii chars

def vigenere(text, key, encrypt=True):
    outputtext = []
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