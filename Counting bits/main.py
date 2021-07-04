'''
  Solution 1: Loop through each index, convert index to binary representation then count number of 1 bits in the binary representation
  
  Time Complexity: O(n * m) where n is the input number and m is the longest binary representation which would be the binary representation of n + 1.
'''

class Solution:
    def hammingWeight(self, n: int) -> int:

        sum = 0
        for i in str(n):
            if i == '1':
                sum += 1
        
        return sum
    
    def countBits(self, n: int) -> List[int]:
        
        '''
            Steps
            1. Iterate through each previous number of n until we get to n + 1
            2. At each number, find the decimal representation of the number and append to array
        '''
        
        arr = []
        
        for i in range(n + 1):
            binary = int(bin(i)[2:])
            numOfOneBits = self.hammingWeight(binary)
            arr.append(numOfOneBits)
    
        return arr
    
    '''
      Solution 2: Involves DP
    '''
            
            
        
