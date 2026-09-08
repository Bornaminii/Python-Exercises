n = int(input('Enter your Passkey (1 <= n <= 26):'))
text = input('Enter your text :')

result = ""

if 1 <= n <= 26:
    for char in text:
        if char.isalpha():

            if char.islower():
                new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a')) #

            else:
                new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A')) #

            result += new_char

        else:
            result += char
else:
    print('Your number is not in range(1 <= n <= 26)')

print(result)