# d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
# for x in d:
#     print (x,d[x]) 
# o/p:
#     #Orange 40
#     # Mango 30
#     # Banana 15
#     # Peach 20
# # KEYS()
# d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
# print(d.keys()) # o/p: dict_keys(['Orange', 'Mango', 'Banana', 'Peach'])
# # VALUES()
# d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
# print(d.values()) # o/p: dict_values([40, 30, 15, 20])
# # ITEMS()
# d = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
# print(d.items()) # o/p: dict_items([('Orange', 40), ('Mango', 30), ('Banana', 15), ('Peach', 20)]) "in list of tuples"

# # 
# f = {'Orange': 40, 'Mango': 30, 'Banana': 15, 'Peach': 20}
# for fruit, cost in f.items():
#     print(fruit, cost)
    
# 
# d = {'Orange': 40, 'Mango': 30, 'Banana': 15}
# # d['peach'] = 50
# print(d)

# qm = {}
# qm['emp_id'] = 1071
# qm['Name'] = 'Saravana'
# qm['Age'] = 22
# qm['mail_id'] = 'saravana20@gmail.com'
# qm_2 = {}
# qm_2['emp_id'] = 1008
# qm_2['Name'] = 'Raja'
# qm_2['Age'] = 24
# qm_2['mail_id'] = 'raja24@gmail.com'
# qm_3 = {}
# qm_3['emp_id'] = 1118
# qm_3['Name'] = 'Kumar'
# qm_3['Age'] = 54
# qm_3['mail_id'] = 'kumar54@gmail.com'

# res = []

# for i in qm,qm_2,qm_3:
#     res.append(i)
# print(res)

# my_dict = {'name': 'raja', 'age': 24}
# new_dict = my_dict.values()
# print(new_dict)

""" COUNTING PROBLEMS """
words = ["Apple", "Orange", "Apple", "Banana", "Peach",  
          "Banana", "Apple", "Peach", "Apple", "Banana"]

c = {}
for sent in words:
    if sent not in c:
        c[sent] = 1
    else:
        c[sent] += 1
print(c)
print("Max is",max(c.items(), key=lambda x: x[1]))
print("Min is", min(c.items(), key= lambda x: x[1]))
print(dict(sorted(c.items(),key= lambda x:x[1],reverse=True)))

""" GROUPING """
cdr = [
('9816724398', '9810485623'),
('9838217965', '9895170862'),
('9816724398', '9858932761'),
('9838217965', '9816724398'),
('9858932761', '9810485623'),
('9858932761', '9895170862'),
('9810485623', '9838217965'),
('9810485623', '9858932761'),
('9838217965', '9858932761'),
('9858932761', '9816724398'),
('9816724398', '9838217965'),
('9895170862', '9810485623'),
('9810485623', '9816724398')
]

call = {}
for caller,calle in cdr:

    if caller not in call:
        call[caller] = [calle]
    else:
        call[caller].append(calle)
print(call)