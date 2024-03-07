class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        
        iterator = self.head
        while iterator.next != None:
            iterator = iterator.next
        iterator.next = node
    
    def prepend(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node
    
    def delete_node(self, key):
        if self.head == None:
            print("List is empty!")
            return
        
        iterator = self.head
        
        if iterator.data == key:
            self.head = iterator.next
            iterator = None
            return
        
        previous = None
        while iterator.data != key and iterator:
            previous = iterator
            iterator = iterator.next
        
        if iterator is None:
            print("Value not availabe in the list")
            return
        
        previous.next = iterator.next
        iterator = None
    
    def print_list(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end="-->")
            iterator = iterator.next

if __name__ == "__main__":
    ll = Linkedlist()
    for i in range(0, 100, 5):
        ll.append(i)
    ll.delete_node(0)
    ll.delete_node(20)
    ll.delete_node(95)
    ll.print_list()