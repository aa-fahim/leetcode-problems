'''
    Solution 1: Brute Force Method
    
    Time Complexity: O(m * n) where m is the number of columns and n is the number of rows of the matrix.
    
    Steps

    1. Iterate through each column
    2. Iterate through each row
    3. If any element in the row is zero, then set all elements in the row to zero
    4. Also record the index in extra memory, all other rows will have that index equal to zero as well.
    5. Iterate through the recorded columns in our hash table, and iterate over the rows of the matrix again and set each column in that row to zero.
    
    
    Notes: 
    Instead of setting the rows to zero in the first iteration, I could've done it in the second iteration where we are also setting the columns to zero.
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
   
        
        zeroColumnsIndex = {}
        
        for i in range(len(matrix)):
            setRowsToZero = False
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    setRowsToZero = True
                    zeroColumnsIndex[j] = 1    
                    
            if (setRowsToZero == True):
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
                    
                    
        for col in zeroColumnsIndex:
            for i in range(len(matrix)):
                matrix[i][col] = 0
