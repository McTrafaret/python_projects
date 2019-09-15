import timer, sys

reps = 10000

def forLoop():
    res = []
    for x in range(reps):
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in range(reps)]

def mapCall():
    return list(map(abs, range(reps)))

def genExpr():
    return list(abs(x) for x in range(reps))

def genFunc():
    def Gen():
        for x in range(reps):
            yield abs(x)
    return list(Gen())


print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' %
         (test.__name__, bestof, result[0], result[-1]))