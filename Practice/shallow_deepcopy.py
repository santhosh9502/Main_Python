a = [[1,2,3],[4,5,6,[20,33]],[7,8,9]]
# b = a
a[1][3][1] = 10

# print(a)
# print(b)
# print()
print("---------$-------")

# Shallowcopy
import copy
b = copy.copy(a)
print(a)
# print(b)
a[2] = 22
print(a)
# print(b)
print(id(a[2]))
print(id(a))
print(b)
print(id(b)) 

# print(id(a[1])) # In here ID values of given variables got not changed because of Normal copy
# print(id(b[1])) # In here ID values of given variables got not changed because of Normal copy 
print("-------------------")

# DEEPCOPY
b = copy.deepcopy(a)
print(a)
print(id(a)) # In here Each and every ID values of he variables got changed because of DEEPCOPY without changes in ORIGINAL Variables
print(id(a[0])) # In here Each and every ID values of he variables got changed because of DEEPCOPY without changes in ORIGINAL Variables
print(b)
# print(id(b)) # In here Each and every ID values of he variables got changed because of DEEPCOPY without changes in ORIGINAL Variables
# print(id(b[0])) # In here Each and every ID values of he variables got changed because of DEEPCOPY without changes in ORIGINAL Variables