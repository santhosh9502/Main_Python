# 3. Write a program to remove all tuples from a list where the second element of the tuple is even
l = []
n = int(input("enter the num: "))
for i in range(n):
    str = input("enter the str: ")
    ip = int(input("enter the num: "))
    res = (str,ip)
    l.append(res)
    print()
print(l)
r = []
for j in l:
    if j[1] % 2 != 0:
        r.append(j)
print(r)
