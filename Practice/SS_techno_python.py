"""SS TECHO-Practice questions"""
# 1.Write a Python program to sum all the items in a list.
def sum_itm(lst):
    return sum(lst)

sum_lst = [1,3,2,4,8,2]
res = sum_itm(sum_lst)
print (f"sum is {res}")
print("--------------------")
# 2. Write a Python program to multiply all the items in a list
def mul_lst(lst):
    result = 1
    for i in lst:
        result *= i
    return result

mul_itm = [3,7,4,9,8,2]
res = mul_lst(mul_itm)
print(f"product is {res}")
print("--------------------")
# 3. Write a Python program to get the largest number from a list.
def lst_num(lst):
    n = sorted(lst,reverse=True)
    result = n[0]
    return result

lists = [121,129,34,78,1,0,43,99,100]
res = lst_num(lists)
print(f"Largest num is {res}")
print("--------------------")
# 4. Write a Python program to get the smallest number from a list.
def sml_num(lst):
    n = sorted(lst)
    result = n[0]
    return result

lists = [121,129,34,78,43,4,1,99,100]
res = sml_num(lists)
print(f"Smallest num is {res}")
print("--------------------")
# 5. Write a Python program to remove duplicates from a list.
def rme_dup(dup):
    clt = set(dup)
    result = list(clt)
    return result

lst = [1,2,3,2,5,7,4,55,7,0,1]
res = rme_dup(lst)
print(f"removed dulpictes are {res}")
print("--------------------")
# 6. Write a Python program to check a list is empty or not
def chk_lst(lst):
    if len(lst) <= 0:
        return print("empty")
    return print("not empty")

l = []
chk_lst(l)
print("--------------------")
# 7. Write a Python program to find the list of words that are longer than n from a given list of words
def find_longer_words(words, n):
    return [word for word in words if len(word) > n]

word_list = ['apple', 'banana', 'carrot', 'dragonfruit', 'elephant']
n = 5
longer_words = find_longer_words(word_list, n)
print(longer_words)
print("--------------------")
# 8. Write a Python function that takes two lists and returns True if they have at least one common member
def cmn_mbr(lst,lst2):
    return bool(set(lst) & set(lst2))

l = [1,2,3,4,5]
# l2 = [2,3,4,5,7,2]
l2 = [6,7,8,9,10]
res = cmn_mbr(l,l2)
print(res)
print("--------------------")
"""9. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']"""
def rme_ele(lst):
    lists = lst[1:4] 
    return lists

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
res = rme_ele(list)
print(res)
print("--------------------")
# 10. Write a Python program to print the numbers of a specified list after removing even numbers from it.
def even_num(numbers):
    odd_num = []
    for i in numbers:
        if i % 2 != 0:
            odd_num.append(i)
    return odd_num

numbers = [1,12,32,34,77,99,79,11]
res = even_num(numbers)
print(res)
print("--------------------")
"""11. Write a Python program to generate and print a list of first and last 5 elements 
where the values are square of numbers between 1 and 30 (both included)."""
def sqr_elem():
    squares = []
    for i in range(1,31):
        num = i**2
        squares.append(num)
    first_five = squares[:5]
    last_five = squares[-5:]
    return first_five,last_five

res = sqr_elem()
print(res)
print("--------------------")
"""12. Write a Python program to generate and print a list except for the first 5 elements, where
the values are square of numbers between 1 and 30 (both included)."""
def elem_sqr():
    squr = []
    for i in range(1,31):
        num = i**2
        squr.append(num)
    exc_first_five = squr[5:]
    return exc_first_five

res = elem_sqr()
print(res)
print("--------------------")
# 13. Write a Python program to get the difference between the two lists.
# def dif_two_lst(elem1,elem2):
#     num = list(set(elem1)-set(elem2))
#     return num

# l1 = [1,2,3,4,5,5,4,3,2,1]
# l2 = [1,2,3,4,5,5,4,3,2,1]
# res = dif_two_lst(l1,l2)
# print(res)
print("--------------------")
# 14. Write a Python program access the index of a list.
def ind_lst(lst,itm):
    index = lst.index(itm)
    return index

my_list = [11,77,34,23,90]
fnd = 23
res = ind_lst(my_list,fnd)
print(res)
print("-------------------")
# 15.Write a Python program to find the index of an item in a specified list.
# 16.Write a Python program to append a list to the second list.
def app(elem1,elem2):
    elem1.extend(elem2)
    return elem1

l1 = [9,8,7,5]
l2 = [1,2,3,4]
res = app(l1,l2)
print(res)
print("-------------------")
# 17.Write a Python program to select an item randomly from a list.
import random
def ran(elem):
    if len(elem) == 0:
        return None
    return random.choice(elem)

l1 = [1,2,3,4]
res = ran(l1)
print(res)
# 18.