# 1
# l = list(range(3,100,3))
# print(l)

# 2
# l = ['a','b','c','d']
# k = ''.join(l)
# print(k)

# 3
# l = input("enter the str: ")
# print(list(l))

# 4
# color1 = ["Red", "Green", "Orange", "White"]
# color2 = ["Black", "Green", "White", "Pink"]
# l = []
# for color in color1:
#     if color in color2 and color2:
#         l.append(color)
# print(l)

# 5
# l1 = [1,2,3,4]
# l2 = [1,2]
# l = set(l1) - set(l2)
# print(list(l))

# 6
# l = [1,2,-8,0]
# print(max(l))

# 7


# 8
# list1 = [10,20,30,20,10,50,60,40,80,50,40]
# l2 = list(set(list1))
# print(sorted(l2))

# 9
# l = [1,2,-8]
# print(sum(l))

# 10
# l1 = [1, 2, 3, 4]
# res = 1
# for i in l1:
#     res *= i
# print(res)

# 11
# l = [2,4,3,9,13,12,7,6,1,5]
# even = sum(l[::2])
# odd = sum(l[1::2])
# print(even - odd)

# 12
# l1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# avg = sum(l1)/len(l1)
# res = []
# for i in l1:
#     if i > avg:
#         res.append(i)
# print(res)

# 13
# l1 = [3, 7, 11, 12, 17, 21]
# res = []
# for i in l1:
#     if i ** 2:
#         res.append(i)
# print(res)

# 14
# l1 = [5, 10, 15, 20, 25, 50, 20]
# l2 = l1.count(20)
# print(l2)

# 15
# l1 = [5, 10, 15, 20, 25, 50, 20]
# if 20 in l1:
#     index = l1.index(20)
#     l1[index] = 200
# print(l1)

# 16

# 17

# 18
# l0 = 7000
# l1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# l2 = l1[2][2][1] , l0
# print(l2)
