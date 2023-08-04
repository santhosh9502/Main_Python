# 
# def func(x,y,z=5):
#     print(x,y,z)
# func(1,z=2,y=3)
# # 
# def rec(a,b):
#     if a == 0:
#         return b
#     else:
#         return rec(a -1, a + b)
# print(rec(8,12))
# 
# def add(x, y=0, z=0): # default arguments
#     s = x + y + z
#     return s
# print(add(4)) # y, z takes default value 0
# print(add(4, 5)) # y's default value replaced by the actual argument value 5 and z takes default value 0
# print(add(4, z=5)) # y takes default value 0 and z's default value replaced by the actual argument, 5

# def x(values):
#     values[0] = 1
# v = [2,3,4]
# x(v)
# print(v)

# def func(x,y,z=4):
#     s = x+y+z
#     return s
# print(func(1,2))
# print(func(2,3,9))

# a = input("enter the num1: ")
# b = input("enter the num2: ")
# c = input("enter the num3: ")
# def max(a,b,c):
#     def max2(x,y):
#         return x if x > y else y
#     return max2(a,max2(b,c))

# print(max(a,b,c))

# def fun(a,b):
#     add = a + b
#     sub = a - b
#     pro = a * b
#     return add,sub,pro

# print(fun(3,2))

""" LAMBDA """
mylist = [2,5,6,7,8,9]
res = list(map(lambda x: x*x,mylist))
print(res)

# 
