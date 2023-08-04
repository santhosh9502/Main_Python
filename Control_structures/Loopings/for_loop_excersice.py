"""FOR LOOP QUESTION"""
"""1.Write a program that prompt the user for their name and how many times to print it. 
The program should print out the user’s name the specified number of times."""
# name = input("enter the name: ")
# c = int(input("how many times to add: "))
# for i in range(c):
#     print(name)

"""2.Write a program that prompt the user for a string and prints out all the location(index) 
of each 'a' in the string. If 'a' doesn't exist, print "None"."""
# name = input("user value: ")
# res = []
# for i in range(len(name)):
#     if name[i] == 'a':
#         res.append(i)
#         print(res)
# if res != 'a':
#     print("none")
# else:
#     print(f"\'a\' is in the variable are {res}")

""" 3.Write a program that prompt the user for their name and prints it in the funny pattern as 
given in the example below.
# Sample Input
Python
# Expected Output
P Py Pyt Pyth Pytho Python"""
# name = input("Enter your name: ")
# for i in range(len(name) + 1):
#     print(name[0:i])

"""4.Write a program that prompt the user to enter a word and then capitalizes every other letter of that word.
# Sample Input
rhinoceros
# Expected Output
rHiNoCeRoS""" 
# name = input("enter your name: ")
# cap = ""
# for i in range(len(name)):
#     if i % 2 == 0:
#         cap += name[i].lower()
#     else:
#         cap += name[i].upper()
# print(cap)

"""5.Write a program that prints out all the integers from 1 to 20 and their squares.
# Expected Output
1 --- 1
2 --- 4
3 --- 9
...
20 --- 400"""
# for i in range(1,21):
#     print(i,i ** 2)

"""6.Write a program to read a line of text as input from the user and
print the count of space characters(' ') in the text entered. Sample Input
Python is the most powerful language you can still read. Expected Output 9"""
# text = input("enter the text: ")
# c = 0
# for space in text:
#     if space == ' ':
#         c+=1
# print(c)

"""7. Write a program that uses a 'for' loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89.""" 
# for i in range(8,90,3):
#     print(i,end=" ")

"""8. Write a program that uses a 'for' loop to print the numbers 100, 98, 96, . . . , 4, 2."""
# for i in range(100,1,-2):
    # print(i,end=" ")

"""9. Write a program that uses a 'for' loop to print numbers from 10 to 1 in descending order."""
# for i in range(10,0,-1):
#     print(i)

"""10. Write a program that counts how many of the squares of the numbers from 1 to 1000 end in a 1."""
# count = 0
# for i in range(1, 1001):
#     square = i ** i
#     if square % 10 == 1:
#         count += 1
# print("There are", count, "squares.")

"""11.Write a program that counts how many of the squares of the numbers from 1 to 1000
end in a 4 and how many end in a 9"""
# c = 0
# c_2 = 0
# for i in range(1,1001):
#     sqt = i ** i
#     if sqt % 10 == 4:
#         c += 1
#     elif sqt % 10 == 9:
#         c_2 += 1
# print("There are", c, "squares.")
# print("There are", c_2, "squares.")

"""12. Write a program to find all numbers between 1 and 1000 that are divisible by 7 and end in a 6."""
# for i in range(1,1001):
#     if i % 7 == 0:
#         if i % 10 == 6:
#             print(i)

"""13. Write a program to determine how many of the numbers between 1 and 10000 contain the digit 3"""
# for i in range(1,10001):
#     if i % 10 == 3:
#         print(i)
#
"""14. Write a program that creates the list [1,11,111,1111,...,111...1], 
where the entries have an ever increasing number of ones, with the last entry having 100 ones.""" 
# list = []
# for i in range(1,101):
#     one = i * '1'
#     list.append(one)
#     i+=1
# print(list)

"""15. Write a program to display the stars in an equilateral triangular form using a single for loop."""
# c = 5
# for i in range(1, 6):
#     print(' ' * c,end='')
#     print('* ' * i)
#     c -= 1


# 3 unconditional statements
# l = [1,2,0,3,4,5,7]
# res = 0
# for i in l:
#     if i == 0:
#         break
#     else:
#         res += i
# print(res)

# 4th 
# l = [1,2,3,4,5,6,7,8,9,10]
# res = ""
# for i in l:
#     if i % 2 == 0:
#         res = i * 3
#         continue
#     print(res)