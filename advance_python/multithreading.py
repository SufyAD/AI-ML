"""
    Threading is akin to a mom multitasking, seamlessly managing various home chores such as cooking, taking phone calls, and caring for her baby simultaneously. 
    Each task can be viewed as a "separate thread", allowing her to efficiently allocate her time and attention to multiple responsibilities, 
    demonstrating the power of concurrency in everyday life.
"""

import time
import threading        #standard library to do threading in python

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func} took {(end-start)*1000}ms time to complete")
        return result
    return wrapper

@time_it
def calc_square(num: list[int]):
    """Calculate the square of a number."""
    for n in num:
        result = n ** 2 
        time.sleep(0.2)
        print(f"Square of {n} = {result}")

@time_it
def calc_cube(num: list[int]):
    """Calculate the cube of a number."""
    for n in num:
        result = n ** 3
        time.sleep(0.2) # cpu is idle here
        print(f"Cube of {n} = {result}")

t1 = time.time()

square_thread = threading.Thread(target=calc_square, args=([1, 2, 3, 4, 5],))
cube_thread = threading.Thread(target=calc_cube, args=([1, 2, 3, 4, 5],))

square_thread.start()
cube_thread.start()

square_thread.join()
cube_thread.join()

# The following calls to calc_square and calc_cube are unnecessary since the calculations have already been done in the threads.
# Therefore, we can remove these lines:
# squares = calc_square([1,2,3,4,5])
# cubes = calc_cube([1,2,3,4,5])

t2 = time.time()
print(f"Total time to complete {(t2-t1)*1000} ms") 


