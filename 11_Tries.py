class Node:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    def insert(self, word) -> None:
        current_node = self.root
        
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = Node()
            current_node = current_node.children[character]
        
        current_node.isEnd = True
    
    def search(self, word) -> bool:
        current_node = self.root
        
        for character in word:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return current_node.isEnd    
    
    def remove(self):
        pass
            

if __name__ == "__main__":
    T = Trie()
    T.insert("Kishore")
    print(T.search("Kish"))