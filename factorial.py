import functools, math, timer

def fact1(N):
    if N < 0:
        return 'can\'t count negative factorials'
    elif N <= 1:
        return 1
    else:
        return N*fact1(N-1)

def fact2(N):
    if N < 0:
        return 'can\'t count negative factorials'
    elif N == 0:
        return 1
    else:
        return functools.reduce(lambda x, y: x * y, range(1,N+1))

def fact3(N):
    if N < 0:
        return 'can\'t count negative factorials'
    elif N == 0:
        return 1
    else:
        counter = 1
        for i in range(1, N+1):
            counter *= i
        return counter

def fact4(N):
    return math.factorial(N)

for test in (fact1, fact2, fact3, fact4):
    (bestof, (total, result)) = timer.bestoftotal(5, 100000, test, 30)
    print('%-9s: %.5f => %s' % (test.__name__, bestof, result))