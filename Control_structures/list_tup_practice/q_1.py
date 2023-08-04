# 1. Create a list of tuples where each tuple contains a string and an integer. Print out the list
l = []
t = int(input("Enter the number of tuples: "))
for i in range(t):
    str = input("Enter a string: ")
    inp = int(input("Enter an integer: "))
    res = (str, inp)
    l.append(res)
print(l)