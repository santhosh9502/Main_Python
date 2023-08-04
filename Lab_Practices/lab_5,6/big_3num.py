num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))
num3 = float(input("Enter the num3: "))

if (num1 > num2) and (num1 > num3):
    print("1st is biggest")
elif (num2 > num1) and (num2 > num3):
    print("2nd is biggest")
else:
    print("3rd is biggest")