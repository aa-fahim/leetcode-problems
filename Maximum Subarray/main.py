'''
  Sliding Window Approach
  
  Time Complexity: O(n) where n is the number of elements in the array
  
  Increment end pointer by 1 every iteration. Increment start pointer only if the previous sum of the last found subarray is negative and the current element is greater
  than the previous sum. Find sum of current subarray and check if it is the largest maximum we have found so far.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -inf
        currSum = 0
        start = 0
        
        for i in range(len(nums)):
            if currSum < 0 and nums[i] >= currSum:
                start = i
                currSum = nums[i]
            else:
                currSum = sum(nums[start: i + 1])
            
            if (currSum > maxSum):
                maxSum = currSum
                
        return maxSum    
