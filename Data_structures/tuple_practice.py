                # tuple pratice questions
# 1
# t = (2,3,4,1,2,3)
# t2 = list(t)
# t2.insert(4,7)
# print(tuple(t2))

# 2
# tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# even = 0
# odd = 0
# for i in tuple1:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even)
# print(odd)

# 3
# t = (78,34,7,'saravana')
# t2 = list(t)
# t2[3],t2[2] = 'raja',2
# print(tuple(t2)) 

# 4
# t1 = (3, 4, 5, 6)
# t2 = (5, 7, 4, 10)
# t3 = set(t1) - set(t2)
# t4 = set(t2) - set(t1)
# res = sorted(list(t3) + list(t4))
# print(tuple(res))

# 5
# t1 = (10,4,5)
# t2 = (2,5,18)
# t3 = tuple(map(lambda x,y: x + y,t1,t2))
# print(t3)

# 6
# t = ('saravana',34,7,23,'saravana',88,43,34,12,'Raja')
# t1 = set(t)
# print(tuple(t1))

# 7
# Write a program to sort the following employ data 
# (list of tuples) as per their salaries (each tuple represents employ ID, name, age and salary)?
data = [(1234, 'Abishek' , 32, 35000),
        (4532, 'Barathi', 27, 29000),
        (3455, 'Charan', 31, 37000),
        (9863, 'Devi', 42, 52000),
        (4852, 'Eswar', 37, 56000),
        (6481, 'Fathima', 40, 65000),
        (2793, 'Ganesh', 28, 45000)
]
sorted_salaries = sorted(data,key=lambda x:x[3],reverse=True)
for i in sorted_salaries:
    print(i)
print(sorted_salaries)

# 8
students = [("John", ["Computers", "Physics", "Maths"]),
            ("Wasim", ["Maths", "Computers", "Statistics"]),
            ("Naresh", ["Computers", "Accounting", "Economics"]),
            ("SaiTeja", ["English", "Accounting", "Economics", "Law"]),
            ("Sravani", ["Sociology", "Economics", "Law", "Stats", "Music"])
]
comp = 0
for i in students:
    if 'Computers' in i[1]:
        comp += 1
print(comp)
