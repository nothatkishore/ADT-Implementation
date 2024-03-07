class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class Queue:
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.size = size
        self.current_size = 0
    
    def enqueue(self, data) -> None:
        if self.is_full():
            print("Overflow")
            return
        
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.current_size += 1
    
    def dequeue(self) -> None:
        if self.is_empty():
            print("Underflow")
            return
        
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
        self.current_size -= 1
    
    def front(self) -> int:
        if self.is_empty():
            print("Queue is empty")
            return -1
        return self.head.data

    def rear(self) -> int:
        if self.is_empty():
            print("Queue is empty")
            return -1
        return self.tail.data
    
    def is_full(self) -> bool:
        return self.current_size == self.size
    
    def is_empty(self) -> bool:
        return self.current_size == 0

    def print_queue(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


if __name__ == "__main__":
    Q = Queue(5)
    for i in range(5):
        Q.enqueue(i)
    Q.print_queue()
    Q.dequeue()
    Q.dequeue()
    Q.dequeue()
    Q.dequeue()
    Q.dequeue()
    Q.print_queue()
