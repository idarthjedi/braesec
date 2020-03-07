#!/usr/bin/env python
#Testing updates on the forked version @braebraesean's github page.
#Testing a second update on the local branch
#Third change.
import binascii
# from sys import argv

"""
-:X'.
"""

def is_set(x, n):
    """
    Takes an n position in binary number x and returns true if the bit is 1
    :param x: binary representation of a number
    :param n: nth position to check if bit is 1
    :return: true if
    """
    return x & 2**n != 0


def encode():
    textToConvert = input("Please enter your text to convert: ")
    textOutput = ""

    for aChar in textToConvert:

        letterMap = [0, 0, 0, 0, 0]
        # will translate it to this:
        #  1 3
        # 4
        #  0 2
        output = ""

        # binNum = bin(int.from_bytes(aChar.encode(), 'big'))
        intNum = int.from_bytes(aChar.encode(), 'big')

        # print(intNum)
        if intNum != 32:

            for loopCount in range(0, 5):
                letterMap[loopCount] = is_set(intNum, loopCount)

            if letterMap[4]:
                output += "-"

            if letterMap[1]:
                if letterMap[0]:
                    output += ":"
                else:
                    output += "'"
            elif letterMap[0]:
                output += "."

            output += "X"

            if letterMap[3]:
                if letterMap[2]:
                    output += ":"
                else:
                    output += "'"
            elif letterMap[2]:
                output += "."

            textOutput += output + " "

        else:
            textOutput += "[SPACE] "
            continue

    print(textOutput)
    pass


def decode():
    textToConvert = input("Please enter your text to convert: ")
    # Should check to see if the input is zero length 
    textOutput = textToConvert.split()

    for aChar in textOutput:
        print(aChar)    

    pass


def main():
#    arguments = getopts(argv)
#    print(len(arguments))
    encode()


main()

