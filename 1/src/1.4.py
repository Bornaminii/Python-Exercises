word = input('Enter Your Word:')

for i in range(len(word)):
    result = ""

    for j in range(len(word)):
        if j <= i:
            result += word[i]
        else:
            result += word[j]

    print(result)