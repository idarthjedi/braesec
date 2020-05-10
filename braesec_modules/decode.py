def decode(bsec):
    output = ""
    #while there is still text to decode grabs the first encoded char
    while len(bsec) > 0:
        codechr = getchr(bsec)
        bsec = bsec[len(codechr):]
        codechr = codechr.lower()
#        print(codechr)
        try:
            #converts the braesec char and adds it to output
            output += convert(codechr)
        except:
            return("is not braesec!")
        else:
            None
    return output

#gets the first braesec char by finding the end of the char and ripping out everything before it
def getchr(bsec):
    pos = 1
    #this if statment fixes a problem where it wasent breaking out of the for loop if the x was immidiatly at the beggining of the str
    for let in bsec:
        pos += 1
        #there was also a problem with it not grabbing the capitals with this if statment
        if (let == "x") or (let == "o") or (let  == "X") or (let == "O"):
            break
    return(bsec[:pos])

#coverts the braesec char to alphanumeric via assigning them a ascii value
def convert(codechr):
    find = {"'": 1, ".": 2,":": 3,"x": 0,"o": 16," ": 0}
    findr = {".": 4,"'": 8,":": 12," ": 0,}
    ascv = 96
    right = 0
    for curchr in codechr:
        #the problem was this if statment was only checking for lowercase fo uppercase x/o #calledit
        if (curchr == "x") or (curchr == "o"):
            right = 1
            ascv += find[curchr]
        elif right == 1:
            ascv += findr[curchr]
        else:
            ascv += find[curchr]
    return(chr(ascv))
# leaving this commented because i need it alot while  debugging print(decode(input("hi")))
