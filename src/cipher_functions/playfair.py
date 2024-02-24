import re # regex

def playfairStringReplace(sentence = "", isKey = False):

    # 1. Convert to upper case and remove non-alphabetic characters
    # 2. Remove letter J and returns unique letter list if isKey is true
    # 3. Change letter J to I and returns if isKey is false

    substitution = re.sub(r'[^A-Z]', '', sentence.upper().replace('J','') if isKey else sentence.upper().replace('J','I'))

    return "".join(dict.fromkeys(substitution)) if isKey else substitution


def playfairKeyMatrix(sentence = ""):
    
    letterList = playfairStringReplace(sentence,True)

    refList = [c for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
    endList = []

    for c in letterList: # insert key letter to matrix
        refList.remove(c)
        endList.append(c)
    
    endList += refList # append remaining lestters

    return [endList[:5], endList[5:10], endList[10:15], endList[15:20], endList[20:]] # split as 5x5 matrix

def playfairMatrixPos(char, matrix):

    lin = 0
    col = 0
    found = False

    # Search
    for l in matrix:
        for c in l:
            if c == char:
                found = True
                break
            col += 1
        if found:
            break
        col = 0
        lin += 1

    return (lin,col)

def playfairBigramTransform(bigram, keyMatrix, encrypt):

    posList = (playfairMatrixPos(bigram[0],keyMatrix), playfairMatrixPos(bigram[1],keyMatrix))
    
    if posList[0][0] == posList[1][0]: # same row
        bigram[0] = keyMatrix[posList[0][0]][(posList[0][1] + (1 if encrypt else -1)) % 5]
        bigram[1] = keyMatrix[posList[1][0]][(posList[1][1] + (1 if encrypt else -1)) % 5]
    elif posList[0][1] == posList[1][1]: # same col
        bigram[0] = keyMatrix[(posList[0][0] + (1 if encrypt else -1)) % 5][posList[0][1]]
        bigram[1] = keyMatrix[(posList[1][0] + (1 if encrypt else -1)) % 5][posList[1][1]]
    else:
        bigram[0] = keyMatrix[posList[0][0]][posList[1][1]]
        bigram[1] = keyMatrix[posList[1][0]][posList[0][1]]

    return

# Playfair cipher
# Character limit: only alphabetic characters, converted to upper case. J character converted to I
def playfair(plaintext, key, encrypt = True):

    plainList = [c for c in playfairStringReplace(plaintext)]

    keyMatrix = playfairKeyMatrix(key)

    startList = plainList.copy()
    tempList = []
    endList = []

    # Bigram processing
    while len(startList) > 0:
        # Get bigram
        tempList.append(startList.pop(0))
        if encrypt:
            if len(startList) > 0: # Bigram complete
                tempList.append(startList.pop(0))
            elif tempList[0] == "X": # Bigram incomplete, first char is X
                tempList.append("Z") 
            else: # Bigram incomplete, first char not X
                tempList.append("X")
        else:
            tempList.append(startList.pop(0))

        # Check if duplicate
        if encrypt and tempList[0] == tempList[1]:
            startList.insert(0,tempList[1])
            tempList[1] = "X" if tempList[0] != "X" else "Z" # Use Z if bigram is previously XX
        
        playfairBigramTransform(tempList,keyMatrix,encrypt) # Transform bigram (plaintext <-> cipher)

        endList.append(tempList[0])
        endList.append(tempList[1])

        tempList = []

    return "".join(endList)

# Demo
if __name__ == '__main__':
    plain = "temui ibu nanti malam"
    plain2 = "gacorreexxx"
    key = "jalan ganesha sepuluh"

    print("Key: ",key, " -> ", playfairStringReplace(key,True))

    print("\nPlain: ",plain, " -> ", playfairStringReplace(plain))
    print("Cipher: ", playfair(plain,key))
    print("Decrypted: ",playfair(playfair(plain,key),key,False))

    print("\nPlain: ",plain2, " -> ", playfairStringReplace(plain2))
    print("Cipher: ", playfair(plain2,key))
    print("Decrypted: ",playfair(playfair(plain2,key),key,False))