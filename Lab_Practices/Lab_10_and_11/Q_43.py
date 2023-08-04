def add(a,b):
    return a + b

def sub(a,b):
    return a -b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

print("""Select the Operation
      1.Add
      2.Sub
      3.Mul
      4.Div
""")

choice = input("enter the choice number: ")
a = int(input("enter the number 1: "))
b = int(input("enter the number 2: "))

if choice == '1':
    print(add(a,b))
elif choice == '2':
    print(sub(a,b))
elif choice == '3':
    print(mul(a,b))
elif choice == '4':
    print(div(a,b))
else:
    print("Invalid Choice, Please try again upto number 5.")