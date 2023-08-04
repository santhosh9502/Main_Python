l = []
for i in range(5):
    n = int(input("enter num:"))
    l.append(n)
print(l)
sum = (l[0::2])
print(sum)

for i in sum:
    print(i, end = " ")
res = (sum[0]+sum[1]+sum[2])
print(res, end= " ")