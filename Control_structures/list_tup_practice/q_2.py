# 2. Write a program to iterate over a list of tuples and print out the first element of each tuple

l= []
t = 2
for i in range(t):
    str = input("enter the string: ")
    ip = int(input("enter the num: "))
    res = (str[0],ip)
    l.append(res)
print(l)