"""Write a program to find whether the given numbers existing in an array or not"""
def list(l):
    lists = int(input("enter the num: "))
    if lists in l:
        print(f"given number {lists} is existing in this array")
    else:
        print("Error, Given number is not exist in this array")
    return lists

l = [1,2,3,5,4,7,8,90]
print(list(l))
