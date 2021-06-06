'''
  Brute Force Method
  
  Time Complexity: O(n^3)
  
  Check every substring possible, then check if the substring has any duplicates.
'''
class Solution:
    def checkUniqueString(self, s: str) -> bool:
        hashTable = {}
        for i in s:
            if i in hashTable:
                return False
            else:
                hashTable[i] = 0
        return True
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        for i in range(len(s)):
            substring = ''
            for j in range(i, len(s)-1):
                substring += s[j]
                isUniqueSubstring = self.checkUniqueString(substring)
                if (isUniqueSubstring):
                    length = len(substring)
                    if (length > maxLength):
                        maxLength = length
        
        return maxLength
      
