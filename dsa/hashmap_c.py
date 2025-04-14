# Creating hashmaps with collision avoidance using two common methods in pytho
# 1. Using a chaining
# 2. Using linear probing

# using chaining method
class HashMap():
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]  # Initialize as list of empty lists
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char) # this will return the HEX code of char
        return h % self.MAX
    
    # collision avoidance using chaining
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            # (element[0], element[1]) = (key, value)
            if element[0] == key:
                self.arr[h][idx] = (key, value)  # Update existing key
        self.arr[h].append((key, value))
                
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1] # Return value associated with key
 
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
               del self.arr[h][index] # delete the key-value pair (tuple)
    
    
    
def main():
    my_dict = HashMap()
    hash1 = my_dict.get_hash("march 6")
    hash2 = my_dict.get_hash("march 17")
    my_dict["march 6"] = 69
    my_dict["march 17"] = 420 # same index for testing purpose
    print(my_dict.arr)
    
    del my_dict["march 17"]
    
    print(my_dict.arr)
    
    
    
    
    
    
    
    
    
if __name__  == "__main__":
    main()