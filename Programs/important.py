# NEW PROJECTS

# len() calculate the length of the words
a = "Quality Matrix"
print(len(a))

#len()2
x = "\n"
print(len(x))

# len()3
x = 'it\'s ok'
print(len(x))

# capital & Small Letter
a = "dream project"
print(a.upper()) # The whole content transform into capital words
print(a.lower()) # The whole content transform into lowercase values
print(a.title()) # This only transform all starting values into capital words
print(a.capitalize()) # This only transform starting values into capital words

# ID()
x = input("enter the value x: ")
y = input("enter the value y: ")
print(id(x)) # this will give address of the given value
print(id(y)) # this will give address of the given value

# COUNT
s = "Hello World!"
print(s.count('o'))

# replace words
x = "Saravana Raja"
x1 = x.replace('a','#')
print(x1)

# Reverse the words
s = "Once upon a time in India, there was a king called Sultan. India was a great country."
word = 'king'
print(s.replace(word, word[::-1]))

# Remove spaces
a = " Dream Project! "
print(a.strip())

# "lstrip()" Removes only front spaces
s = ' saravana raja '
s1 = s.lstrip() # Removes only leading whitespaces from string
print(s1)
print(s)

# "rstrip()" Removes only last spaces
s = ' raja saravana '
s1 = s.rstrip() # Removes only tailing whitespaces from string
print(s1)
print(s)

# USING OF STRIP()
s = '$$$Telangana'
s1 = s.strip('$')  # Removes leading and tailing $'s from string
s2 = s.strip('na$g') # Removes leading and tailing n's, a's, $'s and g's from string
print(s1)
print(s2)
print(s)

# "split()" split strings
a = "Don't,judge,the,book,by,its,cover"
b= a.split(" ")
print(b)

# boolean
a = 12
b = 20
if a > b:
    print("true")
else:
    print("false")

import keyword
print(keyword.kwlist)

# input value in console
x = int(input("Enter the x value: "))
y = int(input("Enter the y Value: "))
print(x + y)

# input value
x = input()
print(type(x))

# Name Adding
name = "Charlie"
txt = "Welcome {}"
print(txt.format(name))

# Words Combining
name = "abc"
roll_no = 123
branch = "xyz"
txt = ("Hey, my name is {} and my roll number is {}. My branch is {}")
print(txt.format(name,roll_no,branch))
print(f"Hey, my name is {name} and my roll number is {roll_no}. My branch is {branch}")

# Type Conversions
print(bin(2345)) # converting decimal to binary
print(oct(0xea)) # converting hexadecimal to octal
print(hex(0o234)) # converting octal to hexadecimal

# binary to decimal
x = int(0o00101101)
print((x))

# float
x = 20
y = 50
z = x/y
print(z,type(z))

# to find avg numbers
a = int(input('Enter 1st Number : '))
b = int(input('Enter 2nd Number : '))
sum = a + b
avg = sum / 2
print('Sum of all 2 Numbers is  {}'.format(sum))
print('Average of all 2 Numbers is  {}'.format(avg))

# square root of number
x = 12
print(x**2)

num = 55
num +=3
print(num)

#
x = "Hello "
y = "World"
print(x+y)
