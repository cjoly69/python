test1 = (1, 2, 2, 3, 4, 3, 9, 3)
unique = []
# print(set(test1))
for i in test1:
    if i not in unique:
        unique.append(i)
    else:
        print('bye')
        print(unique)