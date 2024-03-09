class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to indicate end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True


# Example usage
trie = Trie()
words = ["apple", "banana", "orange", "app", "applesauce"]
for word in words:
    trie.insert(word)

print(trie.search("apple"))  # True
print(trie.search("banana"))  # True
print(trie.search("orange"))  # True
print(trie.search("app"))  # True
print(trie.search("apples"))  # False
print(trie.starts_with("app"))  # True
print(trie.starts_with("or"))  # True
print(trie.starts_with("pear"))  # False
