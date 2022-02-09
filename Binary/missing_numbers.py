from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number = 0
        for i in range(0, len(nums) + 1):
            if i not in nums:
                number = i
        return number
