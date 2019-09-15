import time 
def timer(func, *args):
    start = time.clock()
    for _ in range(1000):
        func(*args)
    return time.clock() - start

print(timer(pow, 2, 100000))