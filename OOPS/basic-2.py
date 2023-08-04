# import calendar
# year = 2023
# m = 5
# result = calendar.month(year,m)
# print(result)

"""INHERITANCE"""
# base class
# class animal:
#     def eat(self):
#         print("I can eat")
#     def sleep(self):
#         print("I can sleep")
# # derived class
# class dog(animal):
#     def friend(self):
#         print("I'm Human's best friend")
    
# dog1 = dog()
# dog1.eat()
# dog1.sleep()
# dog1.friend()
# 
"""ENCAPSULATION"""
# class computer:
#     def __init__(self):
#         self.__maxprice = 800

""" CREATING CLASS """
# class employees:
    
#     def __init__(self,id,name):
#         self.id = id
#         self.name = name

#     def __str__(self):
#         return f"{self.id},{self.name}"
    
# e1 = employees(1001,"Raja")
# e2 = employees(1003,"Saravana")
# print(e1.id)
# print(e2.name)
# print(type(e1))

""" DEFINING CLASS """
# class computer:
    
#     def config(self):
#         return "i7","HP"

# comp1 = computer()

# print(comp1.config())

""" data type using class """
# class bike():

#     def __init__(self,id,name,price):
#         self.id = id
#         self.name = name
#         self.price = price

# KTM = bike(1001,"Ktm",120000)
# Yamaha = bike(1004,"FZ V3",120000)

# print(Yamaha.__dict__)
# print(KTM.__dict__)

""" CREATING A CLASS """
# class MyClass:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello, {self.name}!")
    
#     def set_name(self, new_name):
#         self.name = new_name

# obj = MyClass('Raja')
# obj.greet()

# obj.set_name('Siva')
# obj.greet()

"""  """