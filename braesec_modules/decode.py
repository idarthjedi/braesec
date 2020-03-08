def decode(string_to_decode):
    decoded = ""
    value = {" ": 0,"x": 0,"X": 0,"|": 0,"'": 1, ".": 2,":": 3, "o": 16}
    valuel = {"'": 8,".": 4,":": 12,"|": 0," ": 0,}
    while len(ttc) > 2:
        curchr = ttc[0:4]
        ttc =ttc[4:]
        newchr = chr(96 + value[curchr[0]] + value[curchr[1]] + valuel[curchr[2]] + valuel[curchr[3]])
        decoded += newchr

    return decoded
