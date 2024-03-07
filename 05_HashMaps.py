class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
    
class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        node = Node(key, value)
        
        if self.table[index] is None:
            self.table[index] = node
        
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = node
                
    def retrieve(self, key):
        index = self._hash(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        previous = None
        
        while current.key != key and current:
            previous = current
            current = current.next
        
        if current:
            if previous:
                previous.next = current.next
            else:
                self.table[index] = current.next
            
            current.next = None
            current = None
        
    def display_map(self):
        
        for values in self.table:
            current = values
            while current:
                print(f"Key:{current.key}::Value:{current.value}", end="\n")
                current = current.next
        print()
                

if __name__ == "__main__":
    
    H = HashMap(5)
    H.insert("Kishore", 12)
    H.insert("Abinav",13)
    H.insert("Rahul", 15)
    print(H.retrieve("Kishore"))
    H.display_map()
    H.remove("Abinav")
    H.display_map()