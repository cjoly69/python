list_test = [1, 2, 3, 4, 5, 6]
tuple_test = (1, 2, 3)

print(len(list_test))  # =>6
print(max(list_test))  # =>6
print(min(list_test))  # =>1
print(list(tuple_test))  # =>[1, 2, 3]
print(list_test.append(7))  # =>[1, 2, 3, 4, 5, 6,7]
print(list_test.pop())  # =>[1, 2, 3, 4, 5]
print(list_test.remove(2))  # =>[1, 3, 4, 5, 6]

#  éviter les erreurs lors de saisies utilisateurs en particulier
try:
    list_test.remove(9)
except ValueError:
    print("element introuvable")

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

L1 * 2  # = [1, 2, 3, 4, 1, 2, 3, 4] (Repetition)
L1 + L2  # = [1, 2, 3, 4, 5, 6, 7, 8] (Concaténation)
print(2 in L1)  # affichera True. (Membership)

# tuple

tupleT = (1, 2, 3, 4, 5, 6, 7)
print(tupleT[1:])  # => (2,3,4,5,6,7)
print(tupleT[:4])  # => (1,2,3,4)
print(tupleT[1:5])  # => (2,3,4)
print(tupleT[0:6:2])  # =>(1,3,5)
