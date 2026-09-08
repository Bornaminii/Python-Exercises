n = int(input('Enter your number (1 <= n <= 45):'))

if 1 <= n <= 45:
    if n == 1 or n == 2:
        print(2)
    else:
        a = 2
        b = 2

        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        print(b)
else:
    print('Your number is not in range(1 <= n <= 45)')