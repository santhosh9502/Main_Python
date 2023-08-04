l = []
for i in range(5):
    n = int(input("enter the num: "))
    l.append(n)
print(l)
print(l[-1:] + l[:-1])