# Write a program that accepts a list from the user and check whether your list is having any element or empty.
l=[]
for i in range(6):
    n = int(input("user input: "))
    l.append(n)
print(l)
s = len(l)
if s > 0:
    print("not empty")
else:
    print("empty")
