    # NEW PROJECT-2

# join() string
l = ['A', 'p', 'p', 'l', 'e']
emp_data = ['1234', 'John', '23400.0', 'Chicago']
s1 = ''.join(l)
s2 = ','.join(emp_data)
print(s1)
print(s2)

# find()
x= "hello hai welcome home"
print(x.find("hello"))
print(x.find('home'))

# slicing
a = "saravanamurthi"
print(a)
print(a[0:5])
print(a[1:7:2])
print(a[1:7:4])
print(a[-2:-8:-1])
print(a[-2:-8:-2])
print(a[-5:-8:-2])
print(a[::-1])
print(a[1::])
print(a[::1])
# print(a[-1:-4:-3])
# print(a[-7:-10:-2])
# print(a[-2:-13:-1])
# print(a[-7:-14:-1])

# ASCII VALUE
# 1
result = 0
name = input('enter the value: ')
for i in name:
    result+=ord(i)
print(result)
# 2
print(ord("a"),ord("z"))
print(ord("A"),ord("Z"))
# 3
name = input('enter the string: ').title()
for i in name:  
    result = ord(i)  
    print (i, result)

# CONCADINATION
s = "saravana"
y = 123
print(f"{s} {y}")

# finding 1st 2 WORDS and Last 2 Words
string = input("Enter a value: ")
s = string[0:2]
r = string[-2:]
res = s + r
print(res)

# JOING A VALUES
a = input("enter the value: ")
print(f"{a}ing")

# Isnumeric
n = "1234"
if n.isnumeric() == True:
    print("number")
else:
    print("not number")

# isnumeric-2
s = "hai123"
s1 = s.isnumeric()
print(s1)

# SurName
name = input("enter the value: ").title()
name = name.split()
print(f"{name[0][0]}.{name[1][0]}.{name[2]}")
