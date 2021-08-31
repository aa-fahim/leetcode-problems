'''
  Solution loops through each element in the nums array and appends the element to all existing subsets and appends the new subset to our subset array.
  
  Time Complexity: O(2^n) where n is the number of elements in the array.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for i in range(len(nums)):
            for j in range(len(subset)):
                currentSubset = subset[j].copy()
                currentSubset.append(nums[i])
                subset.append(currentSubset)

        return subset
