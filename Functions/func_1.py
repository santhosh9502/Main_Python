""" Basics of function """
# def deco(func):
#     def intro():
#         print("Hai")
#         func()
#         print("Welcome to my Home")
#     return intro
# @deco
# def greet():
#     print("Hello")
    
# greet = deco(greet)
# print(greet.__name__)

""" Function as a Parameter """
# def fun1():
#     print('this is function-1')
# def fun2(ref):
#     ref()
#     print('this is function-2')
    
# fun2(fun1)

""" FROM START """
# n = 5
# f = 1
# for i in range(1, n+1):
#     f = f * i
# print(f)

""" NCR """
""" nCr = n!/(n-r)! * r! """
# def fact(a):
#     f = 1
#     for i in range(1,a+1):
#         f = f * i
#     return f
# def nCr(n,r):
#     res = fact(n)/(fact(n-r) * fact(r))
#     return res
# print(f"nCr: ",nCr(5,2))

""" lambda """
# def fun():
#     return "Hai Welcome to India"
# print((lambda: fun())())
# def fun(name):
#     lambda name: f"correct" if name[0]== "A" or name[0]== "a" else "wrong"
#     return name

# print(fun("raja"))
# print(fun("anu"))


"""decorator"""
# def deco(func):
#     def deco1(text):
#         res = func(text)
#         return res.upper()
#     return deco1

# @deco
# def result(name):
#     return f"My name is {name}"
# print(result("Raja"))

""" *args """
# def demo(*args):
#     for i in args:
#         print(i)

# demo(10,20,30,40,50,60)

""" **kwargs """
# def demo1(**kwargs):
#     for i in kwargs.items():
#         print(i)

# demo1(a=20,b=55,c=77,d=44)

""" MAP() """
def maps(a,b):
    return a*b

res = map(maps,[1,2,3],[5,3,2])
print(list(res))

""" FILTER() """
def maps1(i):
    if i >= 3:
        return i

res = filter(maps1,[1,0,3,2,12,32,9])
print(list(res))    
# 
score = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def student(marks):
    return marks > 75

res = set(sorted(filter(student, score)))
print(res)

""" reduce() """
from functools import reduce
def fun2(a,b):
    return a * b

res = reduce(fun2,[1,6,5,4])
print(res)
