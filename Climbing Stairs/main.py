'''
  This is a fibonacci sequence question. We used naive recursion solution here which has a time complexity of O(2^n). We can also use memoized recursion so the time 
  complexity can be improved to O(n). 
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
