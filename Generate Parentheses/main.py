'''
  Backtracking Approach
  
  This approach uses recursion to track the number of opening and closing brackets already existing in the string. Then based on these conditions we either append
  an opening bracket, closing bracket, or return the string. We append all strings to an array variable which we return as the final answer.
  
  Time Complexity: O(4^n / sqrt(n)) where n is the number of characters in the string
    - based on the Catalan number
    - can also say O(2*n) for less complex answer
    
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def createSubset(str, numOpening, numClosing):
            if numOpening == n and numClosing == n:
                res.append(str)
                return 
            
            if numOpening == numClosing:
                tmp = str + '('
                createSubset(tmp, numOpening + 1, numClosing)
            
            if numOpening > numClosing:
                if numOpening <= n:
                    createSubset(str + '(', numOpening + 1, numClosing)
                if numClosing <= n:
                    createSubset(str + ')', numOpening, numClosing + 1)
        
        createSubset('', 0, 0)
        return res
