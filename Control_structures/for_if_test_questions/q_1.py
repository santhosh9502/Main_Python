item = int(input("enter the num of item: "))

if item < 10:
    t_cost = item * 12
elif item <= 99:
    t_cost = item * 10
else:
    t_cost = item * 7

print(f"total cost is {t_cost}")