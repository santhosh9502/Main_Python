sum = 0
i = 1
while i <= 10:
    num = int(input("enter the num: "))
    if num >= 0:
        sum = sum + num
        i += 1
    else:
        print(f"Invalid number.")
print(f"the sum of number is {sum}")
