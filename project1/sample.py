list1 = [1, 2, 3, 2, 4, 2, 3, 4, 3, 5, 6]
list2 = [1, 5, 3]
dict1 = {}

for i in list1:
    if i in list2:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

print(dict1)
