""" 3. Write a program to read n mobile numbers from the user. And then write a decorator to 
print them in the standard format shown below:
 +91 xxxxxxxxxx

Sample Input
n = 4
9515669077
8978931695
9640440600
9195969878

Sample Output
+91 9515669077
+91 8978931695
+91 9640440600
+91 9195969878
 """

n = int(input("enter the no.of.times: "))
phone_numbers = []
for main in range(n):
    phone_numbers.append(input("enter the ph_numbers: "))
    
def deco(phnum):
    def fun(number):
        for phone in number:
            phnum("+91 " + phone)
            # return number
    return fun

@deco
def new_num(number):
    print(number)

new_num(phone_numbers)