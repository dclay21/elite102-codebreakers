# Codebreakers (Elite 102 Project)

## Table of Contents

- [Description](#Description)
- [How to Use](#How To Use)

## Description
This program utilizes Python to encrypt/decrypt user-specified text files according to one of the three ciphers listed:
- [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher): shifts all letters 3 positions down the alphabet
- [ROTx Cipher](https://en.wikipedia.org/wiki/ROT13): shifts all letters by a number 'x' down the alphabet
- [Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher): utilizes multiple Caesar ciphers in sequence with different shift values to transform message

Currently, the program only works as intended with messages that are strictly lowercase, alphabetic characters, but there are plans to include the entire ASCII table.


## How to Use
This program runs on [Python](https://www.python.org/downloads/) in the command line terminal.

Run the program in the command terminal as seen below, following the file name with the arguments (described below)

Basic Terminal Input: `[directory]>python3 main.py -c [cipher] -d [direction] -s [shift] -i [input file] -o [output file]`

Example - Encoding sample.txt to sampleEncoded.txt using ROTx shift of 13

`C:\Users\johnd\Desktop>python3 main.py -c rotx -d encode -s 13 -i sample.txt -o sampleEncoded.txt`

### Command Line Arguments
- `-h`/`--help` Help: Shows the list of optional arguments and their descriptions

- `-c`/`--cipher` Cipher Type: Choose which cipher to use (caesar, rotx, vigenere)
   - Example: `-c rotx` will perform an ROTx cipher

- `-d`/`--direction` Direction:  Choose to "encode" or "decode" the input file
   - Example: `-d encode` will ensure that the message is encoded

- `-s`/`--shift` Integer Shift (ROTx): Specify an integer to shift the message by for the ROTx cipher (default is 3 for Caesar Cipher)
   - Example: `-s 8` will shift all letters in the message 8 positions down the alphabet

- `-p`/`--password` Password (Vigenere): The given password will be the keyword used to shift each letter in the message
   - Example: `-p lemon` will shift the message vigenere style using "lemon" as the keyword

- `i`/`--input` Input File: Specify the file containing the original message (include the file extension)
   - Example: `-i ogMessage.txt` will take in the file "ogMessage.txt" to be transformed

- `-o`/`--output` Output File: Specify the file to which the encrypted/decrypted message will be written to
   - Example: `-o newMessage.txt` will result in overwriting the file, if it already exists, or creating a new one if it doesn't exist, and leaving the new message



