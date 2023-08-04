"""Write a program to display the numbers sequentially from 1 to 99 with 5 numbers on each line"""
def dis_num():
    for i in range(1,100):
        print(i, end=" ")
        if i % 5 == 0:
            print()
dis_num()