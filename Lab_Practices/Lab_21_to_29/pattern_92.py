s = 5
for i in range(5, 0, -1):
    for j in range(5, s - i, -1):
        print(j, end=" ")
    print()
