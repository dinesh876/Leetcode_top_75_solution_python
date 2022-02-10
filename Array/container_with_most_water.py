from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l+1,len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res

        # LINEAR TIME SOLUTION
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(area, res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))
