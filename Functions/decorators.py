        # DECORATORS
# A decorator is a function that takes another function 
# and extends the behavior of the latter function without explicitly modifying it.

# def fun(ref):
#     def process():
#         data = ref()
#         return data.upper()
#     return process

# def myfunc():
#     return "Welcome home"

# res = fun(myfunc)
# print(res()) #changed the answer, but the original is not changed that answer is below.

# print(myfunc()) # this is the original.

""" ANOTHER DECORATOR METHOD """
def out_fun():
    msg1 = "Welcome to"
    def inn_fun():
        msg2 = " Hyderabad "
        out = msg1+msg2
        return out
    return inn_fun

obj = out_fun()
print(obj())

""" deco"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        ret = func(*args, **kwargs)
        end = time.perf_counter()
        print("Time taken: ", end - start)
        return ret
    return wrapper

@timer
def process(n):
    for i in range(n):
        i = i * i
        
process(10000000)
