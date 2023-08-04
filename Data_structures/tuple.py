# lambda
# f = lambda x,y: x * y
# print(f(4,8))

# sorted based on salary
employees = [
    (1239, 'John', 23000, 25),
    (1235, 'Samantha', 13000, 21),
    (1238, 'Amanda', 45000, 30),
    (1237, 'Alex', 57000, 31),
    (1236, 'Vicky', 40000, 24)
]

sorted_records = sorted(employees, key = lambda x:x[3],reverse=True)
for rec in sorted_records:
    print(rec)

# def galla(name):
#     res = "welcome" + name
#     return res
# print(galla(" hai"))

# contacts = [('John', 'john.deer@gmail.com'),
#      ('Alex', 'alex.barner@yahoo.com'),
#      ('Brad', 'brad.cooper@hotmail.com'),
#      ('Cindy', 'cindy.barner@hotmail.com'),
#      ('Matt', 'matt.damon@gmail.com'),
#      ('George', 'george.cloony@yahoo.com'),
#      ('Mec', 'mc.barner@hotmail.com')
# ]
# contacts2 = []
# for name, email in contacts:
#     if 'barner' in email:
#         contacts2.append((name, email))
# contacts2.sort()
# print(contacts2)

