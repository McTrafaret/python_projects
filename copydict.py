a = {'a':'hype', 'b':'flex', 'c':'axe'}

def copyDict(dikt):
    new = {}
    for key in dikt.keys():
        new[key] = dikt[key]
    new['f']='press'
    return new

print(copyDict(a))
print(a)