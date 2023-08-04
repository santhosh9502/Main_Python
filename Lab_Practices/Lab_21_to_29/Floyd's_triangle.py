# for loop
s = 1
for i in range(1,5):
    for j in range(i):
        print(s, end=' ')
        s += 1
    print()

# while loop
num = 1
i = 0
while i < 4:
    j = 0
    while j < i+1:
        print(num,end=" ")
        num = num+1
        j = j+1
    print()
    i = i+1