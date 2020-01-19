#coin(1) should return ["O", "R"]
#coin(2) should return ["OO", "OR", "RO", "RR"]
#coin(3) should return ["OOO", "OOR", "ORO","ORR", "ROO", "ROR", "RRO", "RRR"]

def coin(n):
    num = 2 **n
    lst =[]
    for x in range(0,num): 
        binx ="{0:b}".format(x)
        while len(binx)<n:
            binx = "0"+binx
        binx = binx.replace("0", "O")
        binx = binx.replace("1","R")
        lst.append(binx)
    lst.sort()
    return lst



