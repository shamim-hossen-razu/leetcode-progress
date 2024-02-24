from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable_index = 0
        for i in range(len(nums)):
            if i > max_reachable_index:
                return False  # Cannot reach this index
            max_reachable_index = max(max_reachable_index, i + nums[i])
            if max_reachable_index >= len(nums) - 1:
                return True  # Can reach the last index
        return False
print(Solution().canJump([3,2,1,0,4]))