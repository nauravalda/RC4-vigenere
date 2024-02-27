# String replacement
# Convert to lower case and remove non-alphabetic characters
def affineStringReplace(sentence = ""):
    return ''.join(filter(str.isalpha, sentence.lower()))

# Find greatest common divisor
def affineGCD(num1, num2):
    if num1 > num2:
        dividend = num1
        divisor = num2
    else:
        dividend = num2
        divisor = num1
    if dividend % divisor != 0: # continue euclidean algorithm
        return affineGCD(divisor, dividend % divisor)
    else: # GCD found
        return divisor

# Find bezout coefficients
# Return format: (bezout coef of number, bezout coef of modulo)
def affineBezout(number,modulo, gcd):

    quotient = modulo // number
    remainder = modulo % number

    if remainder != gcd:
        bezout1, bezout2 = affineBezout(remainder,number,gcd) # Get smaller coefs.
        return (bezout2 + bezout1 * quotient * -1, bezout1)
    else:
        return (-1 * quotient, remainder) # Return smallest coefs.

# Find inverse
def affineInverse(number,modulo):

    if affineGCD(number,modulo) != 1:
        return None # There is no inverse
    
    return affineBezout(number,modulo,affineGCD(number,modulo))[0]

# Affine cipher
# Character limit: only alphabetic characters, converted to lower case
def affine(text, multiplier, shift, encrypt = True):

    modulo = 26 # Just lower case alphabetic characters

    inverse = affineInverse(multiplier,modulo)
    if inverse is None:
        return None
    
    cleanedInput = [(ord(c) - 97) for c in affineStringReplace(text)]

    # Encryption: multiplier * char + shift
    # Decryption: inverse(multipler) * (char - shift)
    resultList = [ chr((multiplier * c + shift) % 26 + 97) if encrypt else chr((inverse * (c - shift)) % 26 + 97) for c in cleanedInput]

    return "".join(resultList)

# Demo
if __name__ == '__main__':
    plain = "temui ibu nanti malam"
    plain2 = "gacor rEk1"
    multiplier = 3
    shift = 2

    print("Multiplier: ", multiplier)
    print("Shift: ", shift)

    print("\nPlain: ", plain, " -> ", affineStringReplace(plain))
    print("Cipher: ", affine(plain, multiplier, shift))
    print("Decrypted: ", affine(affine(plain, multiplier, shift), multiplier, shift, False))

    print("\nPlain: ", plain2, " -> ", affineStringReplace(plain2))
    print("Cipher: ", affine(plain2, multiplier, shift))
    print("Decrypted: ", affine(affine(plain2, multiplier, shift), multiplier, shift, False))