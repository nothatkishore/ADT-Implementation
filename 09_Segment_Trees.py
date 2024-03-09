#Revise BST in array form before practicing segment trees

class segment_tree:
    def __init__(self, nums) -> None:
        self.length = len(nums)
        self.tree = [0] * (2 * self.length)
        self.build_tree(nums)
    
    def build_tree(self, nums) -> None:
        
        for i in range(self.length):
            self.tree[self.length + i] = nums[i]
        for i in range(self.length - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[(2 * i) + 1]
        
    def update(self, index, value) -> None:
        index += self.length
        self.tree[index] = value
        
        while index > 0:
            right = left = index
            
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            
            self.tree[index // 2] = self.tree[right] + self.tree[left]
            index = index // 2
    
    def query(self, start, end) -> None:
        start += self.length
        end += self.length
        result = 0
        
        while start < end:
            if start % 2 == 1:
                result += self.tree[start]
                start += 1
            
            if end % 2 == 1:
                end -= 1
                result += self.tree[end]
            
            start = start // 2
            end = end // 2
        
        return result
    
    def print_tree(self):
        print(self.tree)
            
    
if __name__ == "__main__":
    S = segment_tree([1,2,3,4,5,6])
    print(S.query(0, 6))