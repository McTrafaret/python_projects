import timer, sys, math

reps = 1000000

lis = [2, 4, 9, 16, 25]

def forLoop():
    new = []
    for i in lis:
        new.append(math.sqrt(i))     
    return new

def mapCall():
    return list(map(math.sqrt, lis))

def lisComp():
    return [math.sqrt(i) for i in lis]

def genExp():
    return list(math.sqrt(i) for i in lis)

print(mapCall())

for test in (forLoop, lisComp, mapCall, genExp):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000000, test)
    print('%-9s: %.5f' %
         (test.__name__, bestof))