'''
  Time Complexity: O(n*m) where n is the number of rows and m is the number of columns of the matrix.
  
  Approach
  Create a set for every row, column and subbox of the matrix. Iterate through each element in the matrix and see if the element already exists in the respective row set,
  column set, and subbox set. If exists, break loop and return false. Else add element to respective row set, column set and subbox set. Return true if no element
  has broken the condition.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        subboxes = {}
        res = True
        
        for i in range(len(board[0])):
            rows[i] = set()
            for j in range(len(board[0])):
                if j not in cols:
                    cols[j] = set()
                val = board[i][j]
                subboxRow = i // 3
                subboxCol = j // 3
                subboxKey = str(subboxCol) + str(subboxRow)
                if subboxKey not in subboxes:
                    subboxes[subboxKey] = set() 
                if (val == '.'):
                    continue
                if (val not in rows[i] and val not in cols[j] and val not in subboxes[subboxKey]):
                    rows[i].add(val)
                    cols[j].add(val)
                    subboxes[subboxKey].add(val)
                    continue
                else:
                    res = False
                    break
                
            if (res == False):
                break

        return res
                
        
