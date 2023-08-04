temp = float(input("Enter the temperature in Celsius: "))
if temp < -273.15:
    print("INVALID")
elif temp == -273.15:
    print("The temperature is absolute 0.")
elif 0 > temp >= -273.15:
    print("The temperature is below freezing.")
elif temp == 0:
    print("The temperature is at the freezing point.")
elif 0 < temp < 100:
    print("The temperature is in the normal range.")
elif temp == 100:
    print("The temperature is at the boiling point.")
else:
    print("The temperature is above the boiling point.")
