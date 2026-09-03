text = input('Enter Your Text:')

result = ""

for char in text:
    if char == " ":
        result += "_"
    else:
        result += char

print(result)

# --------------------------------------------------------------

# text = input()

# text = text.replace(" ", "_")

# print(text)