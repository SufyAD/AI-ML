"""
    Multiprocessing vs Multithreading:
    - Multiprocessing involves multiple processes, each with its own Python interpreter and memory space, allowing for true parallelism.
    - Multithreading, on the other hand, runs multiple threads within a single process, sharing the same memory space, which can lead to issues with the Global Interpreter Lock (GIL) in Python.

    Inter-Process Communication (IPC):
    - Since processes do not share memory, they require different communication protocols to share data. Common IPC methods include:
        1. Pipes: Unidirectional communication channels.
        2. Queues: Thread- and process-safe FIFO data structures.
        3. Shared Memory: Allows multiple processes to access the same memory space, but requires synchronization mechanisms to avoid conflicts.

    Key Considerations:
    - Use multiprocessing for CPU-bound tasks to leverage multiple cores.
    - Use multithreading for I/O-bound tasks to improve responsiveness.
"""


import time
import multiprocessing

def calc_square(num: list[int]):
    """Calculate the square of a number."""
    for n in num:
        result = n ** 2 
        print(f"Square of {n} = {result}")

def calc_cube(num: list[int]):
    """Calculate the cube of a number."""
    for n in num:
        result = n ** 3
        print(f"Cube of {n} = {result}")
        
   
# This prevents the subprocesses from recursively re-importing the script, which leads to that RuntimeError.
     
if __name__ == "__main__":
    t1 = time.time()

    p1 = multiprocessing.Process(target=calc_square, args=([1, 2, 3, 4, 5],))
    p2 = multiprocessing.Process(target=calc_cube, args=([1, 2, 3, 4, 5],))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    t2 = time.time()
    print(f"Total time to complete {(t2-t1)*1000} ms")