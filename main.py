import sys

def rotXencrypt(message, shift):
    newMessage = []
    for line in message:
        newLine = ""
        for currentChar in line:
            newChar = currentChar
            if currentChar.isalpha():
              newChar = chr((ord(currentChar) + shift -87) % 26 + 97)
            newLine += newChar
        newMessage.append(newLine)
    return newMessage

def rotXdecrypt(message, shift):
    return rotXencrypt(message, -shift)

def caesarEncrypt(message):
    return rotXencrypt(message, 3)

def caesarDecrypt(message):
    return rotXencrypt(message, -3)

def vigenereEncrypt(message, key):
    newMessage = []
    keypos = 0
    for line in message:
        newLine = ""
        for currentChar in line:
            newChar = currentChar
            if currentChar.isalpha():
                if keypos == len(key):
                    keypos = 0
                newChar = chr((ord(currentChar)+ ord(key[keypos]) - 194) % 26 + 97)
                keypos += 1
            newLine += newChar
        newMessage.append(newLine)
    return newMessage

def vigenereDecrypt(message, key):
    newMessage = []
    keypos = 0
    for line in message:
        newLine = ""
        for currentChar in line:
            newChar = currentChar
            if currentChar.isalpha():
                if keypos == len(key):
                    keypos = 0
                newChar = chr((ord(currentChar) - ord(key[keypos]) +26) % 26 + 97)
                keypos += 1
            newLine += newChar
        newMessage.append(newLine)
    return newMessage
