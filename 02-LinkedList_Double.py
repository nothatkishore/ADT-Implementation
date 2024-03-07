class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    
    def append(self, data) -> None:
        node = Node(data)
        if self.head ==  None:
            self.head = node
            return
        
        iterator = self.head
        while iterator.next != None:
            iterator = iterator.next
            
        iterator.next = node
        node.previous = iterator

    def prepend(self, data) -> Node:
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node
    
    
    def delete_node(self, key):
        if self.head is None:
            print("List is empty")
            return

        current_node = self.head

        if current_node.data == key:
            self.head = current_node.next
            if self.head:
                self.head.previous = None
            current_node.next = None
            current_node = None
            return

        while current_node and current_node.data != key:
            current_node = current_node.next

        if current_node is None:
            print("Value not found")
            return

        previous_node = current_node.previous
        next_node = current_node.next
        if previous_node:
            previous_node.next = next_node
        if next_node:
            next_node.previous = previous_node

        current_node.next = None
        current_node.previous = None
        current_node = None
    
    def print_nodes(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=' ')
            iterator = iterator.next


if __name__ == "__main__":
    ll = LinkedList()

    for i in range(0, 50, 5):
        ll.append(i)
    ll.delete_node(0)
    ll.delete_node(25)
    ll.delete_node(45)
    ll.print_nodes()
        