calls = int(input("enter the no.of.calls: "))

if calls <= 100:
    bills = 200
elif calls <= 150:
    bills = 200 + (.6 * (calls - 100))
elif calls <= 200:
    bills = 200 + (.6 * 50 + .5 * (calls - 150))
else: 
    bills = 200 + (.6 * 50 + .5 * 50 + .4 * (calls - 200))
print(f"telephone bill is {bills}")

# calls = calls - 100