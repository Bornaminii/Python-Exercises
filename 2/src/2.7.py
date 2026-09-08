sizes = ["S", "M", "L", "XL", "XXL"]

stock = list(map(int, input("Enter the number of shirts: ").split()))

n = int(input("Enter the number of participants: "))

for x in range(n):
    wanted = input("Enter the wanted size: ")

    wanted_index = sizes.index(wanted)

    if stock[wanted_index] > 0:
        print(wanted)
        stock[wanted_index] -= 1
        continue

    best_index = -1
    best_distance = 100

    for i in range(5):
        if stock[i] > 0:
            distance = abs(i - wanted_index)

            if distance < best_distance:
                best_distance = distance
                best_index = i

            elif distance == best_distance and i > best_index:
                best_index = i

    if best_distance > 2:
        print("No Shirt")
    else:
        print(sizes[best_index])
        stock[best_index] -= 1