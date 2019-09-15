import timer, sys

reps = 10000

def forLoop():
    res = []
    for x in range(reps):
        res.append(x+10)
    return res

def listComp():
    return [x+10 for x in range(reps)]

def mapCall():
    return list(map(lambda x: x+10, range(reps)))

def genExpr():
    return list(x+10 for x in range(reps))

def genFunc():
    def Gen():
        for x in range(reps):
            yield x+10
    return list(Gen())


print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' %
         (test.__name__, bestof, result[0], result[-1]))