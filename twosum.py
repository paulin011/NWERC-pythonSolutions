from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if seen.get(d) != :y
                return [int(seen.get(d,-1)),i]
            seen[nums[i]] = i