class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class HashSet:
    
    def __init__(self, size) -> None:
        self.size = size
        self.table = [None] * self.size
    
    def _hash(self, data) -> None:
        return hash(data) % self.size
    
    def insert(self, data) -> None:
        index = self._hash(data)
        node = Node(data)
        
        if self.table[index] is None:
            self.table[index] = node
        
        else:
            current = self.table[index]
            while current:
                if current.data == data:
                    return
                current = current.next
                
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = node
    
    def remove(self, data) -> None:
        index = self._hash(data)
        current = self.table[index]
        
        if current.data == data:
            pass
        
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        
        if current:
            if previous:
                previous.next = current.next
            else:
                self.table[index] = current.next
                
            current.next = None
            current = None
    
    def contains(self, data):
        index = self._hash(data)
        current = self.table[index]
        
        while current:
            if current.data == data:
                return True
            current = current.next
        
        return False
    
    def display_hashsets(self):
        for values in self.table:
            current = values
            while current:
                print(current.data, end=" ")
                current = current.next
        print()


if __name__ == "__main__":
    H = HashSet(10)
    H.insert(10)
    H.insert(20)
    H.insert(30)
    H.insert(30)
    H.insert(40)
    H.display_hashsets()
    H.remove(20)
    H.display_hashsets()
    