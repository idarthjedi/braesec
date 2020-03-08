def decode():
    bsec = str(input("enter braesec: "))
    output = ""
    #while there is still text to decode grabs the first encoded char
    while len(bsec) > 0:
        codechr = getchr(bsec)
        bsec = bsec[len(codechr):]
        try:
            #converts the braesec char and adds it to output
            output += convert(codechr)
        except:
            return("is not braesec!")
        else:
            None
    return(output)

#gets the first braesec char by finding the end of the char and ripping out everything before it
def getchr(bsec):
    pos = 1
    for let in bsec:
        pos += 1
        if (let == "x") or (let == "o"):
            break
    return(bsec[:pos])

#coverts the braesec char to alphanumeric via assgning them a ascii value
def convert(codechr):
    find = {"'": 1, ".": 2,":": 3,"x": 0,"o": 16," ": 0,}
    findr = {".": 4,"'": 8,":": 12," ": 0,}
    ascv = 96
    right = 0
    for curchr in codechr:
        if (curchr == "x") or (curchr == "o"):
            right = 1
            ascv += find[curchr]
        elif right == 1:
            ascv += findr[curchr]
        else:
            ascv += find[curchr]
    return(chr(ascv))
#runs the decode function when i excecute the .py file
print(decode())
