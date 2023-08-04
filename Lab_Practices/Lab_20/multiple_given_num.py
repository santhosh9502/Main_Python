def multiplies(n):
    for i in range(1,201):
        if i % n == 0:
            print(i)

n = int(input("enter the num: "))
multiplies(n)