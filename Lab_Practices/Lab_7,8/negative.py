while True:
    num = int(input("Enter a +ve number: "))
    if num < 0:
        break
    else:
        print(f"You entered: {num}")
print("You gave a -ve number.")
