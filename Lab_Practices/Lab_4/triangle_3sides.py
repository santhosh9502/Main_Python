a = int(input("enter the a: "))
b = int(input("enter the b: "))
c = int(input("enter the c: "))
s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)

print(f"the area of the triangle is {area}")
print(f"the area of the semi-perimeter is {s}")