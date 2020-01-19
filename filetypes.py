
#Given a List of filenames files return a List of string(s) containing the most common extension(s)
#files = ['Lakey - Better days.mp3', 'groovy jam.als', '#4 final mixdown.als', 'album cover.ps', 'good nights.mp3'] 
# return: ['.als', '.mp3']
#files = ['Lakey - Better days.mp3', 'Fisher - Stop it.mp3',  '#4 final mixdown.als', 'album cover.ps']
#return ['.mp3']
def solve(files):
    lst =[]
    obj = {}
    max_num =1
    newfiles =[x[x.rfind(".")+1:] for x in files]
    for y in newfiles:
        if y not in obj:
            obj[y] =1
        else:
            obj[y]+=1
    for el in obj:
        if obj[el]>max_num:
            max_num = obj[el]
    for el2 in obj:
        if obj[el2] == max_num:
            lst.append(el2)
    lst.sort()
    return ["."+v for v in lst]
