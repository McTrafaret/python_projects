def isprime(number):
    if number <= 1: 
        print(str(number), 'is not prime', sep = ' ')
    else:
        x = number // 2
        while x > 1:
            if number % x == 0:
                print(str(number), 'is not prime', sep = ' ')
                break
            x -= 1
        else:
            print(str(number), 'is prime', sep = ' ')

isprime(0)