def playfairStringReplace(sentence = "", isKey = False):

    # 1. Convert to lower case and remove non-alphabetic characters
    # 2. Remove letter J and returns unique letter list if isKey is true
    # 3. Change letter J to I and returns if isKey is false

    substitution = ''.join(filter(str.isalpha, sentence.lower().replace('J','') if isKey else sentence.lower().replace('J','I')))

    return "".join(dict.fromkeys(substitution)) if isKey else substitution


def playfairKeyMatrix(sentence = ""):
    
    letterList = playfairStringReplace(sentence,True)

    refList = [c for c in "abcdefghiklmnopqrstuvwxyz"]
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
# Character limit: only alphabetic characters, converted to lower case. J character converted to I
def playfair(text, key, encrypt = True):

    cleanedInput = [c for c in playfairStringReplace(text)]

    keyMatrix = playfairKeyMatrix(key)

    startList = cleanedInput.copy()
    tempList = []
    endList = []

    # Bigram processing
    while len(startList) > 0:
        # Get bigram
        tempList.append(startList.pop(0))
        if encrypt:
            if len(startList) > 0: # Bigram complete
                tempList.append(startList.pop(0))
            elif tempList[0] == "x": # Bigram incomplete, first char is X
                tempList.append("z") 
            else: # Bigram incomplete, first char not X
                tempList.append("x")
        else:
            tempList.append(startList.pop(0))

        # Check if duplicate
        if encrypt and tempList[0] == tempList[1]:
            startList.insert(0,tempList[1])
            tempList[1] = "x" if tempList[0] != "x" else "z" # Use Z if bigram is previously XX
        
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