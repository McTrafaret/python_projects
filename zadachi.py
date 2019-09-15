'''def vasya():
    vasya - petya = 14
    vasya = vasya + petya - 18
    return vasya, petya
'''
def skorost():
    v1 = 60
    v2 = -15
    t = 2
    vsblizh = v1-v2
    s = vsblizh*t
    return s

def poezd():
    a = int(input('Первая скорость: '))
    b = int(input('Вторая скорость: '))
    v = 2*a*b/(a+b)
    return v

def dvoichaya():
    while True:
        dva = input('Введите двоичное число(максимум 10000 разрядов): ')
        try:
            int(dva, base = 2)
            break
        except ValueError:
            print('Неправильный ввод')
            continue
    counter = 0
    accumulator = 0
    if len(dva) % 4 != 0:
        dva = (4 - (len(dva) % 4)) * '0' + dva
    for _ in range(int(len(dva)/4)):
        accumulator += int(dva[counter : counter + 4], base = 2)
        counter += 4
    if accumulator % 15 == 0:
        return 'Число кратно 15'
    else:
        return 'Число не кратно 15'

def tochki():
    x1 = int(input('x1: '))
    y1 = int(input('y1: '))
    x2 = int(input('x2: '))
    y2 = int(input('y2: '))
    x3 = int(input('x3: '))
    y3 = int(input('y3: '))
    k = (y2-y1)/(x2-x1)
    b = -x1*(y2-y1)/(x2-x1)+y1
    check1 = y2 >= y3 and y3 >= y1
    check2 = y1 >= y3 and y3 >= y2
    if y3 == k*x3+b:
        if check1 or check2:
            return 'Точка попадает в промежуток'
        else:
            return 'Точка не попадает в промежуток'
    else:
        return 'Точка не попадает в промежуток'

def tochki2():
    x1 = int(input('x1: '))
    x2 = int(input('x2: '))
    y1 = int(input('y1: '))
    y2 = int(input('y2: '))
    z1 = int(input('z1: '))
    z2 = int(input('z2: '))
    k = (y2-x2)/(y1-x1)
    b = -x1*(y2-x2)/(y1-x1)+y1
    k1 = -1/k
    b1 = z2 + 1/k*z1
    p1 = (b1-b)/(k-k1)
    check1 = x1 >= p1 and p1 >= y1
    check2 = y1 >= p1 and p1 >= x1
    if check1 or check2:
        return 'Точка попадает в промежуток'
    else:
        return 'Точка не попадает в промежуток'

print(dvoichaya())

