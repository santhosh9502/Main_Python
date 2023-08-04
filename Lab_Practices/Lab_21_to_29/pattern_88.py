rows = 5

for i in range(1, rows+1):
    for j in range(1, i+1):
        if j == i or j == 1:
            print(1, end=" ")
        else:
            print(i-1, end=" ")
    print()
