s = 5
for i in range(1, 6):
    for j in range(5, s - i, -1):
        print(j, end=" ")
    print()
