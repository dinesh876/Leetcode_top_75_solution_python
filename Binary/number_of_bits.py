# Solution 1
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2
            n = n >> 1
        return count
"""
# Solution 2
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
