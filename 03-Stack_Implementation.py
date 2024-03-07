'''
Stack Operations:

    1. Push()
    2. Pop()
    3. Peak()
    4. isEmpty()
    5. size()

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, element) -> None:
        node = Node(element)
        
        if self.head == None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node
    
    def pop(self):
        curr_node = self.head
        self.head = self.head.next
        curr_node.next = None
        curr_node = None
    
    def peak(self):
        print(self.head.data)
    
    def isEmpty(self) -> bool:
        if self.head:
            return False
        else:
            return True
    
    def size(self) -> int:
        iterator = self.head
        count = 0
        while iterator:
            count += 1
            iterator = iterator.next
        return count

    def print_stack(self):
        iterator = self.head
        while iterator:
            print(iterator.data, end=" ")
            iterator = iterator.next
        print()


if __name__ == "__main__":
    S = Stack()
    for i in range(0, 10):
        S.push(i)
    S.print_stack()
    S.pop()
    print(S.size())
    S.print_stack()