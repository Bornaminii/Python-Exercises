n = int(input(('Enter Your Number: (1 <= n <= 19):')))

if 1 <= n <= 19:
    for i in range(n):
        if i <= n // 2:
            spaces = n // 2 - i
            stars = 2 * i + 1
        else:
            spaces = i - n // 2
            stars = 2 * (n - i) - 1

        middle_spaces = n - stars

        print(" " * spaces + "*" * stars + " " * middle_spaces + "*" * stars)
else:
    print('Your number is not in range(1 <= n <= 19)')