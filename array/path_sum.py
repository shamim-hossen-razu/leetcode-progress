class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:  # Check if it's a leaf node
            return root.val == targetSum

        # Recursively check left and right subtrees
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

def create_binary_tree(arr, index):
    if index < len(arr) and arr[index] is not None:
        node = TreeNode(arr[index])
        node.left = create_binary_tree(arr, 2 * index + 1)
        node.right = create_binary_tree(arr, 2 * index + 2)
        return node
    return None

# Example usage:
root_values = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 1]
target_sum = 22

# Create the binary tree
root = create_binary_tree(root_values, 0)

# Create an instance of the Solution class
solution = Solution()

# Check if there exists a root-to-leaf path with the given sum
print(solution.hasPathSum(root, target_sum))  # Output: True
