#Find the missing letter
#["a","b","c","d","f"] -> "e"
#["O","Q","R","S"] -> "P"

def missing_letter(chars):
    boolean = chars[0] == chars[0].upper()
    alpha ="abcdefghijklmnopqrstuvwxyz"
    chars = "".join(chars).lower()
    strng =""
    frst = alpha.find(chars[0])
    last = alpha.find(chars[-1])
    for x in range(frst,last+1):
        strng+= alpha[x]
    for i in strng:
        if i not in chars:
            if boolean:
                return i.upper()
            else:
                return i
