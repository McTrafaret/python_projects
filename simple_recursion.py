def func(counter):
    if counter == 0:
        print('stop')
    else:
        print(counter, end=' ')
        func(counter-1)

func(1)