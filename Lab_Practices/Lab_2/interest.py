# SIMPLE INTEREST
principal = float(input("Enter the Principal: "))
time = int(input("Enter the time: "))
rate = float(input("Enter the rate: "))
n = int(input("Enter the N: "))

S_I = (principal*time*rate)/100
compound_interest = principal * (1+((rate/100)/n))**(n*time)

print(f"The Simple Interest is {S_I}")
print(f"The Compound Interest is {compound_interest}")