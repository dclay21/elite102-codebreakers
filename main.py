import argparse

###
### encryption/decryption methods
###

def rotXencrypt(message, shift):
    newMessage = []
    for line in message:
        newLine = ""
        for currentChar in line:
            newChar = currentChar
            if currentChar.isalpha():
              newChar = chr((ord(currentChar) + shift -97) % 26 + 97)
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


###
### main code
###

if __name__=='__main__':
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="Codebreakers"
    )

    # Add the parameters positional/optional
    parser.add_argument('-c','--cipher', help="Cipher Type (caesar, rotx, vigenere)", default="caesar")
    parser.add_argument('-d','--direction', help="encode or decode", default="decode")
    parser.add_argument('-s','--shift', help="integer shift", type=int, default=3)
    parser.add_argument('-p','--password', help="vigenere password")
    parser.add_argument('-i', '--input', help="input file name")
    parser.add_argument('-o', '--output', help="output file name", default="output.txt")

    # Parse the arguments
    args = parser.parse_args()
    print(args)

    # read in the input file
    input_file = args.input
    with open(input_file) as f_in:
        message = f_in.readlines()

    # encrypt or decrypt the file
    parameter = None
    newMessage = None
    if args.cipher == 'vigenere':
        parameter = args.password
        if args.direction == 'encode':
            newMessage = vigenereEncrypt(message, parameter)
        else:
            newMessage = vigenereDecrypt(message, parameter)
    elif args.cipher == 'rotx':
        parameter = args.shift
        if args.direction == 'encode':
            newMessage = rotXencrypt(message, parameter)
        else:
            newMessage = rotXdecrypt(message, parameter)
    elif args.cipher == 'caesar':
        if args.direction == 'encode':
            newMessage = caesarEncrypt(message)
        else:
            newMessage = caesarDecrypt(message)

    # write result to new file
    with open(args.output,"w") as f_out:
        for line in newMessage:
            f_out.write(line)


