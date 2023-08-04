# List Examples
# l1 = [30, 32, 31, 35.5, 30, 36, 34] 
# print(l1[4],l1[0]) # 30 using index
# print(l1[-1],l1[-2]) # 34,36 using -ve index
# print(l1[::-1]) # using index this will "REVERSE THE LIST"
# 2
# fruits = ["Apple", "Orange", "Banana", "Peach", "Grape"]
# print (fruits[-1], fruits[-2])
# 3
# l2 = [2, 4, 3, 1, 7, 9, 8, 0, 6, 5]
# print(l2[:5]) # returns a list with first five elements
# print(l2[7:]) # returns a list with first seven elements
# print(l2[-3:]) # returns last three elements
# Membership Operator "IN"
# s = [4,5,3,2,8,9]
# print(5 in s) # gives TRUE
# print(1 in s) # gives FALSE
# print(2 not in s) # gives opposie values ex: if real answer is "TRUE",then this "NOT IN" operator works as "FALSE"
# print(1 not in s) # gives TRUE

# Gives the length [len()] of the values
# a = "Quality Matrix"
# print(len(a))
#2
# x = "\n"
# print(len(x))
#3
# x = 'it\'s ok'
# print(len(x))

# COUNT
# s = [2,3,4,5,7,8,9,5,3,2]
# print(s.count(2)) # gives the no of given values inside the COUNT()

# Modify value at specific index
# i = 3
# l = [6, 4, 5, 8, 2, 1]
# l[i] = 99
# print(l)

# APPEND()
# s = [1,2,3,4,5,8,6,7,9]
# s.append(55) # inside the bracket anything can given like "int,str,lis,tuple",etc..
# print(s) # "add the value in the end of the list"
# s = [1,2,3,6]
# r = [55,88,77]
# s.append(r)
# print(s) # {ans: [1, 2, 3, [55, 88, 77]]} => In this method it "Add the Total list into the another list" 
# print(s[4]) # By using the indexing it shows the value of given number
# print(type(s[4])) # {<class 'list'>} => type of value
# print(s[3][1])

# EXTEND
# s = [9,8,7,4]
# r = [87,56,21]
# s.extend(r)
# print(s) # [9,8,7,4,87,56,21] => In this it only add the values into the new list
# print(s[4]) # 87
# print(type(s[4])) # its <class 'int'>
# print(s[3][2])

# INSERT()
# l = [1,2,3,4,5,7]
# l.insert(4,8)
# print(l)

# POP()
# l = [1,2,3,4,5,9,7,8]
# res = l.pop()
# print(res)
# print(l)
# result = l.pop(5),l.pop(3)
# print(result)
# print(l)

# REMOVE()
# l = ["hai",'hello',1,2,3,4,5,7,8]
# l.remove('hai')
# print(l)

# finding INDEX()
# l = [1,2,3,4,5,7,8]
# print(l.index(4)) # 3 because its giving the index value of "4"

# concadinate lists using "+", "*" 
# l1 = [5,6,4,7,8,9]
# l2 = [8,7,4,1,2,3]
# print(l1 + l2) # same answer
# print([* l1,*l2]) # same answer
# l3 = ["saravana","raja","kavi","moorthy","gowtham"]
# l4 = ["gowtham","chinnu","baakiyam","sandy"]
# print([*l3,*l4])

# MAX()
# l = [1,2,3,4,5,7,8,77]
# print(max(l)) # gives the "highest" values in the list
# MIN()
# l = [1,2,3,4,5,7,8,0.23]
# print(min(l)) # gives "lowest" values in the list
# SUM()
# l = [1,2,3,4,5,7,8]
# print(sum(l)) # gives the "total" number of list

# REVERSE()
# l = [1,2,3,4.89,5,7,8,2.45]
# l.reverse() # using normal reverse function
# print(l)
# l1 = [1,2,3,4,5,7,8]
# print(l1[::-1]) # using slicing

# WHILE LOOP
# i = 0
# l = [2,3,4,5,7,8]
# while i < len(l):
#     print (l[i])
#     i += 1

# FOR LOOP
# l = [2.89,3,4,5.23,1.45,8]
# for i in l:
#     print(i)

# ENUMERATE()
# l = ["Apple", "Orange", "Grape", "Banana", "Peach"]
# for l in enumerate(l,start=1001):
#     print(l)

# SORT() & SORTED()
# l = [23,57,2,3,923,4,5,7,8]
# l.sort() # gives result of ascending order to descending order
# print(l)
# l2 = [23,57,2,3,923,4,5,7,8]
# print(sorted(l2))
# print(l2)
# s = 'New York'
# print(sorted(s)) # sort elements in ascending order 
# print(sorted(s, reverse=True)) # sort elements in descending order 
# print(s)

# num_calls = int(input("Enter the number of calls: "))
# if num_calls <= 100:
#     bill_amount = 200
# elif num_calls <= 150:
#     bill_amount = 200 + (num_calls - 100) * 0.6
# elif num_calls <= 200:
#     bill_amount = 200 + 50 * 0.6 + (num_calls - 150) * 0.5
# else:
#     bill_amount = 200 + 50 * 0.6 + 50 * 0.5 + (num_calls - 200) * 0.4
# print("Your monthly telephone bill is Rs. {:.2f}".format(bill_amount))