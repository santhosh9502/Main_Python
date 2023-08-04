"""Write a program to display the multiplication table for a given number."""
def mul_tab(mul_num):
    for i in range(1,50):
        product = i * mul_num
        print(f"{i} * {mul_num} = {product}")

res = int(input("enter the number: "))
mul_tab(res)