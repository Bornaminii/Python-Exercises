n = int(input('Enter the number:'))

length = 1

while n > length:
    n -= length
    length += 1

if n == 1:
    print(1)
else:
    print(0)