
#\ FOR LOOP
n = 11
for i in range(1,n):
    print(i)

#\ even numbers in for loop
num = 11
for i in range(num):
    if i % 2 == 0:
        print(i)

#\ sum the odd numbers in given range
num = 21
for i in range(num):
    if i % 2 != 0:
        print(i)

#\ for loop in LIST
list = [1,2,3,4,5]
for i in list:
    print(i)

#\for loop pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

# ALPABETICAL PATTERNS
for i in range(65,70):
    k=i
    for j in range(65,i + 1):
        print(chr(k),end=" ")
        k += 1
    print()

# 
for i in range(65,70):
    for j in range(65,i + 1):
        print(chr(i),end=" ")
    print()

# 
for i in range(65,70):
    for j in range(65,i + 1):
        print(chr(j),end=" ")
    print()


# test
# 4
for i in range(6):
    name = input("enter the name: ")
    print(name)
# 1
for i in range(-20,-9,2):
    print(i,end=" ")
    print()
# 2
for i in range(2,21,2):
    print(i,end=" ")
    print()
# 3
for i in range(3,20,2):
    print(i,end=" ")
    print()

# 16 th QUESTION
val = input("enter the value: ")
res = val[0]
for i in range(1,len(val)):
    if val[i] != res[-1]:
        res+=val[i]
    # print(res)
print("----------")
print(f"the final value is \"{res}\"")

for i in range(9,0,-2):
    for j in range(9,9-i,-2):
        print(j,end=" ")
    print()
