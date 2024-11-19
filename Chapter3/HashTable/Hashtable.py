class HashTable:
    def __init__(self, size):
        self.size = size
        self.table ={}
        for i in range (size):
            self.table[i]= []
    def hash(self, key):
        return key % self.size
        
            
            