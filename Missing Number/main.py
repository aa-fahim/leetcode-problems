'''
  Brute Force Solution
  
  Time Complexity: O((n + 1) ^ 2) where n is the number of elements in the array.
  Space Complexity: O(n + 1)
  
  First pass, creates a temporary array storing all the numbers which the array should have. Second pass, loops through the temporary array and checks if the 
  current element exists in the nums array. If not, then end loop early and return the current element.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        arr = []
        
        for i in range(len(nums) + 1):
            arr.append(i)
            
        for i in arr:
            if i not in nums:
                return i
            
        return
'''

'''
  Bit Manipulation Solution
  
  Time Complexity: O(n + 1) where n is the number of elements in the array.
  Space Complexity: O(1)
  
  This solution uses an extra int variable where as the brute force solution uses an extra array variable of size n + 1. This solution also eliminates the need
  to check if the current element exists in our extra temporary array.
  
  In the first pass, the temporary variable is performed an XOR operation with the index value of the nums array. In the second pas, the temporary variable is
  performed an XOR operation with each element in the nums array. The resulting temporary variable is the missing number.
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(len(nums) + 1):
            res ^= i
            
        for num in nums:
            res ^= num
            
        return res
        
