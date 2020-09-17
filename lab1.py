import math

def task1():
    print(2**179)

def task2():
    print(math.factorial(20));

def task3():
    print((179**2 + 971**2)**0.5)

def task4():
    print(a*100)

def task5():
    string = input().strip().split(' ')
    for i in range(len(string)):
        string[i] = int(string[i])
    print(max(string))

def task6_cmp(a, b):
    if (a > b): return 1
    elif (a < b): return -1
    return 0

def task6(a, b):
    print(task6_cmp(a, b))

def task7():
    print(int("179"*50)**2)

def task8(a, b):
    print((a**2 + b**2)**0.5)

def task9(a, b, c):
    max(a, b, c)

def task10(a, b, c):
    if(a + b >= c and a + c >= b and b + c >= a): print("YES")
    else: print("NO")

def task11(a, b):
    if(a[0] == b[0] or a[1] == b[1]):
        print("YES")
    else:
        print("NO")

def task12():
    print(int(str(179**10)*4)**(1/10))

def task13(y):
    if((y % 4 == 0 and y % 100 != 0) or y % 400 == 0): print("YES")
    else: print("NO")

def task14(a, b):
    # possible_moves = []
    # for i in [-2, -1, 1, 2]:
    #     for j in [-2, -1, 1, 2]:
    #         if(chr(ord(a[0]) + i) < 'a' or chr(ord(a[0]) + i) > 'f'):
    #             continue
    #         if(chr(ord(a[1]) + j) < '1' or chr(ord(a[1]) + j) > '8'):
    #             continue
    #         if(abs(i) == abs(j)):
    #             continue
    #         possible_moves.append(chr(ord(a[0]) + i) + chr(ord(a[1]) + j));
    # if b in possible_moves: print("YES")
    # else: print("NO")
    dx = abs(ord(a[0])-ord(b[0]))
    dy = abs(ord(a[1])-ord(b[1]))
    if(((dx == 2) and (dy == 1)) or ((dy == 2) and (dx == 1))):
        print("YES")
    else:
        print("NO")

def task15(a, b):
    print(*list(range(a, b + 1)))

def task16(n):
    sum_ = 0
    for i in range(1, n + 1):
        sum_ += i**2
    print(sum)

def task17(n):
    print(math.factorial(n))

def task18(n, k):
    print(math.factorial(n) / math.factorial(k) / math.factorial(n-k))

def task19(n):
    penguine = ["   _~_    ",
                "  (o o)   ",
                " /  V  \  ",
                "/(  _  )\ ",
                "  ^^ ^^   "]
    for string in penguine:
        print(string*n)

def task_20(n, m, k):
    if(n * m > k and (k % n == 0 or k % m == 0)):
        print("YES")
    else:
        print("NO")

def task21(a, b):
    if(not a):
        if(not b): print("INF")
        else: print("NO")
    print(-b / a)

def task22():
    for i in range(100, 1000):
        if(i**2 % 1000 == i):
            print(i)

def task23(n):
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print(j, end='')
        print()

def task24():
    arr = [int(i) for i in input().strip().split(' ')]
    arr.sort()
    print(*arr)

def task25():
    sum_ = 0
    for i in range(1, n+1):
        sum_ += math.factorial(i)
    print(sum_)
