""" 1. Write a program to reverse an integer in Python """
# n = int(input("please give a number : "))
# print("before reverse your numeber is : %d" %n)
# reverse = 0
# while n!=0:
#     reverse = reverse*10 + n%10
#     n = (n//10)
# print("After reverse : %d" %reverse) 
# 
# n = input("enter the number: ")
# print("before reversing number",n)
# res = reversed(n)
# res = ''.join(res)
# print("after reversing number", res)
# 
# n = input("please give the number: ")
# res = n[::-1]
# print(res)

""" 2.Write a program in Python to check given number is prime or not. """
def is_prime(num):
    if num < 1:
        return False
    rt = int(num ** .5)
    for i in range(2,rt+1):
        if num % i == 0:
            return False
    return True

numb = int(input("enter the num: "))
if is_prime(numb):
    print("number is prime", numb)
else:
    print("number is not a prime", numb)

""" 3. """