class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashMap = {0: 0, 1:0, 2:0}
        for i in nums:
            hashMap[i] = hashMap[i] + 1
            
        for i in range(len(nums)):
            if hashMap[0] > 0:
                nums[i] = 0
                hashMap[0] = hashMap[0] - 1
            elif hashMap[1] > 0:
                nums[i] = 1
                hashMap[1] = hashMap[1] - 1
            elif hashMap[2] > 0:
                nums[i] = 2
                hashMap[2] = hashMap[2] - 1
