                # TEST_3
# 1
l = [5,-1,-2,0,3]
l1 = 0
for i in l:
    if i < 0:
        l1 += 1
print(l1)

# 2
L = [1, 2, 3, 4]
num = 2
res = []
for i in L:
    if i > num:
        res.append(True)
    else:
        res.append(False)    
print(res)

# 3
l = [7, 5, 5, 1, 6, 7, 8, 7, 6]
c = []
for i in l:
    if l.count(i) == 1:
        c.append(i)
print(c)

# 4
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low_spendings = []
normal_spendings = []
high_spendings = []

for i in spendings:
    if i < 1000.0:
        low_spendings.append(i)
    elif 1000.0 < i < 2500.0:
        normal_spendings.append(i)
    elif i > 2500.0:
        high_spendings.append(i)
print(f"No.of.Months with Low spendings are {low_spendings}")
print(f"No.of.Months with Normal spendings are {normal_spendings}")
print(f"No.of.Months with High spendings are {high_spendings}")

# 5
l = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
]

count = 0
t_time = 0

for i in l:
    if i[1] == "Rome":
        count += 1
        # t_time += l[2]

# 6
statuses = {
            "Alice": "online", 
            "Bob": "offline", 
            "Eve": "online", 
            "Ravi": "online", 
            "sneha": "offline", 
            "vinod": "online", 
            "dheepika": "online"
}
online = 0
# offline = 0
for i in statuses.values():
    if i == "online":
        online += 1
print(f"{online} employees are working online")

# 7
str = input("enter the string: ")
words = str.split()
d = {}
for i in words:
    d[i] = len(i)
    # x = len(i)
    # if x in d:
    #     d[x] += 1
    # else:
    #     d[x] = 1
print(d)
