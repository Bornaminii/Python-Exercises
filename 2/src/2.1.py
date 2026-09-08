n = int(input('Enter number of students:'))

female_names = {}
male_names = {}

for i in range(n):
    name, gender = input('Enter the name and Gender (M/F)').split()

    if gender == "F":
        if name in female_names:
            female_names[name] += 1
        else:
            female_names[name] = 1

    else:
        if name in male_names:
            male_names[name] += 1
        else:
            male_names[name] = 1


female_result = sorted(female_names, key=lambda name: (-female_names[name], name))[0] #

male_result = sorted(male_names, key=lambda name: (-male_names[name], name))[0] #

print(female_result)
print(male_result)