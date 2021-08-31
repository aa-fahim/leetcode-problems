'''
  Naive Recursion Solution
  
  Time Complexity: O(2^n) 

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1 or n == 2:
            return 1
        
        return self.fib(n-1) + self.fib(n-2)
'''

'''
  Memoized Recursion Solution
  
  Time Complexity: O(n)
'''
hashTable = {}
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1 or n == 2:
            return 1
        if n in hashTable:
            return hashTable[n]
        
        result = self.fib(n-1) + self.fib(n-2)
        hashTable[n] = result
        return result
