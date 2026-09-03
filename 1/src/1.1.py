n = int(input('Enter Your Number: (1 <= n <= 1000000):'))

i = 2
if 1 <= n <= 1000000:
    while n > 1:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i += 1
else:
    print('Your number is not in range(1 <= n <= 100000)')