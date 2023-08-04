sub1 = int(input("enter the maths score: "))
sub2 = int(input("enter the science score: "))
sub3 = int(input("enter the tamil score: "))

total = sub1 + sub2 + sub3
avg = (sub1 + sub2 + sub3)/3

if avg >= 90:
    class_name = "A+"
elif avg >= 80:
    class_name = "A"
elif avg >= 70:
    class_name = "B"
elif avg >= 60:
    class_name = "C"
elif avg >= 50:
    class_name = "D"
elif avg >= 40:
    class_name = "E"
else:
    class_name = "Fail / Need an Improvement"

print(f"the sum of three subjects are {total}")
print(f"the average of three subjects are {avg}")
print(f"the class is {class_name}")
