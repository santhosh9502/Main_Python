# Write a program that accepts a list from the user and print the alternate element of the list.

l = []
for i in range(5):
    s = int(input("enter the num: "))
    l.append(s)
print(l)
print(l[0::2])