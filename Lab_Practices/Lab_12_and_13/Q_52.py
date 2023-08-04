"""Write a program to display the numbers sequentially from 1 to 99 with 5
numbers on each column"""
def dis_col():
    for i in range(1,100):
        print(i)
        if i % 5 == 0:
            print()
dis_col()
