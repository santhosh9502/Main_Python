a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
	print("Equilateral triangle") # 3 sides are equal
elif a==b or b==c or c==a:
	print("isosceles triangle") # only 2 sides are equal
else:
	print("Scalene triangle") # all sides are unequal