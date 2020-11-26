def is_set(x, n):
    """
    Takes an n position in binary number x and returns true if the bit is 1
    :param x: binary representation of a number
    :param n: nth position to check if bit is 1
    :return: true if
    """
    return x & 2**n != 0


def encode(string_to_encode):
    textOutput = ""

    for aChar in string_to_encode:

        letterMap = [0, 0, 0, 0, 0]
        # will translate it to this:
        #  0 3
        # 4
        #  1 2
        output = ""

        # binNum = bin(int.from_bytes(aChar.encode(), 'big'))
        intNum = int.from_bytes(aChar.encode(), 'big')

        # print(intNum)
        if intNum != 32:

            for loopCount in range(0, 5):
                letterMap[loopCount] = is_set(intNum, loopCount)

            if letterMap[1]:
                if letterMap[0]:
                    output += ":"
                else:
                    output += "."
            elif letterMap[0]:
                output += "'"

            #According to Braeden on 03/08 - he added this as a filler
            # to ensure there were 3 characters per encoding.
            # He now says he was being lazy and he doesn't need this so I'm commenting it out.

            # else:
            #    output += "|"
            if letterMap[4]:
                output += "o"
            else:
                output += "X"

            if letterMap[3]:
                if letterMap[2]:
                    output += ":"
                else:
                    output += "'"
            elif letterMap[2]:
                output += "."

            # According to Braeden on 03/08 - he added this as a filler
            # to ensure there were 3 characters per encoding.
            # He now says he was being lazy and he doesn't need this so I'm commenting it out.

            #else:
            #    output += "|"

            textOutput += output + " "

        #else:
        #    textOutput += "[SPACE] "
        #    continue

    #print(textOutput)
    return textOutput
