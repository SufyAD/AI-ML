class HashMap():
    def __init__(self):
        self.MAX = 100
        self.arr = [None] * self.MAX # creating an empty list
        
    # Now it's time to mimic some actual dictionary methods
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char) # this will return the HEX code of char
        return h % 100
    
    def add_item(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value # self.arr[str->int index] = value
                
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is not None:
            return self.arr[h]
        return None
        
    def get_value(self, key):
        h = self.get_hash(key)
        return self.arr[h] 
 
    def pop(self, key):
        h = self.get_hash(key)
        if self.arr[h] is not None: 
            self.arr[h] = None
        return None
    
    # TODOs
    # 3. def update():
    # 4. setdefault(key, default=None) (Complex)
    # 5. fromkeys(seq, value=None) (Complex)
    # 6. items() (Complex)
    
    
if __name__ == "__main__":
    my_dict = HashMap()
    my_dict.add_item("apple", "An apple a day keeps the doctor away!")
    print(my_dict['apple'])