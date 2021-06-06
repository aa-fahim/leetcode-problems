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
      
      
'''
    Sliding Window Approach
    
    Time Complexity: O(2n)
    
    1. Define starting/ending indices to be 0 and hash table to be empty
    2. Check if ending index character is in hash table (so have to shift our starting index until there are no duplicates in our hash table and deleting characters along the way.
        - If yes, find where starting index to be.
            - We can find where the starting index is by:
                1. Checking if the starting index character is equal to the ending index character.
                2. If not, delete the starting index character in hash table then increment starting index by 1.
                2. If yes, then increment by 1 and stop loop.
        
        - If no, define substring from starting index to ending index. Then
        check if the length of this substring is the largest length we've found so far.
    3. End loop when ending index extends string length.

'''
class Solution:   
    def lengthOfLongestSubstring(self, s: str) -> int:
        startIndex = 0
        endIndex = 0
        maxLength = 0
        hashTable = {}
        
        while(endIndex < len(s)):
            if (s[endIndex] in hashTable):
                while(True):
                    if (s[startIndex] == s[endIndex]):
                        startIndex += 1
                        endIndex += 1
                        break
                    else:
                        del hashTable[s[startIndex]]
                        startIndex += 1

            else:
                substring = s[startIndex: endIndex + 1]
                if (len(substring) > maxLength):
                    maxLength = len(substring)
                hashTable[s[endIndex]] = ""
                endIndex += 1

        return maxLength
      
      
'''
      Sliding Window Approach (Optimized)
      
      Time Complexity: O(n)
      
      We store the index of the characters in the hash table and update it accordingly. So when we come across repeated characters, we don't have to check where 
      the first occurence of the character is. We can jump to that index, therefore, we loop only the ending index whereas in the previous approach, we were
      looping the starting and ending indices which made it have a time complexity of 2n.
'''
class Solution:   
    def lengthOfLongestSubstring(self, s: str) -> int:
        startIndex = 0
        endIndex = 0
        maxLength = 0
        hashTable = {}
        
        while(endIndex < len(s)):
            if s[endIndex] in hashTable and (hashTable[s[endIndex]] != endIndex):
                if (hashTable[s[endIndex]] >= startIndex):
                    startIndex = hashTable[s[endIndex]] + 1
                    hashTable[s[endIndex]] = endIndex
                    endIndex += 1
                else:
                    hashTable[s[endIndex]] = endIndex

            else:
                substring = s[startIndex: endIndex + 1]
                if (len(substring) > maxLength):
                    maxLength = len(substring)
                hashTable[s[endIndex]] = endIndex
                endIndex += 1
        return maxLength
      
