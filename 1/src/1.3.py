n = int(input('Enter Your Number: (1 <= n <= 100):'))

if 1 <= n <= 100:
    for i in range(1, n + 1):
        spaces = n - i
        stars = (i * 2) - 1

        print(" " * spaces + "*" * stars)
else:
    print('Your number is not in range(1 <= n <= 100)')