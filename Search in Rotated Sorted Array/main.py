'''
    Fast and slow pointer approach
    
    Time Complexity: O(n/2) where n is the number of elements in the array.

    Slow pointer begins at index 0. Fast pointer starts at middle of array.
    If slow pointer index value < target, increment slow pointer until we find target.
    If fast pointer index value < target, increment fast pointer until we find target.
    
    Notes:
    This method isn't very good because time complexity is still very high (we only halve it using fast and slow pointer approach).
'''
import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        mid = math.floor(len(nums)/2)
        slow = 0
        fast = mid
        res = -1

        if nums[slow] <= target:
            res = self.incrementCounter(slow, nums, target)
        elif nums[fast] <= target:
            res = self.incrementCounter(fast, nums, target)
        else:
            res = self.incrementCounter(slow, nums, target)
            
        return res
    
    def incrementCounter(self, index, nums, target):
        
        for i in range(index, len(nums)):
            if nums[i] == target:
                return i
            
        return -1
            
