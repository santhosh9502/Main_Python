# # 1
# # import math
# num = int(input("enter the num: "))
# # print(math.sqrt(num))
# n = num * 2
# if :
#     print("sqr")
# else:
#     print("not-sqr")

def prime(num):
    # if num < 2:
    #     return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

number = int(input("enter the num: "))
if prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")

# number = int(input("enter the num: "))
# for i in range(2, number):
#     if prime(i):
#         print(i)
