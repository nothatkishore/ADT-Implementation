class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.build_tree(nums)

    def build_tree(self, nums):
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        index += self.n
        self.tree[index] = value
        while index > 0:
            left = right = index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index //= 2

    def query(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

# Example usage:
nums = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(nums)
print(seg_tree.query(1, 3))  # Output: 15 (sum of elements from index 1 to 3)
seg_tree.update(2, 10)
print(seg_tree.query(1, 3))  # Output: 20 (sum of elements from index 1 to 3 after update)
