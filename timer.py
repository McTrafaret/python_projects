import sys, time

timer = time.perf_counter

def total(reps, func, *pargs, **kargs):
    start = timer()
    for _ in range(reps):
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    best = 2**32
    for _ in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
        return(best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    return bestof(reps1, total, reps2, func, *pargs, **kargs)

