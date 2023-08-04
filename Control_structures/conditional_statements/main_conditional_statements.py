"""REMOIVNG DUPLICATE FROM STRING"""
# string = input("enter the value: ")
# res = string[0]
# for i in range(len(string)):
#     if string[i]!= res[-1]:
#         res += string[i]
# print(res)

"""GETTING FIRST 2WORDS and LAST 2WORDS of the string"""
# name = input("enter the string: ")
# val1 = name[0:2]
# val2 = name[-2:]
# res = val1 + val2
# print(res)
 
"""IF CONDITION QUESTIONS"""
# 1. Write a program to accept a number from the keyboard and if the number is even, print "EVEN" otherwise print "ODD"
# val = int(input("enter the value1: "))
# if val % 2 == 0:
#     print("this is EVEN")
# else:
#     print("this is ODD")
# 2. Write a program to take a line of text and a string and print "True" if the string exits in the line of text otherwise print "False".
# text = input("enter text: ")
# line = input("enter line: ")
# if line in text:
#     print("TRUE")
# else:
#     print("FALSE")
# 3. Write a program that asks the user to enter a word and prints out whether that word contains any vowels.
# word = input("Enter the Word: ")
# vowels = ['a','e','i','o','u']
# for letter in word:
#     if letter in vowels:
#         print("True")
#     else:
#         print("False")
# 4. Write a program to check whether an alphabet is a vowel or consonant.
# word = input("enter the value: ")
# consonant = "aeiouAEIOU"
# if word in consonant:
#     print("true")
# else:
#     print("false")
# 5.Write a program that asks the user for two numbers and prints Close if the numbers are within .001 of each other and Not close otherwise
# num = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# if (num - num2) <= 0.001:
#     print("Close")
# else:
#     print("Not close")
# 6.Write a program to take input of age of 3 people from user and determine the oldest and the youngest among them
# p1 = int(input("enter the age of person1: "))
# p2 = int(input("enter the age of person2: "))
# p3 = int(input("enter the age of person3: "))
# if (p1 > p2) and (p1 > p3):
#     print("person1 is oldest")
# elif (p2 > p1) and (p2 > p3):
#     print("person2 is oldest")
# else:
#     print("person3 is oldest")
# if (p1 < p2) and (p1 < p3):
#     print("person1 is youngest")
# elif (p2 < p1) and (p2 < p3):
#     print("person1 is youngest")
# else:
#     print("person1 is youngest")

# 7.

# 8.Write a program to check whether the given year is leap year or not.
# year = int(input("enter the year: "))
# if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")
# 9.Write a program to check a triangle is equilateral, isosceles or scalene
# x = int(input("enter the 1st value: "))
# y = int(input("enter the 2st value: "))
# z = int(input("enter the 3st value: "))
# if x==y==z:
#     print("Equilateral triangle")
# elif x ==y or y == z or x== z:
#     print("Isoceles triangle")
# else:
#     print("Scalene triangle")
# 10.Write a program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
# for num in range(1500,2700):
#     if num % 7 == 0 and num % 5 == 0:
#         print(num)
"""11.Write a program to prompt the user for a temperature and what units (Celsius or Fahrenheit) 
the temperature is in and print the temperature by converting into the other unit. 
[Hint:- F = 95 C + 32 and C = 9 5 (F − 32)]"""

"""12.A store charges Rs.12 per item if you buy less than 10 items. If you buy between 10 and 99 items, 
the cost is Rs.10 per item. If you buy 100 or more items,the cost is Rs.7 per item.
Write a program that asks the user how many items they are buying and prints the total cost"""
# items = int(input("Enter the no.of.items: "))
# if items < 10:
#     cost = 12 * items
# elif items >= 10 and items <= 99:
#     cost = 10 * items
# else:
#     cost = 7 * items
# print(f"the total cost is Rs. {cost}")
"""13.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. 
Write a program that prompt the user for their salary and year of service and print the net bonus amount"""
# salary = float(input("Enter your salary: "))
# service = int(input("year of service: "))

# if service > 5:
#     bonus = salary * .05
#     net_bonus = salary + bonus

#     print(f"your bonus amount is {bonus}")
#     print(f"your net salary (including bonus) is: {net_bonus}")

# else:
#     print("Sorry you don't qualify for the bonus.")
"""14.A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Suppose, 
one unit will cost 100. Write a program to prompt the user for quantity and print the total cost for user"""
# quantity = int(input("Enter the quantity of items: "))
# unit_price = 100
# total_cost = quantity * unit_price

# if total_cost > 1000:
#     total_cost = total_cost * 0.1

# print("The total cost is:", total_cost)

"""MULTIPLE IF QUESTION"""
"""1.A student will not be allowed to sit in exam if his/her attendance is less than 75%. 
Write a program to take the number of classes held, the number of classes attended as inputs and 
calculate the percentage of class attended. If the user attendance is less than 75%, 
ask the user if he/she has medical cause or not ( 'Y' or 'N' ). If response is 'Y', 
print he/she is eligible to sit in the exam, otherwise print he/she is not eligible to sit in the exam."""
num_classes_held = int(input("Number of Classes held: "))
num_classes_atnd = int(input("Number of Classes attended: "))

atnd_perc = (num_classes_atnd / num_classes_held) * 100
print("Attendence percentage is ",atnd_perc)

if atnd_perc < 75:
    medical = input("Do you have the medical certificate? [Y / N]: ")
    if medical.upper() == 'Y':
        print("You are allowed to sit in the class")
    else:
        print("You are not allowed to sit in the class")
else:
    print("You are eligible to sit in he class")
