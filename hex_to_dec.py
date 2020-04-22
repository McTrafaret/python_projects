import sys

hex_number = sys.argv[1]
binary = ''
for digit in hex_number:
    bit = ''
    dec = int(digit, base = 16)
    for _ in range(4):
        bit += str(dec % 2)
        dec = dec // 2
    bit = bit[::-1]
    binary += bit

sign = int(binary[0])
out = binary
if sign:
    out = ''
    print('-', end='')
    for bit in binary:
        out += str(int(not int(bit)))

print(int(out, base = 2) + 1)
