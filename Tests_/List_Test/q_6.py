l = []
for i in range(5):
    n = int(input("enter num:"))
    l.append(n)
print(l)
pro = (l[0::2])
print(pro)

for i in pro:
    print(i, end = " ")
res = (pro[0]*pro[1]*pro[2])
print(res, end= " ")