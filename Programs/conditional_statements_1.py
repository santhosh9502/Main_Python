# Conditional statements

# IF Condition
a = 2
b = 3
if a < b:
    print("True")

# If..Else Condition
a = int(input("num: "))
b = int(input("num_2: "))

if a > b:
    print("True")
else:
    print("False")

# Voting process using Conditions
Age = int(input("Enter the Age: "))

if Age > 18:
    print("You are Eligible to Vote")
else:
    print("You are Not Eligible to Vote")

# If..Elif Condition
# Match
match1 = float(input("Enter the 1st match points: "))
match2 = float(input("Enter the 2nd match points: "))
match3 = float(input("Enter the 3rd match points: "))

if match1 > match2 and match1 > match3:
    Winner = match1
elif match2 > match1 and match2 > match3:
    Winner = match2
else:
    Winner = match3
print(f"The Winner is", Winner)

# 2
text = input("Enter a line of text: ")
target = input("Enter the string to search for: ")
if target in text:
    print("True")
else:
    print("False")

# 3
word = input("Enter the Word: ")
vowels = ['a','e','i','o','u']
for letter in word:
    if letter in vowels:
        print("True")
    else:
        print("False")

# 4 (vowels / consonant)
word = input("Enter an alphabet: ")
vowels = "aeiouAEIOU"
if word in vowels:
    print("Vowel")
else:
    print("consonant")

# 5 (num find)
num = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if (num - num2) <= 0.001:
    print("Close")
else:
    print("Not close")

# 6 (age finding)
num1 = float(input("Enter the first age: "))
num2 = float(input("Enter the second age: "))
num3 = float(input("Enter the third age: "))

if (num1 > num2) and (num1 > num3):
    print("1st age is oldest")
elif (num2 > num1) and (num2 > num3):
    print("2nd age is oldest")
else:
    print("3rd age is oldest")
    
if (num1 < num2) and (num1 < num3):
    print("1st age is youngest")
elif (num2 < num1) and (num2 < num3):
    print("2nd age is youngest")
else:
    print("3rd age is youngest")

# 7

# 8 (leap year)
year = int(input("enter the year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# NEW IF...ELSE CONDIIONS
age = int(input("enter age:"))
if(age >= 1 and age < 18):
    print("User is a Kid")
elif(age >= 18 and age < 30):
    print("User is a Boy")
elif(age >= 30 and age < 80):
    print("User is a old")
elif(age >= 80 and age < 100):
    print(f"User is a senior citizen",age)
else: 
    print("User is Blessed",age)

# 10
for num in range(1500, 2700):
    if num % 7 == 0 and num % 5 == 0:
        print(num)

# 12
items = int(input("Enter the no.of.items: "))
if items < 10:
    cost = 12 * items
elif items >= 10 and items <= 99:
    cost = 10 * items
else:
    cost = 7 * items
print(f"the total cost is Rs. {cost}")

# 14
quantity = int(input("Enter the quantity of items: "))
unit_price = 100
total_cost = quantity * unit_price

if total_cost > 1000:
    total_cost = total_cost * 0.1

print("The total cost is:", total_cost)

