# decorators take input function as argument
"""
    Why decorators are basically used: 
    1. To reduce complextiy of the fx
    2. Timing precision
"""

import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func} took {(end-start)*1000}ms time to complete")
        return result
    return wrapper
        

@time_it
def calc_square(num):
    """Calculate the square of a number."""
    return num ** 2

@time_it
def calc_cube(num):
    """Calculate the cube of a number."""
    return num ** 3

#Lets test these functions
calc_square(29)
calc_cube(8)