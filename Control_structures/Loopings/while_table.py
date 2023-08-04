# num = int(input("enter the num: "))
# i = 1

# while i <= 20:
#     print(i,"*",num,"=", num * i)
#     i += 1

# 
# para = []
# print("enter the para: ")

# while True:
#     line = input()
#     if line:
#         para.append(line)
#     break

# print(para)

"""while QUESTIONS"""
"""1.Write a 'while' loop that prints integers from zero to 5."""
# i = 0
# while i <= 5:
#     print(i,end=" ")
#     i+=1
# print()

""" 2.Write a 'while' loop that starts at the last character in the string and works its way backwards to the
first character in the string,printing each letter on a separate line, except backwards"""
# string = input("enter the word: ")
# res = len(string) - 1

# while res >= 0:
#     print(string[res])
#     res-=1

"""3.Write a program that asks the user to enter a number and prints out all the divisors of that number."""
# num = int(input("enter the num: "))
# i = 1
# while i <= num:
#     if num % i == 0:
#         print(i)
#     i+=1

"""6.Write a program to take integer inputs from user until he/she presses q and print the average 
and product of all those numbers"""




"""7.Write a program to print whether the given number is a palindrome or not"""
# content = input("enter the sentence: ")
# if content == content[::-1]:
#     print("this is palindrome")
# else:
#     print("this is not a palindrome")
