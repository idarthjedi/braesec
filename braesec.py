#!/usr/bin/env python
import binascii
from base64 import decode
import braesec_modules.encode as encoder
import braesec_modules.decode as decoder


# from sys import argv

"""
-:X'.
"""


def main():
    run = str(input("do you want to encode(e) or decode(d): "))
    if run == "e":
        texttoconvert = input("Please enter your text to convert: ")
        output = encoder.encode(texttoconvert)
        print(output)
    elif run == "d":
        ttc = str(input("Please enter your text to convert(space at the beggining): "))
        output = decoder.decode(ttc)
        print(output)
    else:
        print("pleas enter d or e.")


main()
