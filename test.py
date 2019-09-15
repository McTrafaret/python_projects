def adder(**kargs):
    kargslist = list(kargs.keys())
    if kargs[kargslist[0]] == type(0):
        Sum = 0
    else:
        Sum = kargs[kargslist[0]][:0]
    for value in kargs.values():
        Sum += value
    return Sum

print(adder(a = 'hype', b = 'flex', c = 'axe'))