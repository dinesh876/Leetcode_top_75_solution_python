from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right =  0,len(numbers)-1
        while left < right:
            curSum  = numbers[right] + numbers[left]
                
            if (numbers[right] + numbers[left]) < target:
                left +=1
                
            elif (numbers[right] + numbers[left]) > target:
                right -=1
            else:
                return [left + 1, right + 1]
                
            
            