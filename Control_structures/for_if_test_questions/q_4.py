spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low_spend = 0
normal_spend = 0
high_spend = 0

for i in spendings:
    if i < 1000.0:
        low_spend += 1 
    elif i <= 2500.0:
        normal_spend += 1
    else:
        high_spend += 1
print(f"the spending is {low_spend,normal_spend,high_spend}")