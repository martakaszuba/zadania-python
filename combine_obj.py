# objA = { 'a': 10, 'b': 20, 'c': 30 }
    # objB = { 'a': 3, 'c': 6, 'd': 3 }
    # combine(objA, objB) Returns { a: 13, b: 20, c: 36, d: 3 }
def combine(*args):
    dict1 = {}
    for i in args:
        for x in i:
            if x in dict1:
                dict1[x] +=i[x]
            else:
                dict1[x] = i[x]
    return dict1
