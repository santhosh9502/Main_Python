marital_status = input("Married (Y/N): ").lower()
Age = int(input("Enter the Age: "))
Gender = input("Gender (M/F): ").lower()

if marital_status == 'y':
    print("Driver is Insured")
elif marital_status == 'n':
    if (Age >= 30) and (Gender == 'm'):
        print("insured")
    elif (Age >= 25) and (Gender == 'f'):
        print("Insured")
    else:
        print("Your not Insured")
else:
    print("Driver is Not Insured")
