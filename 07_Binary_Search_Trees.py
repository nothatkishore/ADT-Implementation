class Node:
    def __init__(self, data) -> None:
        self.right = None
        self.data = data
        self.left = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data) -> None:
        self.root = self._insertion_helper(self.root, data)
    
    def _insertion_helper(self, root, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = self._insertion_helper(root.left, data)
        
        elif data > root.data:
            root.right = self._insertion_helper(root.right, data)
        
        return root

    def search(self, data) -> None:
        return self._search_helper(self.root, data)
        
    def _search_helper(self, root, data):
        if root is None or root.data == data:
            return root
        
        if data < root.data :
            return self._search_helper(root.left, data)
        
        elif data > root.data :
            return self._search_helper(root.right, data)

        return root
    
    def traversal(self):
        result = []
        self._traversal_helper(self.root, result)
        return result
    
    def _traversal_helper(self, root, result):
        if root:
            self._traversal_helper(root.left, result)
            result.append(root.data)
            self._traversal_helper(root.right, result)


if __name__ == "__main__":
    B = BinarySearchTree()

    for i in range(0, 10):
        B.insert(i * 10)
    
    print(B.search(10))
    print(B.traversal())
