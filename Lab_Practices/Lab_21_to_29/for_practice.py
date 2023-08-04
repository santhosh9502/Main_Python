# this is wrong for me
s = 5
e = 9
# while s <= e:
#     for i in range(5, 9):
#         print(i, end=" ")
#     print()
#     e -= 1

for i in range(8,4,-1):
    for j in range(5,i+1):
        print(j, end=" ")
    print()
