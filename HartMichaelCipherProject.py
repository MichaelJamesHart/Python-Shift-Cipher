# Michael Hart
# Shift Cipher Project

# This is a helper function to handle upper-case letters.
# If the argument is inside of the upper-case alphabet list,
# set the variable lowerCharacter to be the element that is in the same position in the lower-case alphabet list.
# If the argument is not in the upper-case alphabet list, set lowerCharacter to be equal to the argument.
def upperToLower(character):
    lowerAlphaList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upperAlphaList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowerCharacter = ""
    if character in upperAlphaList:
        lowerCharacter = lowerAlphaList[upperAlphaList.index(character)]
    else:
        lowerCharacter = character
    return lowerCharacter


# This function carries out shift cipher encryption.
# Assume that the value of shift is between 0 and 31 inclusive, and the order of the characters is as follows:
# abcdefghijklmnopqrstuvwxyz ';.?,
# Notice that the space is between z and '
# For example, shiftEncrypt("apple", 3) will RETURN the string "dssoh"
def shiftEncrypt(plainText, shift):
    encryptedWord = ""
    alphaList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "'", ";", ".", "?", ","]
    for i in plainText:
        # If the value of (the index of a character + shift) is less than 
        # 31, then that value will be the index used to assign the new element 
        # for the encrypted word.        
        if (alphaList.index(upperToLower(i)) + shift) < 32:
            encryptedWord += upperToLower(alphaList[alphaList.index(upperToLower(i)) + shift])
        # If the value of (the index of a character + shift) is greater than 
        # 31, then 32 will be subtracted from that value to reach the index that 
        # will be used to assign the new element for the encrypted word.
        else:
            encryptedWord += upperToLower(alphaList[(alphaList.index(upperToLower(i)) + shift) - 32])
    return encryptedWord


# This function carries out the shift cipher decryption.
# Assume that the value of shift is between 0 and 31 inclusive, and the order of the characters is as follows:
# abcdefghijklmnopqrstuvwxyz ';.?,
# Notice that the space is between z and '
# For example, shiftDecrypt("dssoh", 3) will RETURN the string "apple"
def shiftDecrypt(cipherText, shift):
    decryptedWord = ""
    alphaList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "'", ";", ".", "?", ","]
    for i in cipherText:
        # If the value of (the index of a character - shift) is greater than -1,
        # then that value will be the index used to assign the new element or the decrypted word.
        if (alphaList.index(upperToLower(i)) - shift) > (-1):
            decryptedWord += alphaList[alphaList.index(upperToLower(i)) - shift]
        # If the value of (the index of a character - shift) is less than -1,
        # then 32 will be added from that value to reach the index that will be used
        # to assign the new element for the decrypted word.
        else:
            decryptedWord += alphaList[alphaList.index(upperToLower(i)) - shift + 32]
    return decryptedWord


# This function takes a string as an argument, and returns a list consisting of
# each character in the string in a separate index,
# with each character in the list appearing in the same order as it appears in the string.
# For example,
# >>>listFromString("hello")
# should return the list ['h', 'e', 'l', 'l', 'o']
# The function takes the argument aString, creates an empty list called newList,
# then iterates through aString to append each element of the argument to the newList list.
def listFromString(aString):
    newList = []
    for i in aString:
        # While appending, helper function upperToLower is called on to ensure
        # that any characters added to the list from the string are changed to lower-case.
        newList.append(upperToLower(i))
    return newList


# The encryption function takes two file names as arguments.
# The file represented by theKeys should contain 3 lines, where each line is a shuffling of 26 lower case letters,
# 5 punctuation symbols and a space.
# The file represented by plainFile should contain text that should be encrypted.
# The function should encrypt the contents of plainFile, and save the cipher text in a file named cipherText.txt.
# Upper case letters will be converted to lower case letters and be encrypted.
# The letters will then appear as lower case letters in the ciphertext.
def MultiAlphaCipher(theKeys, plainFile):
    # Open the file indicated by the file name theKeys to read the file.
    readingTheKeys = open(theKeys, "r")
    # Each line in the file represents a shuffling of the characters and punctuation that will be used as a key.
    # Create 3 variables, line0, line1, and line2 that contain the 3 lines of text from the file theKeys.
    # Setting line0, line1, and line2 to be empty strings, which will later be used to hold the contents of theKeys file.
    line0 = ""
    line1 = ""
    line2 = "" 
    # Create a list alphaList that holds the alphabet and other characters in the proper order,
    # to be referenced later by the encryption and decryption process.
    alphaList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "'", ";", ".", "?", ","]
    # Create an empty list called listOfTheKeys to hold all of the keys in a list
    # in the order that they appear in theKeys file.
    listOfTheKeys = []
    # Iterate through theKeys file (indicated by the variable readingTheKeys,
    # and appending each individual character to the list (listOfTheKeys).
    # Within this iteration, the helper function (upperToLower) makes any upper-case letters into lower-case.
    for word in readingTheKeys:
        for char in word:
            listOfTheKeys.append(upperToLower(char))
    # There are three seperate FOR iterations, each going through 32 indexes in listOfTheKeys
    # and concatenating the element to line0, line1, and line2 respectively.
    # Within these iterations, the helper function (upperToLower) makes any upper-case letters into lower-case.
    for i in range(0,32):
        line0 += upperToLower(listOfTheKeys[i])
    for i in range(33,65):
        line1 += upperToLower(listOfTheKeys[i])
    for i in range(66,98):
        line2 += upperToLower(listOfTheKeys[i])
    # line0 should contain the first line in the file theKeys
    # line1 should contain the second line in the file theKeys
    # line2 should contain the third line in the file theKeys 
    # Close the file theKeys.
    readingTheKeys.close()
    # Use the helper function listFromString(aString) to create lists from the three key strings.
    # key0 is the list generated from line0
    # key1 is the list generated from line1
    # key2 is the list generated from line2
    key0 = listFromString(line0)
    key1 = listFromString(line1)
    key2 = listFromString(line2)
    # Open the file indicated by the file name plainText to
    # read and assign the contents to a variable named fileContents.
    openingPlainFile = open(plainFile, "r")
    # Create a variable fileContents with an empty string, to which all of the text from plainFile will be copied.
    fileContents = ""
    # Iterate through openingPlainFile to concatenate each letter of each word to the fileContents variable.
    for word in openingPlainFile:
        for letter in word:
            # Call on the helper function upperToLower to ensure that any upper-case characters are converted into
            # lower-case characters.
            fileContents += upperToLower(letter)
    # Close the file.
    openingPlainFile.close()
    fileContentsList = listFromString(fileContents)
    # Open a file named cipherText.txt to write the cipher Text
    # Read through the file, and encrypt each character using the correct key:
    # alternating between key0, key1 and key2, and write that information
    # to the file cipherText.txt.
    encryptedString = ""
    # Set count = 0, then iterate through every character (char) in cipherFileContents.
    count = 0
    for char in fileContents:
        # If the character is not in the alphabet list, this character will be concatenated to encryptedString as it is.
        if upperToLower(char) not in alphaList:
            encryptedString += char
        # If the count = 0, concatenate the key0 list element at the index of the char in alphaList, then set count = 1.
        elif count == 0:
            encryptedString += key0[alphaList.index(char)]
            count = 1
        # If the count = 1, concatentate the key1 element at the index of the char in alphaList,
        # then set count = 2.
        elif count == 1:
            encryptedString += key1[alphaList.index(char)]
            count = 2
        # If the count = 2, concatentate the key2 list element at the index of the char in alphaList,
        # then set count = 0, so the whole process will repeat from the beginning of the for interation.
        elif count == 2:
            encryptedString += key2[alphaList.index(char)]
            count = 0
    cipherFile = "cipherText.txt"
    writingCipherText = open(cipherFile, "w")
    writingCipherText.write(encryptedString)
    # Close the cipherText.txt file.
    writingCipherText.close()


# The decryption function will take two file names as arguments.
# The file represented by theKeys should contain 3 lines, where each line is a shuffling of 26 lower case letters,
# 5 punctuation symbols and a space. The file represented by cipherFile should contain text that should
# be decrypted.
# The function should decrypt the contents of cipherFile by reversing the encryption algorithm,
# and save the plain text in a file named MyDecryptedText.txt.
def MultiAlphaDecipher(theKeys, cipherFile):
    # Open the file indicated by theKeys argument.
    readingTheKeys = open(theKeys, "r")
    # Set line0, line1, and line2 to be empty strings, which will later be used to hold the contents of theKeys file.
    line0 = ""
    line1 = ""
    line2 = ""
    # Include a list called alphaList that holds the alphabet and other characters in the proper order,
    # to be referenced later by the encryption and decryption process.
    alphaList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "'", ";", ".", "?", ","]
    # Making an empty list called listOfTheKeys
    # to hold all of the keys in a list in the order that they appear in theKeys file.
    listOfTheKeys = []
    # Iterate through theKeys file (indicated by the variable readingTheKeys,
    # and appending each individual character to the list (listOfTheKeys).
    # Within this iteration, call on the helper function (upperToLower) to make any upper-case letters into lower-case.
    for word in readingTheKeys:
        for char in word:
            listOfTheKeys.append(upperToLower(char))
    # There are three seperate FOR iterations, each going through 32 indexes in listOfTheKeys and concatenating the
    # element to line0, line1, and line2 respectively.
    # Within these iterations, the helper function (upperToLower) will make any upper-case letters into lower-case.
    for i in range(0,32):
        line0 += upperToLower(listOfTheKeys[i])
    for i in range(33,65):
        line1 += upperToLower(listOfTheKeys[i])
    for i in range(66,98):
        line2 += upperToLower(listOfTheKeys[i])
    # Close theKeys file.
    readingTheKeys.close()
    # Call the helper function listFromString to set
    # the lists key0, key1, and key2 to be lists of line0, line1, and line2.
    key0 = listFromString(line0)
    key1 = listFromString(line1)
    key2 = listFromString(line2)
    # Create a variable decryptedString that will contain the decrypted contents of cipherFile.
    decryptedString = ""
    # Opening cipherFile and copy its contents to decryptedString.
    openingCipherFile = open(cipherFile, "r")
    # Create a variable with an empty string called cipherFileContents to hold all of the text from the cipherFile.
    cipherFileContents = ""
    # Iterate through the openingCipherFile to add each letter of each
    # word to the cipherFileContents. Calls on the helper function upperToLower
    # to ensure that any upper-case character is converted to lower-case.
    for word in openingCipherFile:
        for letter in word:
            cipherFileContents += upperToLower(letter)
    # Close the openingCipherFile
    openingCipherFile.close()
    # Set count = 0, then iterate through every character (char) in cipherFileContents.
    count = 0
    for char in cipherFileContents:
        # If the character is not in the alphabet list, this character will be 
        # concatenated to decryptedString as it is.
        if upperToLower(char) not in alphaList:
            decryptedString += char
        # If the count = 0, concatenate the alphabet list (alphaList)element at the index of the char in key0,
        # then set count = 1.
        elif count == 0:
            decryptedString += alphaList[key0.index(char)]
            count = 1
        # If the count = 1, concatentate the alphabet list (alphaList)element at the index of the char in key1,
        # then set count = 2.
        elif count == 1:
            decryptedString += alphaList[key1.index(char)]
            count = 2
        # If the count = 2, concatentate the alphabet list (alphaList)element at the index of the char in key2,
        # then set count = 0, so the whole process will repeat from the beginning of the for interation.
        elif count == 2:
            decryptedString += alphaList[key2.index(char)]
            count = 0
    # Open the file "MyDecryptedText.txt".
    decryptedFile = "MyDecryptedText.txt"
    writingDecryptedText = open(decryptedFile, "w")
    # Write the completed decryptedString string to the MyDecryptedText.txt file.
    writingDecryptedText.write(decryptedString)
    # Close the MyDecryptedText.txt file.
    writingDecryptedText.close()