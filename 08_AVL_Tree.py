class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def rotateLeft(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rotateRight(root)

        if balance < -1 and key > root.right.key:
            return self.rotateLeft(root)

        if balance > 1 and key > root.left.key:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)

        elif key > root.key:
            root.right = self._delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rotateRight(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rotateLeft(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root


    def preOrder(self, root):
        if root is not None:
            print("{0} ".format(root.key), end="")
            self.preOrder(root.left)
            self.preOrder(root.right)


# Usage
myTree = AVLTree()
keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for key in keys:
    myTree.insert(key)

print("Preorder traversal of the", "constructed AVL tree is")
myTree.preOrder(myTree.root)

myTree.delete(10)

print("\nPreorder traversal after", "deletion of 10:")
myTree.preOrder(myTree.root)
