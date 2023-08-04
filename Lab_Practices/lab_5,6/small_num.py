num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number: "))

if(num1<num2):
    print(f"this is smallest {num1}")
elif(num2<num1):
    print(f"this is smallest {num2}")
else:
    print(f"num1 and num2 are equal {num1,num2}")