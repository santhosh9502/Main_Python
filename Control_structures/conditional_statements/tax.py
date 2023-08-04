salary = int(input("Enter the Salary: "))

if salary <= 500000:
    tax = 0
    print(f"your tax is {tax}")
elif salary <= 1000000:
    tax = (salary - 500000) * .2
    print(f"your tax is {tax}")
else:
    tax = (salary - 1000000) * .3
    print(f"your tax is {tax}")
