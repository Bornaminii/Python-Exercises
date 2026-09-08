n, t = map(int, input('Enter the number and time (1 <= n <= 50):').split())
s = list(input('Enter the list of children (G/B)'))

if 1 <= n <= 50:
    for x in range(t):
        i = 0

        while i < n - 1:
            if s[i] == 'B' and s[i + 1] == 'G':
                s[i], s[i + 1] = s[i + 1], s[i]
                i += 2
            else:
                i += 1

    print(''.join(s))
else:
    print('Your numbers is not in range(1 <= n <= 50)')

