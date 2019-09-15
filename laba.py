string = '50 72 6F 67 72 61 6D'
lis = string.split(' ')
print(lis)
for i in lis:
    print(chr(int(i, base = 16)), end = '')
