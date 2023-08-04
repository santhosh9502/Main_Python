# marital_status = input("Married (Y/N): ").lower()
Age = int(input("Enter the age: "))
Gender = input("Gender (M/F): ").lower()

if Gender == 'f':
    print("You will work only in Urban areas")
elif Gender == 'm':
    if 20 < Age < 40:
        print("You can work in anywhere")
    elif 40 < Age < 60:
        print("You can work only in Urban areas")
    else:
        print("ERROR")
