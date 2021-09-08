class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []
        
        def findPermutation(currArr, remainingArr):
            if (len(remainingArr) == 0):
                res.append(currArr)
                return
            
            for i in range(len(remainingArr)):
                currElm = currArr + [remainingArr[i]]
                tmp = remainingArr[0:i] + remainingArr[i+1:]
                findPermutation(currElm, tmp)
        
        for i in range(len(nums)):
            currElm = nums[i]
            tmp = nums[0:i] + nums[i+1:]
            findPermutation([currElm], tmp)
        
        return res
