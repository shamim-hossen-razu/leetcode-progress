from typing import List
class Solution:
    def hasPathSum(self, root_values: List[int], targetSum: int) -> bool:
        def dfs(index, current_sum):
            # Base case: index out of range
            if index >= len(root_values):
                return False
            # Calculate the current sum
            current_sum += root_values[index]
            # If it's a leaf node, check if current_sum equals targetSum
            if index * 2 + 1 >= len(root_values) or index * 2 + 2 >= len(root_values):
                return current_sum == targetSum
            # Recursively check left and right subtrees
            return dfs(index * 2 + 1, current_sum) or dfs(index * 2 + 2, current_sum)

        # Start DFS traversal from the root (index 0) with initial sum 0
        return dfs(0, 0)

# Example usage:
root_values = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 1]
target_sum = 22

# Create an instance of the Solution class
solution = Solution()

# Check if there exists a root-to-leaf path with the given sum
print(solution.hasPathSum(root_values, target_sum))  # Output: True
