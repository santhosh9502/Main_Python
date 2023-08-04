# Write a program to find the sum of even ‘n’ natural numbers.
n = int(input("Enter the value of n: "))
if n <= 0:
    print("Invalid input. n should be a positive integer.")
else:
    total = n * (n + 1)
    print(f"The sum of {n} even natural numbers is: {total}")
    
