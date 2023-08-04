""" 2. You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
import time
# caching technique
cache = {2:2,1:1}
# Recursive function
def ways(n): 
    if n not in cache:
        cache[n] =  ways(n-1) + ways(n-2)
    return cache[n]
print(f'No of Ways: {ways(12)}')