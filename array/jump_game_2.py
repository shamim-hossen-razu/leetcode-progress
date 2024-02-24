from typing import List
from collections import deque
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:  # If there is only one element, no moves are needed
            return 0
        
        queue = deque([(0, 0)])  # Queue to store (index, jumps) pairs
        visited = set()  # Set to store visited indices

        while queue:
            index, jumps = queue.popleft()  # Get the index and jumps from the queue

            # Explore all possible jumps from the current index
            for i in range(1, nums[index] + 1):
                next_index = index + i

                # If the next index is beyond the last index, return the number of jumps
                if next_index >= n - 1:
                    return jumps + 1

                # If the next index has not been visited, add it to the queue
                if next_index not in visited:
                    queue.append((next_index, jumps + 1))
                    visited.add(next_index)

        return -1  #
print(Solution().canJump([0]))