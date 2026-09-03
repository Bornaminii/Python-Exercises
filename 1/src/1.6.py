n = int(input(('Enter Your Number: (1 <= n <= 100):')))

if 1 <= n <= 100:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end=" ")
        print()
else:
    print('Your number is not in range(1 <= n <= 100)')