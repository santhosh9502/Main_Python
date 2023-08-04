# 4. Write a program to create a list of tuples where each tuple contains a string and the length of the string.
l = []
t = int(input("enter the num: "))
for i in range(t):
    str = input("enteer the string: ")
    res = (str,len(str))
    l.append(res)
    print()
print(l)