n = int(input('Enter the number of offerings :'))

codes = []
duplicates = []

for i in range(n):
    code = input('Enter the National code :')

    if code in codes:
        if code not in duplicates:
            duplicates.append(code)
    else:
        codes.append(code)

for code in duplicates:
    print(code)