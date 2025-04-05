"""
Sharing data with Array and Value
"""
import time
import multiprocessing

# child processs
def calc_square(numbers, value, q):
    """Calculate the square of a number."""
    value.value = 56524232
    for num in numbers:
        q.put(num**2) # queue data structure

# parent process
if __name__ == "__main__":
    numbers = [2,3,4]
    # result = multiprocessing.Array('i', len(numbers)) # using Array method
    v = multiprocessing.Value('d', 0.0)
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers, v, q))
    
    
    p.start()
    p.join()

    # child => child sharing data
    while q.empty() is False:
        print(q.get())
    print(v.value)