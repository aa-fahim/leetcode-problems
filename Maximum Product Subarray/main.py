'''
  Time Complexity: O(n) where n is the number of elements in the array
  
  Approach iterates through each element in the array and records the minimum and maximum product subarrays seen so far. At each iteration, we check if multiplying
  the current minimum and maximum products with the current element produces a lower minimum product and a greater maximum product. We check to see if the 
  current maximum product is the largest integer we have seen so far and if the answer is yes, then store this integer in a varaible and return that variable after
  iterating through the array.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1
        currMax = 1
        res = -inf
        
        for i in range(len(nums)):
            tmp = currMin
            currMin = min(currMin * nums[i], currMax * nums[i], nums[i])
            currMax = max(tmp * nums[i], currMax * nums[i], nums[i])
            
            res = max(currMax, res)
        
        return res
