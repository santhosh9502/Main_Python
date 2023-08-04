# table creating
# def table(n,t):
#     if n != 0:
#         table(n-1,t)
#         print(n,'*',t,"=",n * t)
    
# n = int(input("enter the num: "))
# t = int(input("enter the table: "))
# table(n,t)

# factorial
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# n = int(input("enter the num: "))
# res = fact(n)
# print(res)

""" REVERSE A SRING USING RECURSION """
# def rev(string):
#     if len(string) == 0:
#         return string
#     else:
#         return rev(string[1:]) + string[0]

# strings = input("enter the string to reverse: ")
# res = rev(strings)
# print(res)