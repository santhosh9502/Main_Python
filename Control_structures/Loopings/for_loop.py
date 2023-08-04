# FOR LOOP

# string Iteration
a = "Raja"
for i in a:
    print(i)

# List Iteration
a = ['raja','from','tamilnadu']
for i in a:
    print(i)

# tuple Iteration
a = ("Programming", "is", "fun")
for i in a:
    print(i)

for i in range(6):
    print(i, end=" ")
print()

# star pattern
for i in range(1,6):
    print(i * "* ")
print("----------------")

# star pattern in reverse
for i in range(5,0,-1):
    print(i * "* ")

# number pattern
for i in range(1,6):
    for j in range(1,i + 1):
        print(j, end=" ")
    print()
print("--------------------")

#
# for i in range(1,6):
#     for j in range(1,i + 1):
#         print(i, end=" ")
#     print()

# patterns
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = " ")
    print("")
print("--------------------")

#/* star program in reverse *\
for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print("")
print("---------------------")

n = int(input("Enter num value: "))
rt = int(n**0.5)

for i in range(2, rt+1):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

#
for i in range(4):
    for j in range(3):
        print(i,"*",j,"=",i*j)
# -------------#

# test
for i in range(8,4,-1):
    for j in range(5,i+1):
        print(j,end=" ")
    print()

s=0
for i in range(5,10):
    for j in range(5,10-s):
        print(j,end=" ")
    print()
    s+=1
# 
res=0
name = input("enter the name: ")
for i in name:
    print(ord(i),i)
    res += ord(i)
print(res)
# 

t = (3, 5, 4, 2, 1)
t=list(t)
t.insert(3,3)
print(t)

l = [('Apple', 30), ('Grape', 20), ('Mango', 25), ('Peach', 35)]
for fruit,count in l:
    if count < 30:
        print(fruit,count)

# This is from my old file in "PY works folder" 
# list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# s = []
# n = 3
# for i in range(n):
#     s.append(list[i::n])
# print(s)
