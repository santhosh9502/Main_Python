l = input("enter the string: ")
# l = "HeLlO"
l1 = []
for i in range(len(l)):
    if l[i].isupper(): # return "True" if there is capital oterwise return "False"
        l1.append(i)
print(l1)