"""
Creating a simple banking application that supports two processes 
1. check balance
2. withdraw
Both these processes run in parallel, thus, they'll create unnecessary impact on each other while execution, we can see in the code below
"""

import multiprocessing

class Bank:
    def __init__(self):
        self.balance = multiprocessing.Value('i', 1000)  # shared balance (initial = 1000)
        self.lock = multiprocessing.Lock()

    def withdraw(self, amount):
        print(f"Current Balance: {self.balance.value}")
        # note here you can use context_managers that will do work for lock.acquire or lock.release itself efficiently
        with self.lock:
            if self.balance.value >= (amount + 2):
                self.balance.value -= (amount + 2)
                print(f"Withdrawn: {amount}, Fee: 2, New Balance: {self.balance.value}")
            else:
                print("Insufficient balance")

    def deposit(self, amount):
        print(f"Current Balance: {self.balance.value}")
        with self.lock:
            self.balance.value += (amount + 1)   # +1 as tip
            print(f"Deposited: {amount}, Tip: 1, New Balance: {self.balance.value}")
               
               
if __name__ == "__main__":
    my_bank = Bank()

    d = multiprocessing.Process(target=my_bank.deposit, args=(69,))
    w = multiprocessing.Process(target=my_bank.withdraw, args=(90,))

    d.start()
    w.start()

    d.join()
    w.join()

