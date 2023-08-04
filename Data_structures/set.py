# remove duplicate item
# s = {1,2,3,4,5,4,3,5,7,8}
# print(s)

# ADD()
# s = {2,5}
# s.add(1) # add function add the given value in "sort order like {1,2,3,4}"
# print(s) # output is {1,2,5}

# REMOVE()
# s = {3,4,5}
# x = 4
# s.remove(x)
# print(s) # removes the given number/string

# a = "learn"
# b = "about"
# c = "string"
# d = "variable"
# res = c[3] + " " + a[0] + b[2] + d[0] + a[1] + " " + b[-2]
# print(res)

# HASH()
# print(hash(3))
# print(hash(500.57))
# print(hash('Hyderabad'))
# print(hash(True))

# UNION()
# s1 = {1,2,3,4}
# s2 = {5,7,8,9}
# s3 = {6,2,4,9}
# # print(s1 | s2 | s3) # also we can use this method
# s4 = s1.union(s2,s3)
# print(s4) # similar as extend() with sorting and kill duplicate values

# INTERSECTION()
# s1 = {2,3,4,5}
# s2 = {2,5,4,8,9}
# s3 = {3,4,5,7,8}
# print(s1 & s2 & s3) # optional to use this method
# s4 = s1.intersection(s2,s3)
# print(s4)

# DIFFERENCE()
# s1 = {3, 4, 5, 6}
# s2 = {5, 9, 6, 8}
# print(s1-s2) # Elements that are present in one set but not in the other,o/p is {3,4}
# print(s2-s1) # o/p is {8,9}
# s3 = s1.difference(s2)
# s3 = s2.difference(s1)
# print(s3) # o/p is {3,4}
